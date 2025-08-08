from pathlib import Path
import time
from .qemu_controller import QemuController
from ..config import MAX_CPU_COUNT_ALLOCATED, MAX_MEMORY_ALLOCATED

class QemuPoolEmptyError(Exception):
    ...

class QemuCleaned(Exception):
    ...

class QemuPool:
    def __init__(self) -> None:
        self.locked = False
        self.warm_queue: list[QemuController] = []
        self.running_queue: list[QemuController] = []
        self.is_cleaned = False  

        self._warm_vms()
   
    def get_memory_usage(self) -> int:
        if self.is_cleaned:
            raise QemuCleaned()
        
        raise 
    
    def get_cpu_usage(self) -> int:
        if self.is_cleaned:
            raise QemuCleaned()
        
        raise 
    
    def acquire(self ) -> QemuController:
        if self.is_cleaned == True:
            raise QemuCleaned()

        if len(self.warm_queue) == 0:
            # improve this to try to create new vms
            raise QemuPoolEmptyError()
        
        self._lock()
        qemu = self.warm_queue.pop(0)
        self.running_queue.append(qemu)
        self._unlock()

        return qemu
    
    def release(self, qemu: QemuController) -> None:
        if self.is_cleaned:
            raise QemuCleaned()

        self._lock()

        qemu.reset()
        self.running_queue.remove(qemu)
        self.warm_queue.append(qemu)

        self._unlock()
    
    def cleanup(self) -> None:
        self.is_cleaned = True

        for qemu in self.running_queue:
            qemu.stop()
            qemu.delete()
       
        for qemu in self.warm_queue:
            qemu.delete()

        self.warm_queue.clear()
        self.running_queue.clear()
    
    def _lock(self, timeout: float = 3):
        
        delta_time: float = 0
        while self.locked:
            time.sleep(0.1)
            delta_time += 0.1
            if delta_time > timeout:
                raise Exception("Timeout error")
        
        self.locked = True
    
    def _unlock(self):
        if not self.locked:
            raise Exception("Unlocking while not locked")
        self.locked = False

    def _warm_vms(self):
        memory_per_machine = MAX_MEMORY_ALLOCATED // MAX_CPU_COUNT_ALLOCATED
        for _ in range(MAX_CPU_COUNT_ALLOCATED):
            path = Path("./test/path") # update this
            qemu = QemuController(path, 1, memory_per_machine)
            self.warm_queue.append(qemu)
     

qemu_pool = QemuPool()
