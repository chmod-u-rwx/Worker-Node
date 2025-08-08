from src.worker_node.core.qemu_pool import QemuPool, QemuPoolEmptyError
from src.worker_node.config import MAX_MEMORY_ALLOCATED, MAX_CPU_COUNT_ALLOCATED

import pytest

def test_qemu_creating_new_vm_at_startup():
    pool = QemuPool()

    assert len(pool.warm_queue) == MAX_CPU_COUNT_ALLOCATED, "Qemu pool did not create expected numbers of warm vms"
    expected_memory_allocated = (MAX_MEMORY_ALLOCATED // MAX_CPU_COUNT_ALLOCATED)
    drift = pool.warm_queue[0].memory_allocated - expected_memory_allocated 
    assert drift < 100, "Memory allocated was not the expected value"

def test_qemu_acquire_release():
    pool = QemuPool()

    warm_count = len(pool.warm_queue)
    running_count = len(pool.running_queue)

    qemu = pool.acquire()
    assert len(pool.warm_queue) == warm_count - 1
    assert len(pool.running_queue) == running_count + 1

    pool.release(qemu)
    assert len(pool.warm_queue) == warm_count + 1
    assert len(pool.running_queue) == running_count - 1

def test_qemu_pool_cleanup():
    pool = QemuPool()

    warm_count = len(pool.warm_queue)
    running_count = len(pool.running_queue)
    assert warm_count > 0
    assert running_count > 0
    
    pool.cleanup()

    warm_count = len(pool.warm_queue)
    running_count = len(pool.running_queue)
    assert warm_count == 0
    assert running_count == 0

def test_qemu_empty_warm_queue():
    pool = QemuPool()

    with pytest.raises(QemuPoolEmptyError):
        while len(pool.warm_queue) >= 0:
            pool.acquire()

def test_qemu_acquire_after_cleanup():
    pool = QemuPool()

    pool.cleanup()

    with pytest.raises(QemuPoolEmptyError):
        pool.acquire()

