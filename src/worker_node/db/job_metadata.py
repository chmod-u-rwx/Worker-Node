from typing import OrderedDict, Optional
from uuid import UUID

from ..models.job import Job
from ..exceptions import AlreadyExists


class JobMetadataDatabase:

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

