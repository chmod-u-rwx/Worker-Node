from pytest import fail
from pathlib import Path
from src.worker_node.core.qemu_controller import QemuController

# tmp_path is a built in fixture by pytest that provides temproray path
# this path gets automatically cleaned up after running the test

alpine_iso = Path("/Users/luis/netes/x86/alpine-virt-3.22.1-x86_64.iso")

def test_create_qcow2_img(tmp_path: Path):
	img_path = tmp_path / "test_disk.qcow2"
	qemu_controller = QemuController(img_path)

	qemu_controller.create_qcow2_img(img_path, 64)

	assert img_path.exists()


def test_get_qemu_cmd(tmp_path: Path):
	q_cont = QemuController(tmp_path)

	# For macos
	cmd = q_cont._get_qemu_cmd(alpine_iso=alpine_iso, virtualization="macos") # type: ignore
	expected = (
            "qemu-system-x86_64",
            "-machine accel=tcg,usb=off",
            "-cpu max",
            "-m 512M",
            f"-cdrom {alpine_iso}",
            f"-hda {tmp_path}",
            "-netdev user,id=net0,hostfwd=tcp::2222-:22",
            "-device virtio-net,netdev=net0",
            "-nographic"
        )
	
	assert cmd == " ".join(filter(None, expected))

	# For linux
	cmd = q_cont._get_qemu_cmd(alpine_iso=alpine_iso, virtualization="linux") # type: ignore
	expected = (
            "qemu-system-x86_64",
            "-machine accel=kvm:tcg,usb=off",
            "-cpu host",
            "-m 512M",
            f"-cdrom {alpine_iso}",
            f"-hda {tmp_path}",
            "-netdev user,id=net0,hostfwd=tcp::2222-:22",
            "-device virtio-net,netdev=net0",
            "-nographic",
			"-enable-kvm"
        )
	
	assert cmd == " ".join(filter(None, expected))

def test_setup_alpine(tmp_path: Path):
	img_path = tmp_path / "test_disk.qcow2"
	qemu_cont = QemuController(img_path)

	qemu_cont.create_qcow2_img(img_path, 4000)

	try:
		qemu_cont.setup_alpine_linux(alpine_iso, "macos")
	except Exception as e:
		fail(f"Setup_alpine_linux failed with exception: {e}") 
	