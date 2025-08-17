from dotenv import load_dotenv
import os
import platform

load_dotenv()
MAX_MEMORY_ALLOCATED = int(os.environ["MAX_MEMORY_ALLOCATED"]) 
MAX_CPU_COUNT_ALLOCATED = int(os.environ["MAX_CPU_COUNT_ALLOCATED"])
BASE_IMG_FILE = str(os.environ["BASE_IMG_FILE"])
VIRTUALIZATION = platform.system().lower()

if VIRTUALIZATION not in ["darwin", "linux"]:
	raise ValueError(f"Unsupported OS: {VIRTUALIZATION}")