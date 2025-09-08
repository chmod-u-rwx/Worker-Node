from typing import Any, Dict
from ..models.job_configuration import JobConfiguration
from .qemu_pool import qemu_pool
from ..services.local_job_cache_service import LocalJobCacheService
from ..config import CACHE_SIZE_ALLOCATED
from ..models.messages import JobRequestPayload

class JobExecutor():
    def __init__(self) -> None:
        self.local_job_cache = LocalJobCacheService(CACHE_SIZE_ALLOCATED)

    def run_job(self, request: JobRequestPayload):
        self.local_job_cache.cache_job(request.job_id)

        config = self.local_job_cache.get_job_configuration(request.job_id)

        run_command = self.build_run_command(config, request)
        
        with qemu_pool.session() as qemu:
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
            
            qemu.reset()
    
        return output
    
    def build_run_command(self, config: JobConfiguration, request: JobRequestPayload) -> list[str]:
        run_command = ""

        if config.input.type == "http":
            run_command += "setsid "

        if config.input.type == "bin":
            run_command += f"echo \"{str(request.body)}\" | "

        run_command += f"{config.run.runtime.value} {config.run.file} "
        if config.run.args:
            args_string = " ".join([f"{k} {v}" for k,v in config.run.args.items()])
            run_command += args_string

        if config.input.type == "bin" and request.params is not None:
            args_string = self.parse_input_args(config.input.allowed_args, request.params)
            run_command += " " + args_string
        
        if config.input.type == "http":
            run_command += " > /dev/null 2>&1 < /dev/null &"

        return run_command.split(" ")

    def parse_input_args(self, allowed_args: list[str], input_args: Dict[str, Any]) -> str:
        args_string = ""

        for args in allowed_args:
            stripped_args = args.replace("-", "")

            if input_args.get(stripped_args):
                args_string += f"{args} {input_args.get(stripped_args)} "
        
        return args_string.strip()
            
