from dotenv import load_dotenv
from pathlib import Path
import os
import platform


load_dotenv()
MAX_MEMORY_ALLOCATED = int(os.environ["MAX_MEMORY_ALLOCATED"]) 
MAX_CPU_COUNT_ALLOCATED = int(os.environ["MAX_CPU_COUNT_ALLOCATED"])
BASE_IMG_FILE = str(os.environ["BASE_IMG_FILE"])
VIRTUALIZATION = platform.system().lower()

if VIRTUALIZATION not in ["darwin", "linux"]:
	raise ValueError(f"Unsupported OS: {VIRTUALIZATION}")

path_str = os.getenv("LOCAL_JOB_REPOSITORY_CACHE_PATH")
if path_str is None:
    raise ValueError(f"LOCAL_JOB_REPOSITORY_CACHE_PATH not set")

LOCAL_JOB_REPOSITORY_CACHE_PATH = Path(path_str)