
import os
from pathlib import Path
import shutil
from typing import IO, Any
from uuid import UUID

from pydantic import HttpUrl
from git import Repo, GitCommandError

from ..config import LOCAL_JOB_REPOSITORY_CACHE_PATH


class JobRepositoryDatabase:

    def __init__(self, cache_path: Path = LOCAL_JOB_REPOSITORY_CACHE_PATH) -> None:
        self.cache_path = cache_path
        self.ensure_directory_exist(cache_path)
    
    def get_size(self, job_id: UUID) -> int:
        job_path = self.cache_path / str(job_id)
        total = 0
        for root, _, files in os.walk(job_path, followlinks=False):
            for f in files:
                try:
                    total += os.path.getsize(os.path.join(root, f))
                except OSError:
                    continue
        return total // (1024 * 1024)

    def get_file(self, job_id: UUID, file_name: str, mode: str = "r") -> IO[Any]:
        job_root_path = self.get_job_root_path(job_id)
        file_path = job_root_path / file_name

        file = open(file_path, mode=mode)
        return file

    def delete_file(self, job_id: UUID, file_name: str):
        job_root_path = self.get_job_root_path(job_id)
        file_path = job_root_path / file_name

        os.remove(file_path)
        return file_path

    def exists(self, job_id: UUID) -> bool:
        job_root_path = self.get_job_root_path(job_id)
        if not job_root_path.exists():
            return False
        
        if not job_root_path.is_dir():
            raise NotADirectoryError(f"{job_root_path} exist but is not a directory\n This shouldnt happen unless its a major corruption")
        
        if not any(job_root_path.iterdir()):
            raise ValueError(f"{job_root_path} exist but has not contents\n This shouldnt happen unless its a major corruption")

        return True
    
    def store_job_repo(self, job_id: UUID, url: HttpUrl):
        job_root_path = self.get_job_root_path(job_id)
        try:
            os.mkdir(job_root_path)
            self.ensure_directory_exist(job_root_path)
            Repo.clone_from(str(url), job_root_path)
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
    
    def get_job_root_path(self, job_id: UUID):
        return self.cache_path / str(job_id)
    
