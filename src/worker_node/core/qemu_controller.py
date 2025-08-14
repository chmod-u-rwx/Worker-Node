import os
import shutil
import time
import subprocess
from pathlib import Path
from enum import Enum
from typing import List 
from typing import Optional

from ..helpers.process import clean_process
from ..helpers.socket import wait_for_file_socket_availability
from ..config import BASE_IMG_FILE
from ..models.vm_output import VMOutput
import paramiko

class QemuStatus(Enum):
    STARTED = 1
    STOPPED = 2
    RUNNING = 3

class QemuController:
    def __init__(self, img_path: Path, virtualization: str, cpu_count: int = 1, memory_allocated: int = 0, ) -> None:
        if not os.path.exists(BASE_IMG_FILE):
            raise FileNotFoundError("Base img does not exist")

        virtualization = virtualization.lower() 
        if virtualization not in ["macos", "linux"]:
            raise ValueError("Virtualization must be 'macos' or 'linux' only") 
        
        self.virtualization = virtualization
        self.img_path = img_path 
        self.cpu_count = cpu_count
        self.snapshot_name = "base"
        self.memory_allocated = memory_allocated
        self.status = QemuStatus.STOPPED
        self.boot_time = 0
        self.ssh = paramiko.SSHClient()

        # Copy the base img file into img_path
        shutil.copy(BASE_IMG_FILE, img_path)
        self.create_snapshot()

    def start(self):
        if self.img_path.exists() == False:
            raise RuntimeError(f"QEMU img not found at {self.img_path}. Ensure that PATH to img is correct.")

        if os.path.exists("/tmp/qemu.sock"):
            os.remove("/tmp/qemu.sock")

        if self.status == QemuStatus.STARTED:
            raise RuntimeError("QEMU is already running")        
        
        command = self._get_qemu_cmd(True)

        try:
            start_time = time.perf_counter()
            
            self.proc = subprocess.Popen(command, text=True)
            time.sleep(0.5)
            if self.proc.poll() is not None:
                raise RuntimeError(f"Failed to start QEMU process due to an error in the command. Return Code {self.proc.returncode}")
            
            if (self.wait_for_ssh_connection()):
                self.boot_time = (time.perf_counter() - start_time)*1000

            self.status = QemuStatus.STARTED
            print(f"VM booted in {self.boot_time:.2f} ms.")

        except FileNotFoundError:
            self.status = QemuStatus.STOPPED
            raise RuntimeError("QEMU img not found. Ensure that PATH to img is correct.")
        except Exception as e:
            self.status = QemuStatus.STOPPED
            raise RuntimeError(f"An unexpected error occurred: {str(e)}")
    
    def stop(self):
        if self.status != QemuStatus.STARTED:
            raise RuntimeError("QEMU is not STARTED")

        if self.proc:
            self.proc.terminate()
            try:
                self.proc.wait(timeout=10)
            except subprocess.TimeoutExpired:
                self.proc.kill()  # force kill if still alive
                self.proc.wait()

            self.status = QemuStatus.STOPPED
            print("VM stopped successfully.")
        else:
            raise RuntimeError("No QEMU process found")

    def reset(self) -> None:
        ...

    def freeze(self):
        if self.status != QemuStatus.STARTED:
            raise Exception("Qemu has not yet started")

        try:
            self._send_command_to_qemu_monitor("/tmp/qemu.sock", "stop")
        except (RuntimeError, TimeoutError) as e:
            raise RuntimeError("Failed to freeze vm") from e
        
    
    def resume(self):
        if self.status != QemuStatus.STARTED:
            raise Exception("Qemu has not yet started")

        try:
            self._send_command_to_qemu_monitor("/tmp/qemu.sock", "cont")
        except (RuntimeError, TimeoutError) as e:
            raise RuntimeError("Failed to resume vm") from e
        
    def run_command(self, command:List[str], timeout:int = 30) -> VMOutput:
        start_time = time.perf_counter()
        if self.status != QemuStatus.STARTED:
            raise RuntimeError("QEMU is not STARTED. Cannot run command.")
        
        self.wait_for_ssh_connection()
        
        self.status = QemuStatus.RUNNING
        cmd = " ".join(command)
        error_buffer = ""

        while (time.perf_counter() - start_time) < timeout:
            try:
                self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                self.ssh.connect("localhost", port=2222, username="root", password="root", timeout=1)

                _, stdout, stderr = self.ssh.exec_command(cmd)
                returncode = stdout.channel.recv_exit_status()

                output = VMOutput(
                    stdin=cmd,
                    stdout=stdout.read().decode("utf-8"),
                    stderr=stderr.read().decode("utf-8"),
                    returncode=returncode,
                    runtime=f"{(time.perf_counter() - start_time) * 1000:.2f} ms"
                )                    
                return output

            except RuntimeError as e:
                error_buffer = f"Runtime error: {str(e)}\n"
                time.sleep(1)
            except paramiko.SSHException as e:
                error_buffer = f"SSH error: {str(e)}\n"
                time.sleep(1)
            except Exception as e:
                error_buffer = f"Unexpected error: {str(e)}\n"
                time.sleep(1)
            finally:
                self.status = QemuStatus.STARTED
                self.ssh.close()

        raise TimeoutError(f"Command execution timed out after {timeout} seconds. Last known error: {error_buffer}")

    
    def get_status(self) -> dict[str, str]:
        result = subprocess.run(["ps", "-p", str(self.proc.pid), "-o", "%cpu=,mem=,pid=", ""], capture_output=True, text=True)
        cpu_usage, memory_usage, pid = result.stdout.strip().split(" ")
        print(cpu_usage, memory_usage, pid)
        return {
            "cpu_usage": cpu_usage,
            "memory_usage": memory_usage,
            "pid": pid
        }

    def create_snapshot(self):
        proc_qemu = self._start_qemu_no_loadvm()
        try:
            # This only checks monitor socket and it gets ready
            # before the vm has fully booted up
            self._wait_qemu_monitor_socket(proc_qemu)
            
            # By checking for ssh, we ensure that alpine linux
            # is completely booted before savevm
            self.wait_for_ssh_connection()
            self._send_command_to_qemu_monitor("/tmp/qemu.sock", f"savevm {self.snapshot_name}")
        finally:
            clean_process(proc=proc_qemu)
        
    def _get_qemu_cmd(self, loadvm: bool = False) -> list[str]:
        """
        Returns the proper qemu command based on virtualization.
        Loads self.snapshot if loadvm = True
        """
        
        accel = "tcg" if self.virtualization == "macos" else "kvm:tcg,usb=off"
        cpu = "max" if self.virtualization == "macos" else "host"

        cmd = [
            "qemu-system-x86_64",
            "-machine", f"accel={accel}",
            "-cpu", cpu,
            "-smp", str(self.cpu_count),
            "-m", f"{self.memory_allocated}M",
            "-hda", str(self.img_path),
            "-netdev", "user,id=net0,hostfwd=tcp::2222-:22",
            "-device", "virtio-net,netdev=net0",
            "-monitor", "unix:/tmp/qemu.sock,server,nowait",
            "-nographic"
        ]

        if self.virtualization == "linux":
            cmd.append("-enable-kvm")
        if loadvm:
            cmd.extend(["-loadvm", self.snapshot_name])

        return cmd 
    
    def _start_qemu_no_loadvm(self) -> subprocess.Popen[str]:
        qemu_cmd = self._get_qemu_cmd()

        try:
            proc_qemu = subprocess.Popen(
                qemu_cmd,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.PIPE,
                text=True)
            
            return proc_qemu
            
        except FileNotFoundError:
            raise RuntimeError("Qemu binary not found. Not installed?")
    
    def _wait_qemu_monitor_socket(self, proc_qemu: subprocess.Popen[str]): 
        """
        This wait the qemu monitor socket if its ready so that we can
        connect to it and save the vm.
        """

        if wait_for_file_socket_availability("/tmp/qemu.sock"): 
            return

        try:
            _, qemu_stderr = proc_qemu.communicate(timeout=5) 
        except subprocess.TimeoutExpired:
            qemu_stderr = "Timeout reading Qemu stderr"
        finally: 
            clean_process(proc_qemu)

        raise RuntimeError(f"Qemu monitor socket failed to start in time. \nQemu stderr: {qemu_stderr}")

    def _send_command_to_qemu_monitor(self, file_socket: str, command: str, return_stdout: bool = False) -> Optional[str]:
        """ 
        Sends a qemu command to the qemu monitor socket by connecting to it using
        socat. If return_stdout = True, it returns the stdout of the process.
        """

        try:
            proc = subprocess.Popen(
                ["socat", "-", f"unix-connect:{file_socket}"],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True)
        except FileNotFoundError:
            raise RuntimeError("socat command not found. Is socat installed?")
        except OSError as e:
            raise RuntimeError("Failed to start socat") from e

        try:
            stdout, stderr = proc.communicate(input=f"{command}\n", timeout=10)
        except subprocess.TimeoutExpired:
            raise TimeoutError("socat timed out while sending command")
        finally:
            clean_process(proc=proc)
        
        if proc.returncode != 0:
            raise RuntimeError(f"socat exited with error: {stderr.strip()}")
        
        if return_stdout:
            return stdout.strip()
        
    def wait_for_ssh_connection(self, port:int=2222, user:str="root",password:str="root", timeout:int=60) -> bool:
        """
        Poll SSH on localhost:port until authentication succeeds,
        meaning the server is ready for communication.
        """
        # if self.status != QemuStatus.STARTED:
        #     raise RuntimeError("QEMU is not STARTED. Cannot wait for SSH connection.")
        
        start_time = time.perf_counter()
        while (time.perf_counter() - start_time) < timeout:
            try:
                self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                self.ssh.connect("localhost", port=port, username=user, password=password, timeout=1)
                self.ssh.close()
                return True
            except Exception:
                time.sleep(0.05)

        raise TimeoutError("SSH authentication failed. Server not ready.")
    
    def delete(self):
        ...

