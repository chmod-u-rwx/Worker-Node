import pytest
import shutil
from pathlib import Path

@pytest.fixture
def test_img(tmp_path: Path) -> Path:
	"""
	Returns a working qcow2 image file.
	"""
	base_img = Path("/Users/luis/netes/x86/alpine-runner.qcow2")
	test_img = tmp_path / "test_img.qcow2"
	shutil.copy(base_img, test_img)

	return test_img