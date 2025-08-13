import pytest
from pathlib import Path

@pytest.fixture
def test_img(tmp_path: Path) -> Path:
	"""
	Returns a working qcow2 image file.
	"""
	test_img = tmp_path / "test_img.qcow2"
	return test_img