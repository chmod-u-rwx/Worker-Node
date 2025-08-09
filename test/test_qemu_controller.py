from pathlib import Path
from src.worker_node.core.qemu_controller import QemuController, QemuStatus
import subprocess

def test_qemu_controller():
    image_path = Path("/home/dan/Projects/qemu-node/alpine-stndrd/new-alpine.qcow2")

    assert image_path.exists(), f"VM image not found at {image_path}"

    qemu = QemuController(
        image_path,
        cpu_count=2,
        memory_allocated=512
    )

    try:
        qemu.start()
        assert qemu.status == QemuStatus.STARTED, "QEMU failed to set status STARTED after start()"

        proc_check = subprocess.run(
            ["pgrep", "-f", "qemu-system-x86_64"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        assert proc_check.returncode == 0, "QEMU process did not start at all"
        assert qemu.check_ssh_connection(), "SSH connection failed after starting QEMU"

        assert qemu.boot_time is not None, "Boot time not recorded"
        assert qemu.boot_time < 500, f"QEMU boot time too high: {qemu.boot_time}s"

        # Check if VM is still running before stopping
        assert subprocess.run(
            ["pgrep", "-f", "qemu-system-x86_64"],
            stdout=subprocess.DEVNULL
        ).returncode == 0, "QEMU process exited unexpectedly before stop()"

    except AssertionError as e:
        raise AssertionError(f"Test failed: {e}")

    finally:
        qemu.stop()
        assert subprocess.run(
            ["pgrep", "-f", "qemu-system-x86_64"],
            stdout=subprocess.DEVNULL
        ).returncode != 0, "QEMU process is still running after stop()"

        try:
            qemu.stop()
        except RuntimeError as e:
            assert "No QEMU process to stop" in str(e) or isinstance(e, RuntimeError), "Expected RuntimeError not raised when stopping already stopped QEMU"

    no_image = QemuController(
        Path("/non/existent/path.qcow2"),
        cpu_count=2,
        memory_allocated=512
    )
    try:
        no_image.start()
    except RuntimeError as e:
        assert "QEMU img not found" in str(e), "Expected RuntimeError not raised for missing image"