import shutil

from pathlib import Path
from typing import Optional, OrderedDict
from uuid import UUID
from git import Repo, GitCommandError

from pydantic import HttpUrl
from ..models.job import Job
from ..config import LOCAL_JOB_REPOSITORY_CACHE_PATH


class AlreadyExists(Exception):
    ...

class SizeExceed(Exception):
    ...

class JobMetadataStore:

    def __init__(self):
        self.jobs: OrderedDict[UUID, Job] = OrderedDict() 

    def insert(self, job: Job):
        if job.job_id in self.jobs:
            raise AlreadyExists("Job already exists")

        self.jobs[job.job_id] = job
        self.jobs.move_to_end(job.job_id)  

    def exists(self, job_id: UUID) -> bool:
        return job_id in self.jobs

    def delete_first(self):
        if self.jobs:
            self.jobs.popitem(last=False)

    def get(self, job_id: UUID) -> Optional[Job]:
        return self.jobs.get(job_id)


class JobRepositoryStore:

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

class LocalJobCacheService:

    def cache_job(self) -> Job:
        ...
    
    def is_job_cached(self, job_id: UUID) -> bool:
        ...
    
    def get_disk_usage(self) -> int:
        ...
    



