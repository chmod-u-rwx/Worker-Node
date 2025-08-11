from pathlib import Path
from typing import Optional, OrderedDict
from uuid import UUID

from pydantic import HttpUrl
from ..models.job import Job


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

    def exists(self, job_id: UUID):
        ...
    
    def store_job_repo(self, job_id: UUID, url: HttpUrl):
        ...
    
    def update_job_repo(self, job_id: UUID, url: HttpUrl):
        ...
   
    def delete(self, job_id: UUID):
        ...


class LocalJobCacheService:

    def fetch_job_information(self) -> Job:
        ...
    
    def fetch_job_repo(self, repo_url: HttpUrl) -> Path:
        ...
    
    def is_job_cached(self, job_id: UUID) -> bool:
        ...
    
    def get_disk_usage(self) -> int:
        ...
    



