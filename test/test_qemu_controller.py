from pathlib import Path
import paramiko
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
        assert proc_check.returncode is not None, "QEMU process did not start at all"
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
        assert proc_check.returncode is not None, "QEMU process did not stop properly"
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

def test_qemu_command_error():
    cmd_error = QemuController(
        image_path,
        cpu_count,
        memory_allocated
    )
    try:
        cmd_error.img_path = Path("/home/dan/Projects/qemu-node/alpine-stndrd/alpine-standard-3.22.1-x86_64.iso")
        cmd_error.start()
        assert False, "Expected RuntimeError not raised for command error"
    except RuntimeError as e:
        assert "Failed to start QEMU process due to an error in the command" in str(e)


def test_qemu_boot_time():
    qemu = QemuController(
        image_path,
        cpu_count,
        memory_allocated
    )
    try:
        qemu.start()
        assert qemu.boot_time is not None, "Boot time should be recorded after starting QEMU"
        assert qemu.boot_time < 1000, "QEMU boot time exceeded expected threshold"
    finally:
        if qemu.status == QemuStatus.STARTED:
            qemu.stop()


def test_run_command_in_vm():
    qemu = QemuController(
        image_path,
        cpu_count,
        memory_allocated
    )

    test_file_path = Path("test/files_for_transfer/test_in_vm.py")
    path_in_vm = "/root/test_in_vm"
    try:
        qemu.start()
        assert qemu.status == QemuStatus.STARTED
        assert qemu.check_ssh_connection(), "SSH connection failed after starting QEMU"        
        assert test_file_path.exists(), "Test file for command execution does not exist"

        qemu.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        qemu.ssh.connect("localhost", port=2222, username="root", password="root")
        sftp = qemu.ssh.open_sftp()
        assert sftp.put(str(test_file_path), path_in_vm), "Failed to transfer test file to VM"
        sftp.close()

        assert qemu.run_command(path_in_vm, "stdout"), "Command execution in VM failed for stdout"
        print(qemu.run_command(path_in_vm, "stdout"))
        assert qemu.run_command(path_in_vm, "stderr"), "Command execution in VM failed for stderr"
        print(qemu.run_command(path_in_vm, "stderr"))


    finally:
        if qemu.status == QemuStatus.STARTED:
            qemu.ssh.close()
            qemu.stop()