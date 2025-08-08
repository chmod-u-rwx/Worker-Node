import subprocess
import pexpect
from pathlib import Path
from enum import Enum


class QemuStatus(Enum):
    STARTED = 1
    STOPPED = 2
    RUNNING = 3

class QemuController:
    def __init__(self, img_path: Path, cpu_count: int = 1, memory_allocated: int = 0) -> None:
        self.img_path = img_path 
        self.cpu_coun = cpu_count
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

    def create_qcow2_img(self, path: Path, size_mb: int) -> None:
        """ 
        Creates a qcow2 disk file for installing alpine linux into.

        Args:
            img_name (str): name of the qcow2 file
            size (int): size of the disk file in Megabytes
        """

        if size_mb < 50:
            raise ValueError("qcow2 size must atleast be 50 Mb")

        if path.exists() and path.is_dir():
            raise ValueError(f"Provided path '{path}' is a dir")

        if path.suffix != ".qcow2":
            path = path.with_suffix(".qcow2")


        try:
            subprocess.run(["qemu-img", "create", "-f", "qcow2", str(path), f"{size_mb}M"],
                   check=True)
            print(f"Successfully created {path} disk file")
            
        except subprocess.CalledProcessError as e:
            print("Failed to create qcow2 image. \n")
            print(f"Command output: \n{e}")
            raise


    def setup_alpine_linux(self, qcow2_file: Path, alpine_iso: Path, virtualization: str):
        """
        Setups up and install alpine linux on qcow2_file.

        Args:
            qcow2_file (Path)
            virtualization (str): May be 'macos' or 'linux' (for now)
        """

        self._validate_setup_args(qcow2_file, alpine_iso, virtualization)

        cmd = QemuController._get_qemu_cmd(qcow2_file, alpine_iso, virtualization)

        child = pexpect.spawn(cmd, timeout=35)		 # type: ignore

        # setup-alpine sequential prompts
        prompts_and_responses = QemuController._get_alpine_setup_prompts()

        for prompt, response in prompts_and_responses:
            try:
                child.expect(prompt)
                child.sendline(response)
            except pexpect.TIMEOUT:
                print(f"Timeout waiting for: {prompt}")
                raise
            except pexpect.EOF:
                print("Qemu process ended unexpectedly.")
                raise
        else:
            try:
                child.expect("Installation is complete")
                print("Installation completed successfully.")
            except pexpect.TIMEOUT:
                raise Exception("Installation did not complete in time.")
            except pexpect.EOF:
                raise Exception("QEMU process ended before installation finished.")
        

    @staticmethod
    def _get_qemu_cmd(qcow2_file: Path, alpine_iso: Path, virtualization: str) -> str:
        """
        Returns the proper qemu command based on virtualization.

        Args:
            qcow2_file (Path): 
            alpine_iso (Path): 
            virtualization (str): macos or linux

        Returns:
            str: The qemu command
        """
        accel = "kvm:tcg" if virtualization == "macos" else "tcg"
        cpu = "max" if virtualization == "macos" else "host"
        kvm = "-enable-kvm" if virtualization == "linux" else ""

        cmd = (
            "qemu-system-x86_64",
            f"-machine accel={accel},usb=off",
            f"-cpu {cpu}",
            "-m 512M",
            f"-cdrom {alpine_iso}",
            f"-hda {qcow2_file}",
            "-netdev user,id=net0,hostfwd=tcp::2222-:22",
            "-device virtio-net,netdev=net0",
            "-nographic",
            kvm
        )
        
        return " ".join(filter(None, cmd))
    

    def _validate_setup_args(self, qcow2_file: Path, alpine_iso: Path, virtualization: str) -> None:
        if not qcow2_file.exists():
            raise ValueError(f"Provided qcow2 file '{qcow2_file}' does not exist.")
        
        if not alpine_iso.exists():
            raise ValueError(f"{alpine_iso} does not exist.")
        
        if virtualization not in ["macos", "linux"]:
            raise ValueError(f"Provided invalid virtualization '{virtualization}'. Expects 'macos' or 'linux'.")
    
    @staticmethod
    def _get_alpine_setup_prompts() -> list[tuple[str, str]]:
        return [
            ("localhost login:", "root"),
            ("Password:", ""),  # empty password

            # Start of setup
            ("localhost:~#", "setup-alpine"),
            
            # Hostname
            ("Enter system hostname", ""),
            # Network interface
            ("Which one do you want to initialize?", ""),
            ("Ip address for eth0?", ""),

            # Root password
            ("New password:", ""),
            ("Retype password:", ""),

            # Timezone
            ("Which timezone are you in?", "Asia"),
            ("Which timezone are you in", "Manila"),

            # Proxy. default: none 
            ("HTTP/FTP proxy URL?", ""),
            # NTP. default: busybox
            ("Which NTP client to run?", ""),
            # Mirrors 
            ("Enter mirror number", ""),
            # User setup. default: no
            ("Setup a user?", ""),
            # SSH. default: openssh
            ("Which ssh server?", ""),
            # default: prohibit-password
            ("Allow root ssh login?", ""),
            # default: none
            ("Enter ssh key", ""),
            
            # Disk setup
            ("Which disk(s) would you like to use?", "sda"),
            ("How would you like to use it?", "sys"),
            ("Erase the above disk", "y"),
        ]