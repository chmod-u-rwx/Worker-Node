import shutil
import subprocess
import pytest
from unittest.mock import patch, MagicMock
from pathlib import Path
from src.worker_node.core.qemu_controller import QemuController

# tmp_path is a built in fixture by pytest that provides temproray path
# this path gets automatically cleaned up after running the test


def test_get_qemu_cmd_no_loadvm(tmp_path: Path):
	q_cont = QemuController(tmp_path, "macos", 2, 200)

	# For macos
	cmd = q_cont._get_qemu_cmd() # type: ignore
	expected = [
		"qemu-system-x86_64",
		"-machine", "accel=tcg",
		"-cpu", "max",
		"-smp", "2",
		"-m", "200M",
		"-hda", str(tmp_path),
		"-netdev", "user,id=net0,hostfwd=tcp::2222-:22",
		"-device", "virtio-net,netdev=net0",
		"-nographic"
	]
	
	assert cmd == expected

	# For linux
	q_cont = QemuController(tmp_path, cpu_count=2, memory_allocated=400, virtualization="linux")
	cmd = q_cont._get_qemu_cmd() # type: ignore
	expected = [
		"qemu-system-x86_64",
		"-machine", "accel=kvm:tcg,usb=off",
		"-cpu", "host",
		"-smp", "2",
		"-m", "400M",
		"-hda", str(tmp_path),
		"-netdev", "user,id=net0,hostfwd=tcp::2222-:22",
		"-device", "virtio-net,netdev=net0",
		"-nographic",
		"-enable-kvm"
	]
	
	assert cmd == expected


def test_get_qemu_cmd_loadvm(tmp_path: Path):
	q_cont = QemuController(tmp_path, "macos", 4, 400)

	# macos
	cmd = q_cont._get_qemu_cmd(loadvm=True) #type:ignore

	expected = [
		"qemu-system-x86_64",
		"-machine", "accel=tcg",
		"-cpu", "max",
		"-smp", "4",
		"-m", "400M",
		"-hda", str(tmp_path),
		"-netdev", "user,id=net0,hostfwd=tcp::2222-:22",
		"-device", "virtio-net,netdev=net0",
		"-nographic",
		"-loadvm", "base"
	]

	assert cmd == expected

	# linux
	q_cont = QemuController(tmp_path, "linux", 4, 400)
	expected = [
		"qemu-system-x86_64",
		"-machine", "accel=kvm:tcg,usb=off",
		"-cpu", "host",
		"-smp", "4",
		"-m", "400M",
		"-hda", str(tmp_path),
		"-netdev", "user,id=net0,hostfwd=tcp::2222-:22",
		"-device", "virtio-net,netdev=net0",
		"-nographic",
		"-enable-kvm",
		"-loadvm", "base"
	]

def test_get_qemu_cmd_invalid_virtualization(tmp_path: Path):
	with pytest.raises(ValueError) as err:
		q_cont = QemuController(tmp_path, "ms-dos", 4, 400) # type: ignore

	assert "Virtualization must be 'macos' or 'linux' only" in str(err)



def test_create_snapshot(tmp_path: Path):

	base_img = Path("/Users/luis/netes/x86/alpine-runner.qcow2")
	test_img = tmp_path / "test_img.qcow2"
	shutil.copy(base_img, test_img)
	
	qemu_cont = QemuController(test_img, "macos", 2, 500)

	qemu_cont.create_snapshot()

	qemu_img_output = subprocess.check_output(
		["qemu-img", "info", str(test_img)],
		text=True
	)

	assert "base" in qemu_img_output, f"'base' snapshot not found in {test_img} file"

@patch("os.path.exists")
@patch("os.remove")
@patch("subprocess.Popen")
def test_qemu_binary_not_found(mock_popen: MagicMock, mock_remove: MagicMock, mock_exists: MagicMock, test_img: Path):

	q_cont = QemuController(test_img, "macos", cpu_count=2, memory_allocated=400)

	# Simulating Qemu binary not found
	mock_exists.return_value = False
	mock_popen.side_effect = FileNotFoundError

	with pytest.raises(RuntimeError, match="Qemu binary not found. Not installed?"):
		q_cont.create_snapshot()

	mock_remove.assert_not_called()


@patch("os.path.exists")
@patch("os.remove")
@patch("subprocess.Popen")
def test_qemu_monitor_socket_not_ready(mock_popen: MagicMock, mock_remove: MagicMock, mock_exists: MagicMock, test_img: Path):
	mock_exists.return_value = True
	mock_remove.return_value = None
	q_cont = QemuController(test_img, "macos", 4, 400)

	# mock of qemu_proc in create_snapshot
	proc_mock = MagicMock()
	q_cont._wait_for_socket = lambda file_socket: False #type:ignore

	mock_popen.return_value = proc_mock

	proc_mock.communicate.return_value = ("", "some error")

	with pytest.raises(RuntimeError) as e:
		q_cont.create_snapshot()

	assert "Qemu monitor socket failed to start in time" in str(e)
	mock_remove.assert_called_once_with("/tmp/qemu.sock")
	proc_mock.wait.assert_called()


@patch("os.path.exists")
@patch("os.remove")
@patch("subprocess.Popen")
def test_socat_timeout_while_sending_savevm_cmd(mock_popen: MagicMock, mock_remove: MagicMock, mock_exists: MagicMock, test_img: Path):
	mock_exists.return_value = True
	q_cont = QemuController(test_img, "macos", 2, 200)

	# First Popen call
	proc_qemu_mock = MagicMock()
	q_cont._wait_for_socket = lambda file_socket: True #type:ignore

	# Second Popen call. Socat proc
	proc_socat_mock = MagicMock()
	proc_socat_mock.communicate.side_effect = subprocess.TimeoutExpired(cmd="socat", timeout=10)

	mock_popen.side_effect = [proc_qemu_mock, proc_socat_mock]

	with pytest.raises(RuntimeError) as e:
		q_cont.create_snapshot()

	assert "socat timed out while sending savevm command" in str(e)
	print(e)

	mock_remove.assert_called_once()