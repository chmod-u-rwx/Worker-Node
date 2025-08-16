import pytest
from unittest.mock import patch
from uuid import uuid4
from pathlib import Path
from git import GitCommandError
from pydantic import HttpUrl
from pathlib import Path

from src.worker_node.db.job_repository import JobRepositoryDatabase


@pytest.fixture
def job_repo_db(tmp_path: Path):
    # Use a temporary directory so we're not touching real files
    return JobRepositoryDatabase(cache_max_size=10, cache_path=tmp_path)


def test_exists_when_directory_with_files(job_repo_db: JobRepositoryDatabase):
    job_id = uuid4()

    with patch.object(Path, "exists", return_value=True), \
         patch.object(Path, "is_dir", return_value=True), \
         patch.object(Path, "iterdir", return_value=[Path("file.txt")]):
        assert job_repo_db.exists(job_id) is True


def test_exists_when_directory_missing(job_repo_db: JobRepositoryDatabase):
    job_id = uuid4()
    with patch.object(Path, "exists", return_value=False):
        assert job_repo_db.exists(job_id) is False


def test_exists_not_a_directory(job_repo_db: JobRepositoryDatabase):
    job_id = uuid4()
    with patch.object(Path, "exists", return_value=True), \
         patch.object(Path, "is_dir", return_value=False):
        with pytest.raises(NotADirectoryError):
            job_repo_db.exists(job_id)


def test_exists_empty_directory(job_repo_db: JobRepositoryDatabase):
    job_id = uuid4()
    with patch.object(Path, "exists", return_value=True), \
         patch.object(Path, "is_dir", return_value=True), \
         patch.object(Path, "iterdir", return_value=[]):
        with pytest.raises(ValueError):
            job_repo_db.exists(job_id)


def test_store_job_repo_success(job_repo_db: JobRepositoryDatabase):
    job_id = uuid4()
    url = HttpUrl("https://github.com/example/repo.git")

    with patch.object(job_repo_db, "ensure_directory_exist") as mock_ensure, \
         patch("src.worker_node.db.job_repository.Repo.clone_from") as mock_clone:
        job_repo_db.store_job_repo(job_id, url)
        mock_ensure.assert_called_once()
        mock_clone.assert_called_once_with(str(url), job_repo_db.cache_path / str(job_id))


def test_store_job_repo_git_error(job_repo_db: JobRepositoryDatabase):
    job_id = uuid4()
    url = HttpUrl("https://github.com/example/repo.git")

    with patch.object(job_repo_db, "ensure_directory_exist"), \
         patch("src.worker_node.db.job_repository.Repo.clone_from", side_effect=GitCommandError("clone", 1)):
        with pytest.raises(RuntimeError, match="Error while cloning job repo"):
            job_repo_db.store_job_repo(job_id, url)


def test_delete_success(job_repo_db: JobRepositoryDatabase):
    job_id = uuid4()

    with patch.object(job_repo_db, "exists", return_value=True), \
         patch("shutil.rmtree") as mock_rmtree:
        job_repo_db.delete(job_id)
        mock_rmtree.assert_called_once_with(job_repo_db.cache_path / str(job_id))


def test_delete_not_found(job_repo_db: JobRepositoryDatabase):
    job_id = uuid4()
    with patch.object(job_repo_db, "exists", return_value=False):
        with pytest.raises(FileNotFoundError):
            job_repo_db.delete(job_id)


def test_ensure_directory_exist_creates_dir(job_repo_db: JobRepositoryDatabase):
    path = job_repo_db.cache_path / "newdir"
    with patch.object(Path, "exists", return_value=False), \
         patch.object(Path, "mkdir") as mock_mkdir, \
         patch.object(Path, "is_dir", return_value=True):
        job_repo_db.ensure_directory_exist(path)
        mock_mkdir.assert_called_once()


def test_ensure_directory_exist_not_a_dir(job_repo_db: JobRepositoryDatabase):
    path = job_repo_db.cache_path / "file"
    with patch.object(Path, "exists", return_value=True), \
         patch.object(Path, "is_dir", return_value=False):
        with pytest.raises(NotADirectoryError):
            job_repo_db.ensure_directory_exist(path)

def test_store_and_delete_repo(job_repo_db: JobRepositoryDatabase):
    job_id = uuid4()
    url = HttpUrl(f"https://github.com/sarcasticadmin/empty-repo.git")
    
    job_repo_db.store_job_repo(job_id, url)
    assert job_repo_db.exists(job_id)

    job_repo_db.delete(job_id)
    assert not job_repo_db.exists(job_id)

def test_exists_with_corruption(job_repo_db: JobRepositoryDatabase):
    job_id = uuid4()
    bad_path = job_repo_db.cache_path / str(job_id)
    
    bad_path.write_text("not a dir")
    with pytest.raises(NotADirectoryError):
        job_repo_db.exists(job_id)
    
    # Empty dir
    bad_path.unlink()
    bad_path.mkdir()
    with pytest.raises(ValueError):
        job_repo_db.exists(job_id)
