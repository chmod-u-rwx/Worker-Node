from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()
MAX_MEMORY_ALLOCATED = int(os.getenv("MAX_MEMORY_ALLOCATED", 0)) 
MAX_CPU_COUNT_ALLOCATED = int(os.getenv("MAX_CPU_COUNT_ALLOCATED", 0))

if MAX_MEMORY_ALLOCATED is 0 and MAX_CPU_COUNT_ALLOCATED is 0:
    raise ValueError(f"Resource allocated is invalid \n MAX_MEMORY_ALLOCATED = {MAX_MEMORY_ALLOCATED} \n MAX_CPU_COUNT_ALLOCATED = {MAX_CPU_COUNT_ALLOCATED}")

path_str = os.getenv("LOCAL_JOB_REPOSITORY_CACHE_PATH")
if path_str is None:
    raise ValueError(f"LOCAL_JOB_REPOSITORY_CACHE_PATH not set")

LOCAL_JOB_REPOSITORY_CACHE_PATH = Path(path_str)
CACHE_SIZE_ALLOCATED = int(os.getenv("CACHE_SIZE_ALLOCATED") or "0")
if CACHE_SIZE_ALLOCATED <= 0:
    raise ValueError("CACHE_SIZE_ALLOCATED cannot be zero or lower")

CORE_API_URI=os.getenv("CORE_API_URI")