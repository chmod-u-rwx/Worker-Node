
from pathlib import Path
from unittest.mock import MagicMock, patch
from uuid import UUID, uuid4
from src.worker_node.core.qemu_pool import QemuPool, QemuPoolEmptyError, QemuCleaned
from src.worker_node.config import MAX_MEMORY_ALLOCATED, MAX_CPU_COUNT_ALLOCATED
from src.worker_node.core.qemu_controller import QemuStatus

import pytest

class MockQemu:
    def __init__(self, img_path: Path, cpu_count: int = 1, memory_allocated: int = 0, vm_id: UUID = uuid4()) -> None:
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
    
    def run_command(self):
        ...
    
    def get_status(self):
        ...
    
    def delete(self):
        ...
    
    def freeze(self):
        ...

    def resume(self):
        ...


@pytest.fixture(autouse=True, scope="module")
def patch_qemu_controller():
    with patch("src.worker_node.core.qemu_pool.QemuController", MockQemu) :
        yield

def test_qemu_creating_new_vm_at_startup():
    pool = QemuPool()

    assert len(pool.warm_queue) == MAX_CPU_COUNT_ALLOCATED, "Qemu pool did not create expected numbers of warm vms"
    expected_memory_allocated = (MAX_MEMORY_ALLOCATED // MAX_CPU_COUNT_ALLOCATED)
    drift = pool.warm_queue[0].memory_allocated - expected_memory_allocated 
    assert drift < 100, "Memory allocated was not the expected value"

def test_qemu_acquire_release():
    pool = QemuPool()
    pool._warm_vms() # type: ignore

    warm_count = len(pool.warm_queue)
    running_count = len(pool.running_queue)
    assert warm_count > 0

    qemu = pool.acquire()
    assert len(pool.warm_queue) == warm_count - 1
    assert len(pool.running_queue) == running_count + 1

    pool.release(qemu)
    assert len(pool.warm_queue) == warm_count 
    assert len(pool.running_queue) == running_count 

def test_qemu_pool_cleanup():
    pool = QemuPool()
    pool._warm_vms() # type: ignore

    warm_count = len(pool.warm_queue)
    running_count = len(pool.running_queue)
    assert warm_count > 0
    
    pool.cleanup()

    warm_count = len(pool.warm_queue)
    running_count = len(pool.running_queue)
    assert warm_count == 0
    assert running_count == 0

    with pytest.raises(QemuCleaned):
        pool.acquire()
    
    with pytest.raises(QemuCleaned):
        pool.get_cpu_usage()

def test_qemu_empty_warm_queue():
    pool = QemuPool()
    pool._warm_vms() # type: ignore

    with pytest.raises(QemuPoolEmptyError):
        while len(pool.warm_queue) >= 0:
            pool.acquire()

def test_qemu_pool_session():
    pool = QemuPool()
    pool._warm_vms() # type: ignore
    pool.acquire = MagicMock()
    pool.release = MagicMock()
    with pool.session() as qemu:
        print(qemu)
    
    pool.acquire.assert_called_once()
    pool.release.assert_called_once()    


