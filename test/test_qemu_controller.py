from pathlib import Path
from src.worker_node.core.qemu_controller import QemuController,QemuStatus
import subprocess

def test_qemu_controller():
    qemu = QemuController(Path("/home/dan/Projects/qemu-node/alpine-stndrd/new-alpine.qcow2"), cpu_count=2, memory_allocated=512)

    try:
        qemu.start()
        assert qemu.check_ssh_connection(), "SSH connection failed after starting QEMU"
        assert qemu.status == QemuStatus.STARTED, "QEMU did not start successfully"
        assert qemu.boot_time < 500, f"QEMU boot time was not as expected, boot_time: {qemu.boot_time}"

    finally:
        qemu.stop()
        assert subprocess.run(
            ["pgrep", "-f", "qemu-system-x86_64"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        ).returncode != 0, "QEMU process is still running after stop"


if __name__ == "__main__":
    test_qemu_controller()