import subprocess
import pytest
from unittest.mock import patch, MagicMock
from pathlib import Path
from src.worker_node.core.qemu_controller import QemuController

def test_create_snapshot(test_img: Path):

	qemu_cont = QemuController(test_img, "macos", 2, 500)

	qemu_cont.create_snapshot()

	qemu_img_output = subprocess.check_output(
		["qemu-img", "info", str(test_img)],
		text=True
	)

	assert "base" in qemu_img_output, f"'base' snapshot not found in {test_img} file"


# Unittest.mock.patch allows us to substute whats being patched to be
# a MagicMock object. This object acts like a fake object or function
@patch("os.path.exists")
@patch("subprocess.Popen")
def test_qemu_binary_not_found(mock_popen: MagicMock, mock_exists: MagicMock, test_img: Path):

	mock_exists.side_effect = [True, False]
	
	qemu = QemuController(test_img, "macos", cpu_count=2, memory_allocated=400)

	# makes subprocess.Popen induce a FileNotFoundError
	mock_popen.side_effect = FileNotFoundError

	with pytest.raises(RuntimeError, match="Qemu binary not found. Not installed?"):
		qemu.create_snapshot()


@patch("subprocess.Popen")
@patch("src.worker_node.core.qemu_controller.wait_for_file_socket_availability")
def test_create_snapshot_qemu_monitor_socket_not_ready(mock_wait_for_file_socket_availability: MagicMock, 
	mock_popen: MagicMock, test_img: Path):

	qemu = QemuController(test_img, "macos", 4, 400)

	proc_mock = MagicMock()

	# We patch wait_for_file_socket_availability so we can change its
	# return value. This induces the RuntimeError
	mock_wait_for_file_socket_availability.return_value = False

	# makes so that subprocess.Popen returns the fake proc mock
	mock_popen.return_value = proc_mock

	proc_mock.communicate.return_value = ("", "some error")

	with pytest.raises(RuntimeError) as e:
		qemu._wait_qemu_monitor_socket(proc_mock) # type: ignore

	assert "Qemu monitor socket failed to start in time" in str(e)


@patch("os.path.exists")
@patch("subprocess.Popen")
def test_socat_timeout_while_sending_savevm_cmd(mock_popen: MagicMock, mock_exists: MagicMock, test_img: Path):
	mock_exists.return_value = True
	qemu = QemuController(test_img, "macos", 2, 200)

	proc_socat_mock = MagicMock()
	proc_socat_mock.communicate.side_effect = subprocess.TimeoutExpired(cmd="socat", timeout=10)

	mock_popen.return_value = proc_socat_mock

	with pytest.raises(TimeoutError) as e:
		qemu._save_vm() # type: ignore

	assert "socat timed out while sending savevm command" in str(e)

# tmp_path is a built in fixture by pytest that provides temproray path
# this path gets automatically cleaned up after running the test

def test_get_qemu_cmd_invalid_virtualization(tmp_path: Path):
	with pytest.raises(ValueError) as err:
		qemu = QemuController(tmp_path, "ms-dos", 4, 400) # type: ignore

	assert "Virtualization must be 'macos' or 'linux' only" in str(err)