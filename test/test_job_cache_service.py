from pydantic import HttpUrl
import pytest
import requests
from unittest.mock import MagicMock, patch
from uuid import uuid4

from src.worker_node.services.local_job_cache_service import LocalJobCacheService, JobNotFound
from src.worker_node.exceptions import AlreadyExists
from src.worker_node.models.job import Job


@pytest.fixture
def sample_job():
    return Job(job_id=uuid4(),
               user_id=uuid4(),
               job_name="test_job",
               job_description="test description",
               repo_url=HttpUrl("https://github.com/example/repo.git"))


@pytest.fixture
def service():
    with patch("src.worker_node.services.local_job_cache_service.JobMetadataDatabase") as mock_metadata_db, \
         patch("src.worker_node.services.local_job_cache_service.JobRepositoryDatabase") as mock_repository_db:
        metadata_db = MagicMock()
        repo_db = MagicMock()
        mock_metadata_db.return_value = metadata_db
        mock_repository_db.return_value = repo_db
        mock_service = LocalJobCacheService(cache_max_size=1000)
        mock_service.job_metadata_db = metadata_db
        mock_service.job_repository_db = repo_db
        yield mock_service


def test_cache_job_success(service: LocalJobCacheService, sample_job: Job):
    with patch.object(service, "fetch_job_information", return_value=sample_job):
        assert isinstance(service.job_metadata_db, MagicMock)
        assert isinstance(service.job_repository_db, MagicMock)
        service.job_metadata_db.exists.return_value = False
        service.job_repository_db.exists.return_value = False
        service.job_repository_db.get_size.return_value = 50

        service.cache_job(sample_job.job_id)

        service.job_metadata_db.insert.assert_called_once_with(sample_job)
        service.job_repository_db.store_job_repo.assert_called_once_with(sample_job.job_id, sample_job.repo_url)
        assert service.cache_size_usage == 50


def test_cache_job_already_exists(service: LocalJobCacheService):
    assert isinstance(service.job_metadata_db, MagicMock)
    assert isinstance(service.job_repository_db, MagicMock)
    service.job_metadata_db.exists.return_value = True
    service.job_repository_db.exists.return_value = True

    with pytest.raises(AlreadyExists):
        service.cache_job(uuid4())


def test_cache_job_fetch_raises_job_not_found(service: LocalJobCacheService):
    with patch.object(service, "fetch_job_information", side_effect=JobNotFound()):
        assert isinstance(service.job_metadata_db, MagicMock)
        assert isinstance(service.job_repository_db, MagicMock)
        service.job_metadata_db.exists.return_value = False
        service.job_repository_db.exists.return_value = False
        with pytest.raises(JobNotFound):
            service.cache_job(uuid4())


def test_free_till_cache_below_max(service: LocalJobCacheService, sample_job: Job):
    assert isinstance(service.job_metadata_db, MagicMock)
    assert isinstance(service.job_repository_db, MagicMock)
    service.cache_size_usage = 200
    service.cache_max_size = 100
    service.job_metadata_db.pop_first_not_locked.return_value = sample_job
    service.job_repository_db.get_size.return_value = 50

    service.free_till_cache_below_max()

    service.job_repository_db.delete.assert_called_with(sample_job.job_id)
    assert service.cache_size_usage <= 100


def test_lock_unlock(service: LocalJobCacheService):
    assert isinstance(service.job_metadata_db, MagicMock)
    assert isinstance(service.job_repository_db, MagicMock)
    job_id = uuid4()
    service.lock_job(job_id)
    service.job_metadata_db.lock_job.assert_called_with(job_id)

    service.unlock_job(job_id)
    service.job_metadata_db.lock_job.assert_called_with(job_id)  


def test_get_disk_usage(service: LocalJobCacheService):
    service.cache_size_usage = 123
    assert service.get_disk_usage() == 123


@patch("src.worker_node.services.local_job_cache_service.requests.get")
def test_fetch_job_information_success(mock_get: MagicMock, service: LocalJobCacheService, sample_job: Job):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = sample_job.model_dump()

    job = service.fetch_job_information(sample_job.job_id)

    assert isinstance(job, Job)
    assert job.job_id == sample_job.job_id


@patch("src.worker_node.services.local_job_cache_service.requests.get")
def test_fetch_job_information_404(mock_get: MagicMock, service: LocalJobCacheService, sample_job: Job):
    mock_get.return_value.status_code = 404
    with pytest.raises(JobNotFound):
        service.fetch_job_information(sample_job.job_id)


@patch("src.worker_node.services.local_job_cache_service.requests.get", side_effect=requests.Timeout("Request timed out"))
def test_fetch_job_information_timeout(_, service: LocalJobCacheService, sample_job: Job):
    with pytest.raises(RuntimeError, match="timed out"):
        service.fetch_job_information(sample_job.job_id)


@patch("src.worker_node.services.local_job_cache_service.requests.get", side_effect=requests.RequestException("fail"))
def test_fetch_job_information_request_exception(_, service: LocalJobCacheService, sample_job: Job):
    with pytest.raises(RuntimeError, match="request failed"):
        service.fetch_job_information(sample_job.job_id)


@patch("src.worker_node.services.local_job_cache_service.requests.get", side_effect=ValueError("bad json"))
def test_fetch_job_information_unexpected(_, service: LocalJobCacheService, sample_job: Job):
    with pytest.raises(RuntimeError, match="unexpected error"):
        service.fetch_job_information(sample_job.job_id)



@pytest.mark.parametrize("config_path", [
    "./test/fixtures/bin_sample_config.yml",
    "./test/fixtures/file_sample_config.yml",
    "./test/fixtures/http_sample_config.yml",
])
@patch("src.worker_node.services.local_job_cache_service.JobRepositoryDatabase")
def test_get_job_configuration_success(repository: MagicMock, service: LocalJobCacheService, config_path: str):
    job_id = uuid4()

    config_file = open(config_path)
    service.job_repository_db.get_file.return_value.__enter__.return_value = config_file # type: ignore
    
    config = service.get_job_configuration(job_id)
    assert config

   