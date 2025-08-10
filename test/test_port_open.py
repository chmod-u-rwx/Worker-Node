import subprocess
import shutil
from pathlib import Path
from src.worker_node.core.qemu_controller import QemuController
from src.worker_node.config import BASE_IMG_FILE

def test_port(tmp_path: Path):
	base_img = Path(BASE_IMG_FILE)
	test_img = tmp_path / "test_img.qcow2"
	shutil.copy(base_img, test_img)
	
	qemu_cont = QemuController(test_img, "linux", 2, 500)

	qemu_cont.create_snapshot()

	qemu_img_output = subprocess.check_output(
		["qemu-img", "info", str(test_img)],
		text=True
	)

	assert "base" in qemu_img_output, f"'base' snapshot not found in {test_img} file"