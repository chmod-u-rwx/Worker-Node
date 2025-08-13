import os # type:ignore
from pathlib import Path
from enum import Enum
import subprocess
import shlex # type:ignore
import time
import paramiko

class QemuStatus(Enum):
    STARTED = 1
    STOPPED = 2
    RUNNING = 3

class QemuController:
    def __init__(self, img_path: Path, cpu_count: int = 1, memory_allocated: int = 0) -> None:
        self.img_path = img_path 
        self.snapshot_name = "base"
        self.cpu_count = cpu_count
        self.memory_allocated = memory_allocated
        self.status = QemuStatus.STOPPED
        self.boot_time = 0
        self.ssh = paramiko.SSHClient()

    def start(self):
        if self.img_path.exists() == False:
            raise RuntimeError(f"QEMU img not found at {self.img_path}. Ensure that PATH to img is correct.")
        
        command = [
            "qemu-system-x86_64",
            "-machine", "accel=kvm:tcg,usb=off",
            "-m", f"{self.memory_allocated}M",
            "-cpu", "host",
            "-smp", str(self.cpu_count),
            "-hda", str(self.img_path),
            "-loadvm", str(self.snapshot_name),
            "-net", "nic", "-net", "user,hostfwd=tcp::2222-:22",
            "-nographic",
            "-enable-kvm"
        ]

        if self.status == QemuStatus.STARTED:
            raise RuntimeError("QEMU is already running")        

        try:
            start_time = time.perf_counter()
            
            self.proc = subprocess.Popen(command)
            time.sleep(0.5)
            if self.proc.poll() is not None:
                raise RuntimeError(f"Failed to start QEMU process due to an error in the command. Return Code {self.proc.returncode}")
            
            if (self.check_ssh_connection()):
                self.boot_time = (time.perf_counter() - start_time)*1000

            self.status = QemuStatus.STARTED
            print(f"VM booted in {self.boot_time:.2f} ms.")

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

            if (not self.check_ssh_connection()):
                raise ConnectionError("SSH connection failed. QEMU is not ready for command execution.")
            
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
    
    def check_ssh_connection(self, port: int = 2222, user: str = "root", password:str ="root", timeout: int = 60) -> bool:
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

