import subprocess
import shutil
from pathlib import Path
from src.worker_node.core.qemu_controller import QemuController

def test_port(tmp_path: Path):
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