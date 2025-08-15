
from uuid import UUID
from ..models.job import Job


class LocalJobCacheService:

    def cache_job(self) -> Job:
        ...
    
    def is_job_cached(self, job_id: UUID) -> bool:
        ...
    
    def get_disk_usage(self) -> int:
        ...
    



