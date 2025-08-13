from typing import Any
import pytest
from uuid import uuid4
from datetime import datetime
from collections import OrderedDict

from src.worker_node.core.local_job_cache_service import JobMetadataStore, AlreadyExists, Job  # adjust import


@pytest.fixture
def store() -> JobMetadataStore:
    return JobMetadataStore()


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


def test_insert_and_exists(store: JobMetadataStore):
    job = job_factory()
    store.insert(job)
    assert store.exists(job.job_id) is True
    assert store.exists(uuid4()) is False


def test_insert_duplicate_raises(store: JobMetadataStore):
    job = job_factory()
    store.insert(job)
    with pytest.raises(AlreadyExists):
        store.insert(job)


def test_get_returns_job_and_none(store: JobMetadataStore):
    job = job_factory()
    store.insert(job)
    assert store.get(job.job_id) == job
    assert store.get(uuid4()) is None


def test_delete_first_removes_oldest(store: JobMetadataStore):
    job1 = job_factory(job_name="Job 1")
    job2 = job_factory(job_name="Job 2")
    store.insert(job1)
    store.insert(job2)

    store.delete_first()
    assert store.exists(job1.job_id) is False
    assert store.exists(job2.job_id) is True

    store.delete_first()
    assert store.exists(job2.job_id) is False


def test_delete_first_on_empty_store_does_nothing(store: JobMetadataStore):
    store.delete_first()
    assert store.jobs == OrderedDict()
