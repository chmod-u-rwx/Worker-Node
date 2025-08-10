import subprocess
import os
import shutil
from pathlib import Path
from enum import Enum
from ..helpers.process import clean_proccess
from ..helpers.socket import wait_for_file_socket_availability
from ..config import BASE_IMG_FILE

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
        
        # Copy the base img file into img_path
        shutil.copy(BASE_IMG_FILE, img_path)

        self.virtualization = virtualization
        self.img_path = img_path 
        self.cpu_count = cpu_count
        self.snapshot_name = "base"
        self.memory_allocated = memory_allocated
        self.status = QemuStatus.STARTED

    def start(self):
        ...
    
    def stop(self):
        ...

    def reset(self) -> None:
        ...
    
    def run_command(self):
        ...
    
    def get_status(self):
        ...

    def create_snapshot(self):
        # using file based socket, to interact with qemu monitor


        proc_qemu = self._start_qemu_with_monitor()

        try:
            # wait for qemu monitor socket to open
            self._wait_qemu_monitor_socket(proc_qemu)

            # Connect using socat 
            self._save_vm()

        finally:
            # terminate the process. force exit after 5 secs
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
        
