from pathlib import Path
from enum import Enum
from typing import Any, List, Optional

from ..models.vm_output import VMOutput

class QemuStatus(Enum):
    STARTED = 1
    STOPPED = 2
    RUNNING = 3

class QemuController:
    def __init__(self, img_path: Path, cpu_count: int = 1, memory_allocated: int = 0) -> None:
        self.img_path = img_path 
        self.cpu_coun = cpu_count
        self.memory_allocated = memory_allocated
        self.status = QemuStatus.STARTED

    def start(self):
        ...
    
    def stop(self):
        ...

    def reset(self) -> None:
        ...
    
    def run_command(self, command: List[str], timeout: int = 30) -> VMOutput:
        ...
    
    def get_status(self):
        ...

    def send_http_request_to_vm(self, method: str,
                                path: str,
                                port: int,
                                query_params: Optional[dict[str, Any]] = None,
                                body: Optional[dict[str, Any]] = None,
                                headers: Optional[dict[str, str]] = None) -> VMOutput:
        ...
    
    def delete(self):
        ...