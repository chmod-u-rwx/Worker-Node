import subprocess
from pathlib import Path

class QemuController:

	@classmethod
	def create_qcow2_img(cls, path: Path, size_mb: int) -> None:
		""" 
		Creates a qcow2 disk file for installing alpine linux into.

		Args:
			img_name (str): name of the qcow2 file
			size (int): size of the disk file in Megabytes
		"""

		if size_mb < 50:
			raise ValueError("qcow2 size must atleast be 50 Mb")

		if path.exists() and path.is_dir():
			raise ValueError(f"Provided path '{path}' is a dir")

		if path.suffix != ".qcow2":
			path = path.with_suffix(".qcow2")


		try:
			subprocess.run(["qemu-img", "create", "-f", "qcow2", str(path), f"{size_mb}M"],
				   check=True)
			print(f"Successfully created {path} disk file")
			
		except subprocess.CalledProcessError as e:
			print("Failed to create qcow2 image. \n")
			print(f"Command output: \n{e}")
			raise
