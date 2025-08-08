from dotenv import load_dotenv
import os

load_dotenv()
MAX_MEMORY_ALLOCATED = int(os.environ["MAX_MEMORY_ALLOCATED"]) 
MAX_CPU_COUNT_ALLOCATED = int(os.environ["MAX_CPU_COUNT_ALLOCATED"])
