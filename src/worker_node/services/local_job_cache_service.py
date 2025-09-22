from pathlib import Path
from typing import Any
import requests
import yaml

from pydantic import UUID4


from ..exceptions import AlreadyExists
from ..db.job_metadata import JobMetadataDatabase
from ..db.job_repository import JobRepositoryDatabase
from ..models.job_configuration import JobConfiguration
from ..models.job import Job
from ..config import CORE_API_URI

class JobNotFound(Exception):
    ...

class LocalJobCacheService:

    def __init__(self, cache_max_size: int) -> None:
        self.job_metadata_db = JobMetadataDatabase()
        self.job_repository_db = JobRepositoryDatabase()
        self.cache_size_usage: int = 0
        self.cache_max_size: int = cache_max_size

    def cache_job(self, job_id: UUID4):
        if self.is_job_cached(job_id):
            # raise AlreadyExists("Job already cached")
            print("Job already cached")
            return
        try:
            job = self.fetch_job_information(job_id)
            self.job_metadata_db.insert(job)
            self.job_repository_db.store_job_repo(job.job_id, job.repo_url)

            self.cache_size_usage = self.job_repository_db.get_size(job.job_id)
        except JobNotFound:
            raise 
        except Exception as e:
            raise RuntimeError(f"Failed to cache job: {e}")
    
    def is_job_cached(self, job_id: UUID4) -> bool:
        return self.job_metadata_db.exists(job_id) and self.job_repository_db.exists(job_id)
   
    def free_till_cache_below_max(self):
        while self.cache_size_usage > self.cache_max_size:
            job = self.job_metadata_db.pop_first_not_locked()
            size = self.job_repository_db.get_size(job.job_id)
            self.job_repository_db.delete(job.job_id)
            self.cache_size_usage -= size

    def lock_job(self, job_id: UUID4):
        self.job_metadata_db.lock_job(job_id)

    def unlock_job(self, job_id: UUID4):
        self.job_metadata_db.lock_job(job_id)
    
    def get_disk_usage(self) -> int:
        return self.cache_size_usage
    
    def fetch_job_information(self, job_id: UUID4) -> Job:
        try:
            response = requests.get(f"{CORE_API_URI}/job/get/{job_id}")
            print(f"\n\n\n{CORE_API_URI}/job/get/{job_id}")

            if response.status_code == 404:
                raise JobNotFound("Job does not exist") 
            
            job = Job(**response.json())
            return job

        except JobNotFound as e:
            raise 
        except requests.Timeout as e:
            raise RuntimeError(f"Request timed out while fetching job information: {e}")
        except requests.RequestException as e:
            raise RuntimeError(f"Fetching job information failed request failed: {e}")
        except Exception as e:
            raise RuntimeError(f"Fetching job information failed unexpected error occurrred: {e}")
    
    def get_job_configuration(self, job_id: UUID4) -> JobConfiguration:
        CROWD_CLOUD_CONFIG_FILE_NAME = "crowdcloud.yml"
        with self.job_repository_db.get_file(job_id, CROWD_CLOUD_CONFIG_FILE_NAME) as config_file:
            config_dict: dict[Any, Any] = yaml.safe_load(config_file)
            config = JobConfiguration(**config_dict)
            return config
    
    def create_file(self, job_id: UUID4, file_name: str, contents: Any = "") -> Path:
        with self.job_repository_db.get_file(job_id, file_name, "w") as input_file:
            input_file.write(contents)

            return self.job_repository_db.cache_path / str(job_id) / file_name
    
    def delete_file(self, job_id: UUID4, file_name: str):
        path = self.job_repository_db.delete_file(job_id, file_name)
        return path
