from typing import Any, Dict
from ..models.job_configuration import JobConfiguration
from .qemu_pool import QemuPool
from ..services.local_job_cache_service import LocalJobCacheService
from ..config import CACHE_SIZE_ALLOCATED
from ..models.payloads import JobRequestPayload, JobResponsePayload

class JobExecutor():
    def __init__(self) -> None:
        # self.qemu_pool._warm_vms() # type: ignore
        self.qemu_pool = QemuPool()
        self.local_job_cache = LocalJobCacheService(CACHE_SIZE_ALLOCATED)

    def run_job(self, request: JobRequestPayload):
        try:
            self.local_job_cache.cache_job(request.job_id)

            config = self.local_job_cache.get_job_configuration(request.job_id)

            run_command = self.build_run_command(config, request)
            
            with self.qemu_pool.session() as qemu:
                if config.input.type == "bin":
                    output = qemu.run_command(run_command)
                elif config.input.type == "file":
                    self.local_job_cache.create_file(request.job_id, config.input.path, request.model_dump(mode="json"))
                    output = qemu.run_command(run_command)
                elif config.input.type == "http":
                    qemu.run_command(run_command)
                    assert request.method
                    output = qemu.send_http_request_to_vm(request.method.value, request.path, config.input.port, request.params, request.body, request.headers)
                else:
                    raise Exception("Unsupported Type")
            
            status_code = self.parse_status_code(config.error_map, output.returncode)
            is_error = self.is_error(status_code)
            body = output.stderr if is_error else output.stdout
            meta: dict[Any, Any] = {"stdin": output.stdin, "runtime": output.runtime}

            response = JobResponsePayload(job_id=request.job_id, master_id=request.master_id, worker_id=request.worker_id, request_id=request.request_id, status_code=status_code, body=body, meta=meta)
            return response
        except Exception as e:
            response = JobResponsePayload(job_id=request.job_id, master_id=request.master_id, worker_id=request.worker_id, request_id=request.request_id, status_code=500, body=str(e))
            return response

    def parse_status_code(self, error_map: dict[Any, Any], return_code: int) -> int:
        return int(error_map.get(str(return_code), error_map.get("default", 500)))
    
    def is_error(self, return_code: int) -> bool:
        return 400 <= return_code <= 599

    def build_run_command(self, config: JobConfiguration, request: JobRequestPayload) -> list[str]:
        cmd: list[str] = []

        cmd.append(f"cd /mnt/jobcache/{request.job_id} &&")

        if config.input.type == "http":
            cmd.append("setsid")

        if config.input.type == "bin" and request.body:
            cmd.extend(["sh", "-c", "\"", f"echo \"{str(request.body)}\" |"])

        cmd.append(config.run.runtime.value)
        cmd.append(config.run.file)

        if config.run.args:
            for k, v in config.run.args.items():
                cmd.extend([k, str(v)])

        if config.input.type == "bin" and request.params is not None:
            args_string = self.parse_input_args(config.input.allowed_args, request.params)
            if args_string:
                cmd.extend(args_string.split(" "))

        if config.input.type == "http":
            cmd.extend([">", "/dev/null", "2>&1", "<", "/dev/null", "&"])

        if config.input.type == "bin" and request.body:
            cmd.extend("\"")

        return cmd

    def parse_input_args(self, allowed_args: list[str], input_args: Dict[str, Any]) -> str:
        args_string = ""

        for args in allowed_args:
            stripped_args = args.replace("-", "")

            if input_args.get(stripped_args):
                args_string += f"{args} {input_args.get(stripped_args)} "
        
        return args_string.strip()
            
