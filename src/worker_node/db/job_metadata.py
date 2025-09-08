from copy import deepcopy
from typing import OrderedDict
from uuid import UUID

from ..models.job import Job
from ..exceptions import AlreadyExists


class JobMetadataDatabase:

    def __init__(self):
        self.jobs: OrderedDict[UUID, Job] = OrderedDict() 
        self.locks: dict[UUID, int] = dict()

    def insert(self, job: Job):
        if job.job_id in self.jobs:
            raise AlreadyExists("Job already exists")

        self.jobs[job.job_id] = job
        self.jobs.move_to_end(job.job_id)  
        self.locks[job.job_id] = 0

    def pop_first_not_locked(self) -> Job:
        if len(self.jobs) == 0:
            raise RuntimeError("No jobs stored")

        for job_id, job in self.jobs.items():
            if not self.is_locked(job_id): 
                job_copy = deepcopy(job)
                del self.jobs[job_id]
                return job_copy

        raise RuntimeError("All jobs are locked cannot delete") 

    def get(self, job_id: UUID) -> Job:
        if not self.exists(job_id):
            raise KeyError("Job metadata not found")
        
        return self.jobs[job_id]
    
    def lock_job(self, job_id: UUID):
        if not self.exists(job_id):
            raise KeyError("Job metadata not found")

        self.locks[job_id] += 1 

    def unlock_job(self, job_id: UUID):
        if not self.exists(job_id):
            raise KeyError("Job metadata not found")

        if self.locks[job_id] == 0:
            raise RuntimeError("Job already unlocked (0 Locks)")

        self.locks[job_id] -= 1 
    
    def is_locked(self, job_id: UUID):
        return self.locks[job_id] != 0
        
    def exists(self, job_id: UUID) -> bool:
        return job_id in self.jobs



