
import os
import time
import pytest
import subprocess
from pathlib import Path
from unittest.mock import patch, MagicMock
from src.worker_node.core.qemu_controller import QemuController, QemuStatus


def test_create_snapshot(test_img: Path):
    QemuController(test_img, "macos", 2, 500)
    qemu_img_output = subprocess.check_output(
        ["qemu-img", "info", str(test_img)],
        text=True
        )
    assert "base" in qemu_img_output, f"'base' snapshot not found in {test_img} file"
    os.remove(test_img)

# Unittest.mock.patch allows us to substute whats being patched to be
# a MagicMock object. This object acts like a fake object or function
@patch("os.path.exists")
@patch("subprocess.Popen")
def test_qemu_binary_not_found(mock_popen: MagicMock, mock_exists: MagicMock, test_img: Path):
    mock_exists.side_effect = [True, False]

    # makes subprocess.Popen induce a FileNotFoundError
    mock_popen.side_effect = FileNotFoundError

    with pytest.raises(RuntimeError, match="Qemu binary not found. Not installed?"):
        QemuController(test_img, "linux", cpu_count=2, memory_allocated=400)

    os.remove(test_img)


@patch("subprocess.Popen")
@patch("src.worker_node.core.qemu_controller.wait_for_file_socket_availability")
def test_create_snapshot_qemu_monitor_socket_not_ready(mock_wait_for_file_socket_availability: MagicMock, 
    mock_popen: MagicMock, test_img: Path):
    proc_mock = MagicMock()

    # We patch wait_for_file_socket_availability so we can change its
    # return value. This induces the RuntimeError
    mock_wait_for_file_socket_availability.return_value = False

    # makes so that subprocess.Popen returns the fake proc mock
    mock_popen.return_value = proc_mock

    proc_mock.communicate.return_value = ("", "some error")

    with pytest.raises(RuntimeError) as e:
        qemu = QemuController(test_img, "linux", 4, 400)
        qemu._wait_qemu_monitor_socket(proc_mock) # type: ignore

    assert "Qemu monitor socket failed to start in time" in str(e)
    os.remove(test_img)


@patch("os.path.exists")
@patch("subprocess.Popen")
def test_socat_timeout_while_sending_savevm_cmd(mock_popen: MagicMock, mock_exists: MagicMock, test_img: Path):
    mock_exists.return_value = True

    proc_socat_mock = MagicMock()
    proc_socat_mock.communicate.side_effect = subprocess.TimeoutExpired(cmd="socat", timeout=10)
    mock_popen.return_value = proc_socat_mock

    with patch.object(QemuController, "create_snapshot", return_value=None) as mock_create_snapshot:
        qemu = QemuController(test_img, "linux", 2, 200)

        with pytest.raises(TimeoutError) as e:
            qemu._save_vm()  # type: ignore

        assert "socat timed out while sending savevm command" in str(e.value)
        mock_create_snapshot.assert_called_once()
        mock_popen.assert_called_once()
        assert "socat" in " ".join(mock_popen.call_args[0][0])

    os.remove(test_img)

# tmp_path is a built in fixture by pytest that provides temproray path
# this path gets automatically cleaned up after running the test
def test_get_qemu_cmd_invalid_virtualization(tmp_path: Path):
	with pytest.raises(ValueError) as err:
		qemu = QemuController(tmp_path, "ms-dos", 4, 400) # type: ignore

	assert "Virtualization must be 'macos' or 'linux' only" in str(err)


cpu_count = 2
memory_allocated = 500

def test_qemu_initialization(test_img: Path):
    qemu = QemuController(
        test_img,
		"linux",
        cpu_count,
        memory_allocated
    )
    assert qemu.img_path == test_img
    assert qemu.cpu_count == cpu_count
    assert qemu.memory_allocated == memory_allocated
    assert qemu.status == QemuStatus.STOPPED
    os.remove(test_img)

def test_qemu_start(test_img: Path):
    qemu = QemuController(test_img, "macos", 2, 500)
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
        assert qemu.wait_for_ssh_connection(), "SSH connection failed after starting QEMU"
    finally:
        if qemu.status == QemuStatus.STARTED:
            qemu.stop()

def test_qemu_stop(test_img: Path):
    qemu = QemuController(
        Path("./alpine.qcow2"),
		"linux",
        cpu_count,
        memory_allocated
    )
    try:
        qemu.start()
        assert qemu.status == QemuStatus.STARTED
        assert qemu.wait_for_ssh_connection(), "SSH connection failed after starting QEMU"
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

def test_qemu_missing_image(test_img: Path):
    with patch.object(QemuController, "__init__", return_value=None):
        no_image = QemuController(
            Path(test_img),
            "linux",
            cpu_count,
            memory_allocated
        )

        with pytest.raises(RuntimeError, match="QEMU img not found"):
            no_image.img_path = Path("/non/existent/path")
            no_image.start()
            assert False, "Expected RuntimeError not raised for missing image"

def test_qemu_command_error(test_img: Path):
    cmd_error = QemuController(
        test_img,
		"linux",
        cpu_count,
        memory_allocated
    )
    with pytest.raises(RuntimeError, match="Failed to start QEMU process due to an error in the command"):
        cmd_error.img_path = Path("./alpine/alpine-standard-3.22.1-x86_64.iso")
        cmd_error.start()

def test_qemu_boot_time(test_img: Path):
    qemu = QemuController(
        test_img,
		"linux",
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


def test_freeze_resume_vm(test_img: Path):
    file_socket = "/tmp/qemu.sock"
    qemu = QemuController(test_img, "macos", cpu_count, memory_allocated)
    qemu.start()
    qemu._send_command_to_qemu_monitor(file_socket, "stop") # type: ignore
    assert "VM status: paused" in qemu._send_command_to_qemu_monitor(file_socket, "info status", return_stdout=True) # type: ignore

    time.sleep(2)
    result = subprocess.run(["ps", "-p", str(qemu.proc.pid), "-o", "%cpu="], capture_output=True, text=True)
    cpu_usage = result.stdout.strip()
    assert cpu_usage == "0.0"

    qemu._send_command_to_qemu_monitor(file_socket, "cont") # type: ignore
    assert "VM status: running" in qemu._send_command_to_qemu_monitor(file_socket, "info status", return_stdout=True) # type: ignore

    time.sleep(0.5)
    result = subprocess.run(["ps", "-p", str(qemu.proc.pid), "-o", "%cpu="], capture_output=True, text=True)
    cpu_usage = result.stdout.strip()
    assert cpu_usage != "0.0"
