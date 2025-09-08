from pathlib import Path
from typing import Any
from uuid import uuid4

import yaml
import pytest

from src.worker_node.core.job_executor import JobExecutor, JobConfiguration, JobRequestPayload
from src.worker_node.models.messages import MethodEnum


@pytest.fixture
def executor() -> JobExecutor:
    exec = JobExecutor()
    return exec

def get_config(path: Path | str):
    with open(path) as file:
        config_dict = yaml.safe_load(file)
        config = JobConfiguration(**config_dict)
    return config

    

@pytest.fixture
def sample_job_bin_configuration() -> JobConfiguration:
    config = get_config("./test/fixtures/bin_sample_config.yml")
    return config

@pytest.fixture
def sample_job_http_configuration() -> JobConfiguration:
    config = get_config("./test/fixtures/http_sample_config.yml")
    return config

@pytest.fixture
def sample_job_file_configuration() -> JobConfiguration:
    config = get_config("./test/fixtures/file_sample_config.yml")
    return config

@pytest.fixture
def sample_job_request() -> JobRequestPayload:
    request = JobRequestPayload(request_id=uuid4(),
                                job_id=uuid4(),
                                path="hello",
                                method=MethodEnum.GET, 
                                params={"qty": 2},
                                body="hello"
                                
                                )
    return request

@pytest.fixture
def job_configuration(request: Any):
    return request.getfixturevalue(request.param)

@pytest.mark.parametrize(
    "job_configuration, expected_output",
    [
        ("sample_job_bin_configuration", "echo \"hello\" | python main.py --sample args --qty 2"),
        ("sample_job_file_configuration", "python main.py --sample args"),
        ("sample_job_http_configuration", "setsid python main.py --sample args > /dev/null 2>&1 < /dev/null &"),
    ],
    indirect=["job_configuration"],  # tells pytest to resolve these as fixtures
)
def test_build_run_command_bin(job_configuration: JobConfiguration, expected_output: str, executor: JobExecutor,sample_job_request: JobRequestPayload):
    command = executor.build_run_command(job_configuration, sample_job_request)
    assert " ".join(command) == expected_output


def test_parse_args(executor: JobExecutor):
    allowed_args = ["--qty", "-v", "--isTrue"] 
    input_args: dict[Any, Any] = {
        "qty": 3,
        "v": "Hello",
        "isTrue": True
    }

    args_string = executor.parse_input_args(allowed_args, input_args)

    assert args_string == "--qty 3 -v Hello --isTrue True"

