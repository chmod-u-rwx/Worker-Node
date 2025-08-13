import os
import shutil
import time
import subprocess
from pathlib import Path
from enum import Enum
from ..helpers.process import clean_proccess
from ..helpers.socket import wait_for_file_socket_availability
from ..config import BASE_IMG_FILE
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

        if self.status == QemuStatus.STARTED:
            raise RuntimeError("QEMU is already running")        
        
        command = self._get_qemu_cmd(True)

        try:
            start_time = time.perf_counter()
            
            self.proc = subprocess.Popen(command)
            time.sleep(0.5)
            if self.proc.poll() is not None:
                raise RuntimeError(f"Failed to start QEMU process due to an error in the command. Return Code {self.proc.returncode}")
            
            if (self.wait_for_ssh_connection()):
                self.boot_time = (time.perf_counter() - start_time)*1000

            self.status = QemuStatus.STARTED
            print(f"VM booted in {self.boot_time:.2f} ms.")

            self.status = QemuStatus.STARTED
        except FileNotFoundError:
            self.status = QemuStatus.STOPPED
            raise RuntimeError("QEMU img not found. Ensure that PATH to img is correct.")
        except subprocess.CalledProcessError as e:
            self.status = QemuStatus.STOPPED
            raise RuntimeError(f"QEMU exited with an error code {e.returncode}. Command: {' '.join(command)}")
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
    
    def run_command(self, file_name: str, type:str) -> str:
        start_time = time.perf_counter()
        if self.status != QemuStatus.STARTED:
            raise RuntimeError("QEMU is not STARTED. Cannot run command.")
        
        try:
            self.status = QemuStatus.RUNNING
            cmd = f"python3 {file_name} {type}"

            if (not self.wait_for_ssh_connection()):
                raise ConnectionError("SSH test connection failed. QEMU is not ready for command execution.")
            
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect("localhost", port=2222, username="root", password="root", timeout=1)

            stdin, stdout, stderr = self.ssh.exec_command(cmd) #type:ignore
            returncode = stdout.channel.recv_exit_status()

            if returncode != 0:
                return f"Error: {stderr.read().decode("utf-8")}"
            
            elapsed_time = (time.perf_counter() - start_time) * 1000
            print(f"Command executed in {elapsed_time:.2f} ms.")
            return f"Output: {stdout.read().decode("utf-8")}"
        
        except paramiko.SSHException as e:
            raise RuntimeError(f"SSH connection error: {str(e)}")
        except Exception as e:
            raise RuntimeError(f"An error occurred while running the command: {str(e)}")
        finally:
            self.status = QemuStatus.STARTED
            self.ssh.close()

    
    def get_status(self):
        ...


    def create_snapshot(self):
        proc_qemu = self._start_qemu_with_monitor()
        try:
            # This only checks monitor socket and it gets ready
            # before the vm has fully booted up
            self._wait_qemu_monitor_socket(proc_qemu)
            
            # By checking for ssh, we ensure that alpine linux
            # is completely booted before savevm
            self.wait_for_ssh_connection()
            self._save_vm()
        finally:
            clean_proccess(proc=proc_qemu)
        
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
            "-nographic"
        ]

        if self.virtualization == "linux":
            cmd.append("-enable-kvm")
        if loadvm:
            cmd.extend(["-loadvm", self.snapshot_name])

        return cmd 
    
    def _start_qemu_with_monitor(self) -> subprocess.Popen[str]:
        qemu_cmd = self._get_qemu_cmd()
        qemu_cmd.extend(["-monitor", f"unix:/tmp/qemu.sock,server,nowait"])

        if os.path.exists("/tmp/qemu.sock"):
            os.remove("/tmp/qemu.sock")

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
            # Try to get the stderr from qemu to give a more detailed
            # error message
            _, qemu_stderr = proc_qemu.communicate(timeout=5) 

        except subprocess.TimeoutExpired:
            # fallback if we cant get the stderr
            qemu_stderr = "Timeout reading Qemu stderr"
        finally: 
            clean_proccess(proc_qemu)

        raise RuntimeError(f"Qemu monitor socket failed to start in time. \nQemu stderr: {qemu_stderr}")

    def _save_vm(self):
        """ 
        Sends a savevm command to the qemu monitor socket by connecting to it using
        socat.
        """

        proc = subprocess.Popen(
            ["socat", "-", "unix-connect:/tmp/qemu.sock"],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)

        try:
            # sending the savevm command
            _, stderr = proc.communicate(input=f"savevm {self.snapshot_name}\n", timeout=10)
        
        except subprocess.TimeoutExpired:
            # happens if for some reason socat cant send the command until timeout
            raise TimeoutError("socat timed out while sending savevm command")
        
        finally:
            clean_proccess(proc=proc)
        
        # the process when wrong if its not 0
        if proc.returncode != 0:
            raise RuntimeError(f"socat exited with error: \n{stderr}")
        
    def wait_for_ssh_connection(self, port:int=2222, user:str="root",password:str="root", timeout:int=60) -> bool:
        """
        Poll SSH on localhost:port until authentication succeeds,
        meaning the server is ready for communication.
        """

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

