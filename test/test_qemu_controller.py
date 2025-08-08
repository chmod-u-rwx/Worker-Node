from pathlib import Path
from src.worker_node.core.qemu_controller import QemuController,QemuStatus

def test_qemu_controller():
    qemu = QemuController(Path("/home/dan/Projects/qemu-node/alpine-stndrd/new-alpine.qcow2"), cpu_count=2, memory_allocated=512)

    try:
        qemu.start()
        assert qemu.status == QemuStatus.RUNNING
        assert qemu.boot_time > 0
    finally:
        qemu.stop()
        assert qemu.status == QemuStatus.STOPPED
if __name__ == "__main__":
    test_qemu_controller()