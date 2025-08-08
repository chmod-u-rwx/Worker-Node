from pathlib import Path
from worker_node.core.qemu_controller import QemuController

# tmp_path is a built in fixture by pytest that provides temproray path
# this path gets automatically cleaned up after running the test

def test_create_qcow2_img(tmp_path: Path) -> None:
	img_path = tmp_path / "test_disk.qcow2"

	QemuController.create_qcow2_img(img_path, 64)

	assert img_path.exists()


def