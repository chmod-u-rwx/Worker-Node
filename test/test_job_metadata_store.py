from typing import Any
import pytest
from uuid import uuid4
from datetime import datetime

from src.worker_node.db.job_metadata import JobMetadataDatabase, AlreadyExists, Job  


@pytest.fixture
def store() -> JobMetadataDatabase:
    return JobMetadataDatabase()


def job_factory(**overrides: Any) -> Job:
    base: dict[Any, Any] = dict(
        user_id=uuid4(),
        job_id=uuid4(),
        job_name="Test Job",
        job_description="A test job description",
        repo_url="https://example.com/repo.git",
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
    base.update(overrides)
    return Job(**base)


def test_insert_and_exists(store: JobMetadataDatabase):
    job = job_factory()
    store.insert(job)
    assert store.exists(job.job_id) is True
    assert store.exists(uuid4()) is False


def test_insert_duplicate_raises(store: JobMetadataDatabase):
    job = job_factory()
    store.insert(job)
    with pytest.raises(AlreadyExists):
        store.insert(job)


def test_get_returns_job_and_raises_if_job_do_not_exist(store: JobMetadataDatabase):
    job = job_factory()
    store.insert(job)
    assert store.get(job.job_id) == job
    with pytest.raises(KeyError, match="Job metadata not found"):
        store.get(uuid4())


def test_delete_first_removes_oldest_unlocked(store: JobMetadataDatabase):
    job1 = job_factory(job_name="Job 1")
    job2 = job_factory(job_name="Job 2")
    store.insert(job1)
    store.insert(job2)

    store.lock_job(job1.job_id)

    store.pop_first_not_locked()
    assert store.exists(job1.job_id) is True
    assert store.exists(job2.job_id) is False

    store.unlock_job(job1.job_id)
    store.pop_first_not_locked()
    assert store.exists(job1.job_id) is False

def test_pop_first_runtime_exception_if_all_jobs_are_locked(store: JobMetadataDatabase):
    job1 = job_factory()
    store.insert(job1)
    store.lock_job(job1.job_id)

    with pytest.raises(RuntimeError, match="All jobs are locked cannot delete"):
        store.pop_first_not_locked()

def test_pop_first_runtime_exception_no_jobs(store: JobMetadataDatabase):
    with pytest.raises(RuntimeError, match="No jobs stored"):
        store.pop_first_not_locked()

def test_job_lock_unlock(store: JobMetadataDatabase):
    job = job_factory()

    store.insert(job)

    store.lock_job(job.job_id)
    store.lock_job(job.job_id)
    assert store.locks[job.job_id] == 2

    store.unlock_job(job.job_id)
    assert store.locks[job.job_id] == 1

    store.unlock_job(job.job_id) 
    assert store.locks[job.job_id] == 0

    with pytest.raises(RuntimeError, match="Job already unlocked"):
        store.unlock_job(job.job_id)
    
def test_job_lock_unlock_job_do_not_exiist(store: JobMetadataDatabase):
    with pytest.raises(KeyError, match="Job metadata not found"):
        store.lock_job(uuid4())
    with pytest.raises(KeyError, match="Job metadata not found"):
        store.lock_job(uuid4())
