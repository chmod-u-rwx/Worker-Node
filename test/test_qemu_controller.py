
import os
import time
import pytest
import subprocess
from pathlib import Path
import paramiko
from unittest.mock import patch, MagicMock
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
    os.remove(test_img)

def test_start_already_started(test_img: Path):    
    qemu = QemuController(test_img, "linux", 2, 512)
    qemu.status = QemuStatus.STARTED

    with pytest.raises(RuntimeError, match="QEMU is already running"):
        qemu.start()
    os.remove(test_img)

def test_start_command_fails(test_img: Path):
    qemu = QemuController(test_img, "linux", 2, 512)

    with patch("subprocess.Popen") as mock_popen:
        process_mock = MagicMock()
        process_mock.poll.return_value = 1
        process_mock.returncode = 1
        mock_popen.return_value = process_mock

        with pytest.raises(RuntimeError, match="Failed to start QEMU process"):
            qemu.start()
    os.remove(test_img)

@patch("src.worker_node.core.qemu_controller.subprocess.Popen")
@patch("src.worker_node.core.qemu_controller.QemuController.create_snapshot", new=MagicMock())
def test_start_wait_for_ssh_connection_timeout(mock_popen: MagicMock, test_img: Path):
    fake_proc = MagicMock()
    fake_proc.poll.return_value = None
    fake_proc.returncode = 0
    mock_popen.return_value = fake_proc

    qemu = QemuController(test_img, "linux", 2, 512)
    qemu.ssh = MagicMock()
    qemu.ssh.connect.side_effect = paramiko.SSHException("Unable to connect")

    with pytest.raises(RuntimeError, match="SSH authentication failed"):
        qemu.start()
    os.remove(test_img)

@patch("src.worker_node.core.qemu_controller.QemuController.create_snapshot", new=MagicMock())
def test_qemu_stop(test_img: Path):
    with patch.object(QemuController, 'wait_for_ssh_connection', return_value=True), \
         patch("subprocess.Popen") as mock_popen:
        
        mock_proc = MagicMock()
        mock_proc.returncode = 0
        mock_proc.poll.return_value = None
        mock_popen.return_value = mock_proc

        qemu = QemuController(test_img, "linux", 2, 500)
        qemu.start()
        assert qemu.status == QemuStatus.STARTED

        qemu.stop()
        assert qemu.status == QemuStatus.STOPPED
        mock_proc.terminate.assert_called_once()

        mock_proc.poll.assert_called()
        os.remove(test_img)

def test_qemu_stop_before_start(test_img: Path):
    with patch.object(QemuController, "wait_for_ssh_connection", return_value=True):
        qemu = QemuController(test_img, "linux", 2, 500)
        with pytest.raises(RuntimeError, match="QEMU is not STARTED"):
            qemu.stop()

        qemu.status = QemuStatus.STARTED
        qemu.proc = MagicMock()

        qemu.stop()
        assert qemu.status == QemuStatus.STOPPED
        qemu.proc.terminate.assert_called_once()
        os.remove(test_img)

def test_wait_for_ssh_connection_success(test_img: Path):
    qemu = QemuController(test_img, "linux", 2, 512)
    qemu.ssh = MagicMock()

    qemu.ssh.connect.return_value = None

    assert qemu.wait_for_ssh_connection(timeout=1) is True
    qemu.ssh.connect.assert_called_once_with(
        "localhost", port=2222, username="root", password="root", timeout=1
    )
    os.remove(test_img)

def test_wait_for_ssh_connection_timeout(test_img: Path):
    qemu = QemuController(test_img, "linux", 2, 512)
    qemu.ssh = MagicMock()

    qemu.ssh.connect.side_effect = paramiko.SSHException("Unable to connect")

    with pytest.raises(TimeoutError, match="SSH authentication failed"):
        qemu.wait_for_ssh_connection(timeout=1)

def test_wait_for_ssh_connection_eventual_success(test_img: Path):
    qemu = QemuController(test_img, "linux", 2, 512)
    qemu.ssh = MagicMock()

    qemu.ssh.connect.side_effect = [paramiko.SSHException("Fail 1"), None]

    assert qemu.wait_for_ssh_connection(timeout=2) is True
    assert qemu.ssh.connect.call_count == 2


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

# ======================================================================== EDIT FILE PATH
def test_qemu_command_error(test_img: Path):
    cmd_error = QemuController(
        test_img,
		virtualization,
        cpu_count,
        memory_allocated
    )
    with pytest.raises(RuntimeError, match="Failed to start QEMU process due to an error in the command"):
        cmd_error.img_path = Path("/home/dan/Projects/qemu-node/alpine-stndrd/alpine-standard-3.22.1-x86_64.iso")
        cmd_error.start()
# ======================================================================== EDIT FILE PATH

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


def test_run_command_in_vm(test_img: Path):
    qemu = QemuController(test_img, "linux", 2, 500)

    test_file_path = Path("test/files_for_transfer/test_in_vm.py")
    path_in_vm = "/root/test_in_vm"
    try:
        qemu.start()
        assert qemu.status == QemuStatus.STARTED
        assert qemu.wait_for_ssh_connection(), "SSH connection failed after starting QEMU"        
        assert test_file_path.exists(), "Test file for command execution does not exist"

        qemu.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        qemu.ssh.connect("localhost", port=2222, username="root", password="root")
        sftp = qemu.ssh.open_sftp()
        assert sftp.put(str(test_file_path), path_in_vm), "Failed to transfer test file to VM"
        sftp.close()
        qemu.ssh.close()

        assert qemu.run_command(["test_in_vm", "stdout"]), "Command execution in VM failed for stdout"
        assert qemu.run_command(["test_in_vm", "stderr"]), "Command execution in VM failed for stderr"


    finally:
        if qemu.status == QemuStatus.STARTED:
            qemu.stop()
    os.remove(test_img)

def test_run_command_fails_ssh_connection(test_img: Path):
    qemu = QemuController(test_img, "linux", 2, 500)
    qemu.status = QemuStatus.STARTED

    with patch.object(qemu, "wait_for_ssh_connection", return_value=True), \
        patch.object(qemu.ssh, "connect", side_effect=paramiko.SSHException("Unable to connect")):
        with pytest.raises(TimeoutError, match="SSH error"):
            qemu.run_command(["ls", ""],timeout=1)
    
    os.remove(test_img)

def test_run_command_exec_times_out(test_img: Path):
    qemu = QemuController(test_img, "linux", 2, 500)
    qemu.status = QemuStatus.STARTED

    with patch.object(qemu.ssh, "connect", return_value=None), \
         patch.object(qemu.ssh, "exec_command", side_effect=Exception("Exec failed")):
        with pytest.raises(TimeoutError, match="Command execution timed out"):
            qemu.run_command(["ls", ""],timeout=1)
    
    os.remove(test_img)

def test_run_command_non_zero_return_code(test_img: Path):
    qemu = QemuController(test_img, "linux", 2, 500)
    qemu.status = QemuStatus.STARTED

    fake_stdout = MagicMock()
    fake_stdout.read.return_value = b"some error output"
    fake_stdout.channel.recv_exit_status.return_value = 1

    fake_stderr = MagicMock()
    fake_stderr.read.return_value = b"error details"

    with patch.object(qemu.ssh, "connect", return_value=None), \
         patch.object(qemu.ssh, "exec_command", return_value=(None, fake_stdout, fake_stderr)):
        output = qemu.run_command(["ls", ""])
        assert output.returncode == 1
        assert "some error output" in output.stdout
    
    os.remove(test_img)

def test_run_command_qemu_not_started(test_img: Path):
    qemu = QemuController(test_img, "linux", 2, 500)
    qemu.status = QemuStatus.STOPPED

    with pytest.raises(RuntimeError, match="QEMU is not STARTED. Cannot run command."):
        qemu.run_command(["ls", ""])
    
    os.remove(test_img)

def test_freeze_resume_vm(test_img: Path):
    file_socket = "/tmp/qemu.sock"
    qemu = QemuController(test_img, virtualization, cpu_count, memory_allocated)
    qemu.start()
    qemu.freeze()
    assert "VM status: paused" in qemu._send_command_to_qemu_monitor(file_socket, "info status", return_stdout=True) # type: ignore

    time.sleep(10)
    result = subprocess.run(["ps", "-p", str(qemu.proc.pid), "-o", "%cpu="], capture_output=True, text=True)
    cpu_usage = result.stdout.strip()
    assert cpu_usage == "0.0"

    qemu.resume()
    assert "VM status: running" in qemu._send_command_to_qemu_monitor(file_socket, "info status", return_stdout=True) # type: ignore

    time.sleep(0.5)
    result = subprocess.run(["ps", "-p", str(qemu.proc.pid), "-o", "%cpu="], capture_output=True, text=True)
    cpu_usage = result.stdout.strip()
    assert cpu_usage != "0.0"

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