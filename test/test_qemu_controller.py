
import os
import time
import pytest
import subprocess
from pathlib import Path
from unittest.mock import patch, MagicMock
from src.worker_node.models.qemu_load import QemuLoad
from src.worker_node.core.qemu_controller import QemuController, QemuStatus

cpu_count = 2
memory_allocated = 500
virtualization = "macos"

def test_create_snapshot(test_img: Path):
    QemuController(test_img, virtualization, cpu_count, memory_allocated)
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
        QemuController(test_img, virtualization, cpu_count, memory_allocated)

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
        qemu = QemuController(test_img, virtualization, cpu_count, memory_allocated)
        qemu._wait_qemu_monitor_socket(proc_mock) # type: ignore

    assert "Qemu monitor socket failed to start in time" in str(e)
    os.remove(test_img)

@patch("subprocess.Popen")
def test_send_command_to_qemu_monitor(mock_popen: MagicMock):
    qemu = QemuController.__new__(QemuController) # gives an empty instance of QemuController that doesnt run __init__
    proc_mock = MagicMock() 
    proc_mock.communicate.return_value = ("Stdout is okayy", "No stderr")
    proc_mock.returncode = 0
    mock_popen.return_value = proc_mock
    stdout = qemu._send_command_to_qemu_monitor("/tmp/qemu.sock", "some random command", return_stdout=True) # type: ignore

    mock_popen.assert_called_once()
    assert stdout == "Stdout is okayy"

@patch("subprocess.Popen")
def test_send_command_to_qemu_monitor_socat_not_found(mock_popen: MagicMock, test_img: Path):
    qemu = QemuController.__new__(QemuController)
    mock_popen.side_effect = FileNotFoundError()

    with pytest.raises(RuntimeError, match="socat command not found. Is socat installed?"):
        qemu._send_command_to_qemu_monitor("/tmp/qemu.sock", "random command") # type: ignore

@patch("subprocess.Popen")
def test_send_command_to_qemu_monitor_failed_to_start_socat(mock_popen: MagicMock, test_img: Path):
    mock_popen.side_effect = OSError("Some os error")
    qemu = QemuController.__new__(QemuController)

    with pytest.raises(RuntimeError, match="Failed to start socat"):
        qemu._send_command_to_qemu_monitor("/tmp/qemu.sock", "random command") # type: ignore

@patch("subprocess.Popen")
def test_send_command_to_qemu_monitor_socat_timeout(mock_open: MagicMock, test_img: Path):
    proc_mock = MagicMock()
    proc_mock.communicate.side_effect = subprocess.TimeoutExpired("socat", 10)
    mock_open.return_value = proc_mock
    qemu = QemuController.__new__(QemuController)
    
    with pytest.raises(TimeoutError, match="socat timed out while sending command"):
        qemu._send_command_to_qemu_monitor("/tmp/qemu.sock", "random command") # type: ignore

@patch("subprocess.Popen")
def test_send_command_to_qemu_monitor_socat_exited_with_error(mock_open: MagicMock):
    proc_mock = MagicMock()
    mock_open.return_value = proc_mock
    qemu = QemuController.__new__(QemuController) 
    proc_mock.communicate.return_value = ("stdout", "Some error")

    with pytest.raises(RuntimeError, match="socat exited with error: Some error"):
        qemu._send_command_to_qemu_monitor("/tmp/qemu.sock", "random command") # type: ignore

# tmp_path is a built in fixture by pytest that provides temproray path
# this path gets automatically cleaned up after running the test
def test_get_qemu_cmd_invalid_virtualization(tmp_path: Path):
	with pytest.raises(ValueError) as err:
		qemu = QemuController(tmp_path, "ms-dos", 4, 400) # type: ignore

	assert "Virtualization must be 'macos' or 'linux' only" in str(err)

def test_qemu_initialization(test_img: Path):
    qemu = QemuController(
        test_img,
		virtualization,
        cpu_count,
        memory_allocated
    )
    assert qemu.img_path == test_img
    assert qemu.cpu_count == cpu_count
    assert qemu.memory_allocated == memory_allocated
    assert qemu.status == QemuStatus.STOPPED
    os.remove(test_img)

def test_qemu_start(test_img: Path):
    qemu = QemuController(test_img, virtualization, 2, 500)
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
        test_img,
		virtualization,
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
            virtualization,
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
		virtualization,
        cpu_count,
        memory_allocated
    )
    with pytest.raises(RuntimeError, match="Failed to start QEMU process due to an error in the command"):
        cmd_error.img_path = Path("/Users/luis/netes/alpine-standard-3.22.1-x86_64.iso")
        cmd_error.start()

def test_qemu_boot_time(test_img: Path):
    qemu = QemuController(
        test_img,
		virtualization,
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
    qemu = QemuController(test_img, virtualization, cpu_count, memory_allocated)
    qemu.start()
    qemu.freeze()
    assert "VM status: paused" in qemu._send_command_to_qemu_monitor(file_socket, "info status", return_stdout=True) # type: ignore

    time.sleep(2)
    result = subprocess.run(["ps", "-p", str(qemu.proc.pid), "-o", "%cpu="], capture_output=True, text=True)
    cpu_usage = result.stdout.strip()
    assert cpu_usage == "0.0"

    qemu.resume()
    assert "VM status: running" in qemu._send_command_to_qemu_monitor(file_socket, "info status", return_stdout=True) # type: ignore

    time.sleep(0.5)
    result = subprocess.run(["ps", "-p", str(qemu.proc.pid), "-o", "%cpu="], capture_output=True, text=True)
    cpu_usage = result.stdout.strip()
    assert cpu_usage != "0.0"

    qemu.stop()

def test_freeze_resume_failure_case(test_img: Path):
    qemu = QemuController(test_img, virtualization, cpu_count, memory_allocated)

    with pytest.raises(Exception, match="Qemu has not yet started"):
        qemu.freeze()

    with pytest.raises(Exception, match="Qemu has not yet started"):
        qemu.resume()

    qemu.start()
    qemu._send_command_to_qemu_monitor = MagicMock() # type: ignore
    qemu._send_command_to_qemu_monitor.side_effect = RuntimeError() # type: ignore
    
    with pytest.raises(RuntimeError, match="Failed to freeze vm"):
        qemu.freeze()

    with pytest.raises(RuntimeError, match="Failed to resume vm"):
        qemu.resume()

    qemu.stop()

@patch("subprocess.run")
def test_get_resource_load(mock_run: MagicMock):
    qemu = QemuController.__new__(QemuController)
    qemu.status = QemuStatus.STARTED
    qemu.proc = MagicMock()
    qemu.cpu_count = 4
    qemu.proc.pid = 44335         # %cpu memory pid
    mock_run.return_value.stdout = "54.2 30000 44335" 
    resource_load = qemu.get_resource_load()

    mock_run.assert_called_once_with(
        ["ps", "-p", "44335", "-o", "pcpu=,rss=,pid="],
        capture_output=True,
        text=True,
        check=True
    )

    assert isinstance(resource_load, QemuLoad)
    assert resource_load.cpu_usage == 54.2 / 4
    assert resource_load.memory_usage == 30000
    assert resource_load.pid == 44335


@patch("subprocess.run")
def test_get_resource_load_ps_not_found(mock_run: MagicMock):
    mock_run.side_effect = FileNotFoundError
    qemu = QemuController.__new__(QemuController)
    qemu.status = QemuStatus.STARTED
    qemu.proc = MagicMock()

    with pytest.raises(RuntimeError, match="ps command not found. Not installed?"):
        qemu.get_resource_load()

def test_get_resource_load_qemu_not_started():
    qemu = QemuController.__new__(QemuController)
    qemu.status = QemuStatus.STOPPED

    with pytest.raises(Exception, match="Qemu has not yet started"):
        qemu.get_resource_load()

@patch("subprocess.run")
def test_get_resource_load_error_occured(mock_run: MagicMock):
    mock_run.side_effect = subprocess.CalledProcessError(1, "ps", stderr="Some error")
    qemu = QemuController.__new__(QemuController)
    qemu.status = QemuStatus.STARTED
    qemu.proc = MagicMock()

    with pytest.raises(RuntimeError, match="ps failed: Some error"):
        qemu.get_resource_load()
