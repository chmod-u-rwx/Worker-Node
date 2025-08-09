import subprocess
from pathlib import Path
from enum import Enum


class QemuStatus(Enum):
    STARTED = 1
    STOPPED = 2
    RUNNING = 3

class QemuController:
    def __init__(self, img_path: Path, cpu_count: int = 1, memory_allocated: int = 0) -> None:
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


    def _get_qemu_cmd(self, virtualization: str, loadvm: bool = False) -> str:
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
        accel = "tcg" if virtualization == "macos" else "kvm:tcg"
        cpu = "max" if virtualization == "macos" else "host"
        kvm = "-enable-kvm" if virtualization == "linux" else ""
        loadvmflag = f"-loadvm {self.snapshot_name}" if loadvm else "" 

        cmd = (
            "qemu-system-x86_64",
            f"-machine accel={accel},usb=off",
            f"-cpu {cpu}",
            f"-smp {self.cpu_count}"
            f"-m {self.memory_allocated}M",
            f"-hda {self.img_path}",
            "-netdev user,id=net0,hostfwd=tcp::2222-:22",
            "-device virtio-net,netdev=net0",
            "-nographic",
            kvm,
            loadvmflag
        )
        
        return " ".join(filter(None, cmd))
    