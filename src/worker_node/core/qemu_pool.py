from pathlib import Path
from .qemu_controller import QemuController
from ..config import MAX_CPU_COUNT_ALLOCATED, MAX_MEMORY_ALLOCATED

class QemuPoolEmptyError(Exception):
    pass

class QemuPool:
    def __init__(self) -> None:
        self.warm_queue: list[QemuController] = []
        self.running_queue: list[QemuController] = []

        self._warm_vms()
   
    def get_memory_usage(self) -> int:
        ...
    
    def get_cpu_usage(self) -> int:
        ...
    
    def acquire(self ) -> QemuController:
        ...
    
    def release(self, qemu: QemuController) -> None:
        ...
    
    def cleanup(self) -> None:
        ...

    def _warm_vms(self):
        memory_per_machine = MAX_MEMORY_ALLOCATED // MAX_CPU_COUNT_ALLOCATED
        for _ in range(MAX_CPU_COUNT_ALLOCATED):
            path = Path("./test/path") # update this
            qemu = QemuController(path, 1, memory_per_machine)
            self.warm_queue.append(qemu)
     

qemu_pool = QemuPool()
