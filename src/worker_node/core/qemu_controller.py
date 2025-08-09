from pathlib import Path
from enum import Enum
import subprocess
import shlex
import time

class QemuStatus(Enum):
    STARTED = 1
    STOPPED = 2
    RUNNING = 3

class QemuController:
    def __init__(self, img_path: Path, cpu_count: int = 1, memory_allocated: int = 0) -> None:
        self.img_path = img_path 
        self.snapshot_name = "kvm-fastboot" #"base"
        self.cpu_count = cpu_count
        self.memory_allocated = memory_allocated
        self.status = QemuStatus.STOPPED
        self.boot_time = 0

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

        self.status = QemuStatus.STARTED
        try:
            start_time = time.perf_counter()
            
            self.proc = subprocess.Popen(command)
            time.sleep(0.5)
            if self.proc.poll() is not None:
                raise RuntimeError(f"Failed to start QEMU process due to an error in the command. Return Code {self.proc.returncode}")
            
            if (self.check_ssh_connection()):
                self.boot_time = (time.perf_counter() - start_time)*1000

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
    
    def run_command(self):
        ...
    
    def get_status(self):
        ...

    def check_ssh_connection(self, port:int=2222, user:str="root", timeout:int=60) -> bool:
        """
        Poll SSH on localhost:port until SSH responds with 'Permission denied',
        indicating the server is up and requesting authentication.
        """
        ssh_cmd = (
            f"ssh -p {port} -o StrictHostKeyChecking=no "
            f"-o BatchMode=yes -o ConnectTimeout=1 {user}@localhost true"
        )

        start_time = time.perf_counter()
        result = None

        while (time.perf_counter() - start_time) < timeout:
            result = subprocess.run(
                shlex.split(ssh_cmd),
                stdout=subprocess.DEVNULL,
                stderr=subprocess.PIPE,
                text=True,
            )

            if "Permission denied" in result.stderr:
                return True # if returned SSH can connect
            
            time.sleep(0.05)

        last_error = result.stderr.strip() if result else "No result from SSH command"
        raise TimeoutError(f"SSH connection failed. Last error: {last_error}")