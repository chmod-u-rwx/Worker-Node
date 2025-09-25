from ...worker_node.core.job_executor import JobExecutor


job_executor: JobExecutor | None = None
def get_job_executor() -> JobExecutor:
	global job_executor
	if not job_executor:
		job_executor = JobExecutor()
	return job_executor