from .qemu_pool import qemu_pool
from ..services.local_job_cache_service import LocalJobCacheService
from ..config import CACHE_SIZE_ALLOCATED
from ..models.messages import JobRequestPayload

class JobExecutor():
    def __init__(self) -> None:
        self.qemu_pool = qemu_pool
        self.local_job_cache = LocalJobCacheService(CACHE_SIZE_ALLOCATED)

    def run_job(self, request: JobRequestPayload):
        self.local_job_cache.cache_job(JobRequestPayload.job_id)

        # create run command

        # run process

        # get output
    
    
