
from pathlib import Path


class QemuController:
    def __init__(self, img_path: Path, cpu_count: int = 1, memory_allocated: int = 0) -> None:
        self.img_path = img_path 
        self.cpu_coun = cpu_count
        self.memory_allocated = memory_allocated

    def start(self):
        ...
    
    def stop(self):
        ...

    def reset(self) -> None:
        ...
    
    def run_command(self):
        ...
    
    def get_status(self):
        ...