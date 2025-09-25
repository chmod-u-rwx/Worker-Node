import ast
from datetime import datetime
import time
import hashlib
from pathlib import Path
from typing import Any
from unittest.mock import MagicMock, patch
from uuid import uuid4, UUID

from pydantic import HttpUrl
import yaml
import pytest

from src.worker_node.models.job import Job
from src.worker_node.core.job_executor import JobExecutor, JobConfiguration, JobRequestPayload
from src.worker_node.models.payloads import MethodEnum

from src.worker_node_ui.providers.websocket_client_provider import get_websocket_client_service
from src.worker_node_ui.providers.heartbeat_timer_provider import get_heartbeat_timer
# import worker_ws_client_runner
import asyncio
from qasync import QEventLoop
from PySide6.QtWidgets import QApplication



@pytest.fixture
def executor() -> JobExecutor:
    with patch("src.worker_node.core.job_executor.QemuPool", new=MagicMock):
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

request = JobRequestPayload(
                            request_id=uuid4(),
                            master_id=uuid4(),
                            worker_id=uuid4(),
                            job_id=uuid4(), 
                            path="hello",
                            method=MethodEnum.GET, 
                            params={"qty": 2},
                            body="hello"
                            )

http_job_request = JobRequestPayload(
                            request_id=uuid4(),
                            master_id=uuid4(),
                            worker_id=uuid4(),
                            job_id=uuid4(), 
                            path="health",
                            method=MethodEnum.GET, 
                            body=None
                            )

@pytest.fixture
def sample_job_request() -> JobRequestPayload:
    return request

@pytest.fixture
def sample_http_job_request() -> JobRequestPayload:
    return http_job_request

@pytest.fixture
def job_configuration(request: Any):
    return request.getfixturevalue(request.param)

def test_run_job_success(executor: JobExecutor, sample_job_request: JobRequestPayload, sample_job_bin_configuration: JobConfiguration, sample_job_file_configuration: JobConfiguration, sample_job_http_configuration: JobConfiguration):
    executor.local_job_cache.cache_job = lambda job_id: None
    executor.local_job_cache.get_job_configuration = lambda job_id: sample_job_bin_configuration
    executor.run_job(sample_job_request)
    assert isinstance(executor.qemu_pool, MagicMock)
    executor.qemu_pool.session.assert_called_once()

@pytest.mark.parametrize(
    "job_configuration, expected_output",
    [
        ("sample_job_bin_configuration",
         f'cd /mnt/jobcache/{request.job_id} && sh -c " echo "hello" | python main.py --sample args --qty 2 "'),
        ("sample_job_file_configuration",
         f'cd /mnt/jobcache/{request.job_id} && python main.py --sample args'),
        ("sample_job_http_configuration",
         f'cd /mnt/jobcache/{request.job_id} && setsid python main.py --sample args > /dev/null 2>&1 < /dev/null &'),
    ],
    ids=[
        "bin_config",
        "file_config",
        "http_config",
    ],
    indirect=["job_configuration"],
)
def test_build_run_command_bin(job_configuration: JobConfiguration,
                               expected_output: str,
                               executor: JobExecutor,
                               sample_job_request: JobRequestPayload):
    command = executor.build_run_command(job_configuration, sample_job_request)
    assert expected_output == " ".join(command)

def test_parse_args(executor: JobExecutor):
    allowed_args = ["--qty", "-v", "--isTrue"] 
    input_args: dict[Any, Any] = {
        "qty": 3,
        "v": "Hello",
        "isTrue": True
    }

    args_string = executor.parse_input_args(allowed_args, input_args)

    assert args_string == "--qty 3 -v Hello --isTrue True"

def test_parse_args_ignore_not_allowed(executor: JobExecutor):
    allowed_args = ["--qty", "-v", "--isTrue"] 
    input_args: dict[Any, Any] = {
        "qty": 3,
        "v": "Hello",
        "isTrue": True,
        "ignore": "bad data"
    }

    args_string = executor.parse_input_args(allowed_args, input_args)

    assert args_string == "--qty 3 -v Hello --isTrue True"


@pytest.mark.parametrize("status_code, expected", [
    (1, 400),
    (2, 500),
    (999, 500), # Should be caught by default state
    (-1000, 500)
])
def test_parse_status_code(status_code: int, expected: int, executor: JobExecutor, sample_job_bin_configuration: JobConfiguration):
    error_map = sample_job_bin_configuration.error_map

    result = executor.parse_status_code(error_map, status_code)
    assert result == expected

def test_parse_status_code_no_default(executor: JobExecutor, sample_job_bin_configuration: JobConfiguration):
    error_map = sample_job_bin_configuration.error_map
    del error_map["default"]
    status_code = 100

    status_code = executor.parse_status_code(error_map, status_code)
    assert status_code  == 500 # should default to 500 even if no default mappint provided

@pytest.mark.integration
def test_run_job_integration(sample_job_request: JobRequestPayload):
    executor = JobExecutor()
    sample_job = Job(user_id=uuid4(),
                     job_id=sample_job_request.job_id,
                     job_name="hash_job",
                     job_description=" test",
                     repo_url=HttpUrl("https://github.com/chmod-u-rwx/Binary-Sample-Project.git"),
                     created_at=datetime.now(),
                     updated_at=datetime.now())

    executor.local_job_cache.fetch_job_information = lambda job_id: sample_job

    assert sample_job_request.params
    assert sample_job_request.params["qty"]
    assert sample_job_request.body

    assert sample_job_request.body
    assert sample_job_request.params
    result = sample_job_request.body + "\n"
    for _ in range(int(sample_job_request.params["qty"])):
        result = hashlib.sha256(result.encode()).hexdigest()

    expected: dict[Any, Any] =  {"input": sample_job_request.body + "\n", "result": result}

    output = executor.run_job(sample_job_request)

    assert expected == output



""" @pytest.mark.integration
def test_run_http_job_integration(sample_http_job_request: JobRequestPayload):
    executor = JobExecutor()
    sample_job = Job(user_id=uuid4(),
                     job_id=sample_http_job_request.job_id,
                     job_name="http_job",
                     job_description=" test",
                     repo_url=HttpUrl("https://github.com/chmod-u-rwx/Http-Sample-Project.git"),
                     created_at=datetime.now(),
                     updated_at=datetime.now())

    executor.local_job_cache.fetch_job_information = lambda job_id: sample_job

    t1 = time.time()
    output = executor.run_job(sample_http_job_request)
    t2 = time.time()

    f = t2 - t1

    assert output.status_code == 200
    assert output.body == "healthy"

    assert ast.literal_eval(output.body) == expected
 """

