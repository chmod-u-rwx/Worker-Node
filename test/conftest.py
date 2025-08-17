from typing import Generator
import pytest
from pathlib import Path

@pytest.fixture
def test_img(tmp_path: Path) -> Generator[Path, None, None]:
	"""
	Returns a working qcow2 image file.
	"""
	test_img = tmp_path / "test_img.qcow2"
	yield test_img
	test_img.unlink(missing_ok=True)  # delete the file