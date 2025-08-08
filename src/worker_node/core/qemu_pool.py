from .qemu_controller import QemuController

class QemuPoolEmptyError(Exception):
    pass

class QemuPool:
    def __init__(self) -> None:
        self.warm_queue: list[QemuController] = []
        self.running_queue: list[QemuController] = []
    
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
    

qemu_pool = QemuPool()
