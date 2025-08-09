from pathlib import Path
from src.worker_node.core.qemu_controller import QemuController, QemuStatus
import subprocess

image_path = Path("/home/dan/Projects/qemu-node/alpine-stndrd/new-alpine.qcow2")
cpu_count = 2
memory_allocated = 512

def test_qemu_initialization():
    qemu = QemuController(
        image_path,
        cpu_count,
        memory_allocated
    )
    assert qemu.img_path == image_path
    assert qemu.cpu_count == cpu_count
    assert qemu.memory_allocated == memory_allocated
    assert qemu.status == QemuStatus.STOPPED

def test_qemu_start():
    qemu = QemuController(
        image_path,
        cpu_count,
        memory_allocated
    )
    try:
        qemu.start()
        assert qemu.status == QemuStatus.STARTED
        proc_check = subprocess.run(
            ["pgrep", "-f", "qemu-system-x86_64"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        assert proc_check.returncode == 0, "QEMU process did not start at all"
        assert qemu.check_ssh_connection(), "SSH connection failed after starting QEMU"
    finally:
        if qemu.status == QemuStatus.STARTED:
            qemu.stop()

def test_qemu_stop():
    qemu = QemuController(
        image_path,
        cpu_count,
        memory_allocated
    )
    try:
        qemu.start()
        assert qemu.status == QemuStatus.STARTED
        assert qemu.check_ssh_connection(), "SSH connection failed after starting QEMU"
    finally:
        qemu.stop()
        assert qemu.status == QemuStatus.STOPPED
        proc_check = subprocess.run(
            ["pgrep", "-f", "qemu-system-x86_64"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        assert proc_check.returncode != 0, "QEMU process did not stop properly"
        # Double check that stopping again raises an error
        try:
            qemu.stop()
            assert False, "Expected RuntimeError not raised when stopping already stopped QEMU"
        except RuntimeError as e:
            assert "No QEMU process to stop" in str(e) or isinstance(e, RuntimeError)

def test_qemu_missing_image():
    no_image = QemuController(
        Path("/non/existent/path.qcow2"),
        cpu_count,
        memory_allocated
    )
    try:
        no_image.start()
        assert False, "Expected RuntimeError not raised for missing image"
    except RuntimeError as e:
        assert "QEMU img not found" in str(e)

def test_qemu_boot_time():
    qemu = QemuController(
        image_path,
        cpu_count,
        memory_allocated
    )
    try:
        qemu.start()
        assert qemu.boot_time is not None, "Boot time should be recorded after starting QEMU"
        assert qemu.boot_time < 500, "QEMU boot time exceeded expected threshold"
    finally:
        if qemu.status == QemuStatus.STARTED:
            qemu.stop()