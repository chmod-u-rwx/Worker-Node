
import os
from pathlib import Path
import shutil
from uuid import UUID

from pydantic import HttpUrl
from git import Repo, GitCommandError

from ..config import LOCAL_JOB_REPOSITORY_CACHE_PATH


class JobRepositoryDatabase:

    def __init__(self, cache_max_size: int, cache_path: Path = LOCAL_JOB_REPOSITORY_CACHE_PATH) -> None:
        self.cache_max_size = cache_max_size
        self.cache_path = cache_path
        self.ensure_directory_exist(cache_path)

    def exists(self, job_id: UUID) -> bool:
        job_path = self.cache_path / str(job_id)
        if not job_path.exists():
            return False
        
        if not job_path.is_dir():
            raise NotADirectoryError(f"{job_path} exist but is not a directory\n This shouldnt happen unless its a major corruption")
        
        if not any(job_path.iterdir()):
            raise ValueError(f"{job_path} exist but has not contents\n This shouldnt happen unless its a major corruption")
        
        return True
    
    def store_job_repo(self, job_id: UUID, url: HttpUrl):
        job_path = self.cache_path / str(job_id)
        try:
            os.mkdir(job_path)
            self.ensure_directory_exist(job_path)
            Repo.clone_from(str(url), job_path)
        except GitCommandError as e:
            raise RuntimeError(f"Error while cloning job repo: {e}")
  
    def delete(self, job_id: UUID):
        if not self.exists(job_id):
            raise FileNotFoundError("Job files does not exist in local job cache")

        job_path = self.cache_path / str(job_id)
        shutil.rmtree(job_path)
    
    def ensure_directory_exist(self, cache_path: Path):
        if not cache_path.exists():
            cache_path.mkdir(parents=True, exist_ok=True)

        if not cache_path.is_dir():
            raise NotADirectoryError(f"{cache_path} exists but is not a directory")
