from pathlib import Path
from dotenv import load_dotenv
from pathlib import Path
import os
import platform


load_dotenv()
MAX_MEMORY_ALLOCATED = int(os.getenv("MAX_MEMORY_ALLOCATED", 0)) 
MAX_CPU_COUNT_ALLOCATED = int(os.getenv("MAX_CPU_COUNT_ALLOCATED", 0))
BASE_IMG_FILE = str(os.environ["BASE_IMG_FILE"])
VIRTUALIZATION = platform.system().lower()

if VIRTUALIZATION not in ["darwin", "linux"]:
	raise ValueError(f"Unsupported OS: {VIRTUALIZATION}")

if MAX_MEMORY_ALLOCATED is 0 and MAX_CPU_COUNT_ALLOCATED is 0:
    raise ValueError(f"Resource allocated is invalid \n MAX_MEMORY_ALLOCATED = {MAX_MEMORY_ALLOCATED} \n MAX_CPU_COUNT_ALLOCATED = {MAX_CPU_COUNT_ALLOCATED}")

path_str = os.getenv("LOCAL_JOB_REPOSITORY_CACHE_PATH")
if path_str is None:
    raise ValueError(f"LOCAL_JOB_REPOSITORY_CACHE_PATH not set")

LOCAL_JOB_REPOSITORY_CACHE_PATH = Path(path_str)
CORE_API_URI=os.getenv("CORE_API_URI")
