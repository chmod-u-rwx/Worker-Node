import subprocess
import time
import os
import socket
from pathlib import Path
from enum import Enum
from typing import Optional


class QemuStatus(Enum):
    STARTED = 1
    STOPPED = 2
    RUNNING = 3

class QemuController:
    def __init__(self, img_path: Path, virtualization: str, cpu_count: int = 1, memory_allocated: int = 0, ) -> None:

        if not img_path.exists():
            raise FileNotFoundError("Base img does not exist")

        virtualization = virtualization.lower() 

        self._validate_virtualization(virtualization)

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


    def _get_qemu_cmd(self, loadvm: bool = False) -> list[str]:
        """
        Returns the proper qemu command based on virtualization.
        This command assumes qcow2 img has no alpine installed yet

        Args:
            qcow2_file (Path): 
            alpine_iso (Path): 
            virtualization (str): macos or linux
            loadvm (bool): loads self.snapshot_name if True, otherwise boot from qcow2 img

        Returns:
            str: The qemu command
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
    

    def _validate_virtualization(self, virtualization: str):
        if virtualization not in ["macos", "linux"]:
            raise ValueError("Virtualization must be 'macos' or 'linux' only") 
            


    def _wait_for_socket(self, file_socket: str, timeout: int=10):
        start = time.time()

        while time.time() - start < timeout:
            try:
                with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
                    sock.connect(file_socket)
                    return True
            except (FileNotFoundError, ConnectionRefusedError):
                time.sleep(0.5)

        return False
    
    def wait_for_qemu_socket(self, proc_qemu: subprocess.Popen[str]):
        if not self._wait_for_socket("/tmp/qemu.sock"):
            # Try to capture qemu proc stderr
            try:
                _, qemu_stderr = proc_qemu.communicate(timeout=5)
            except subprocess.TimeoutExpired:
                proc_qemu.kill()
                proc_qemu.wait()
                qemu_stderr = "Timeout reading Qemu stderr"
            
            proc_qemu.terminate()
            proc_qemu.wait()

            raise RuntimeError(f"Qemu monitor socket failed to start in time. \nQemu stderr: {qemu_stderr}")
        

    def run_socat_save_vm(self):
        # Connect using socat 
        proc = subprocess.Popen(
            ["socat", "-", "unix-connect:/tmp/qemu.sock"],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)


        try:
            stdout, stderr = proc.communicate(input=f"savevm {self.snapshot_name}\n", timeout=10)
        
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.wait()

            raise RuntimeError("socat timed out while sending savevm command")
        
        finally:
            # proc is still running
            self._cleanup_proc_gracefully(proc=proc)
                
        
        print("socat output: ", stdout)

        # 0 means success
        if proc.returncode != 0:
            raise RuntimeError(f"socat exited with error: \n{stderr}")
        

    def start_qemu(self, qemu_cmd: list[str]) -> subprocess.Popen[str]:
        try:
            proc_qemu = subprocess.Popen(
                qemu_cmd,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.PIPE,
                text=True)
            
            return proc_qemu
            
        except FileNotFoundError:
            raise RuntimeError("Qemu binary not found. Not installed?")


    def create_snapshot(self):

        qemu_cmd = self._get_qemu_cmd()

        # using file based socket on /tmp/qmp.sock
        qemu_cmd.extend(["-monitor", f"unix:/tmp/qemu.sock,server,nowait"])

        if os.path.exists("/tmp/qemu.sock"):
            os.remove("/tmp/qemu.sock")

        proc_qemu = self.start_qemu(qemu_cmd=qemu_cmd)

        try:
            # wait for qemu monitor socket to open
            self.wait_for_qemu_socket(proc_qemu=proc_qemu)

            # Connect using socat 
            self.run_socat_save_vm()

        finally:
            # terminate the process. force exit after 5 secs
            self._cleanup_proc_gracefully(proc_qemu)


    def _cleanup_proc_gracefully(self, proc: subprocess.Popen[str], timeout: int = 5):
        if proc.poll() is None:
            proc.terminate()

            try:
                proc.wait(timeout=timeout)
            except subprocess.TimeoutExpired:
                proc.kill()
                proc.wait()