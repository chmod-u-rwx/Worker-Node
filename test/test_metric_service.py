from typing import Any
from uuid import uuid4
import pytest
from unittest.mock import patch, MagicMock
from src.worker_node.models.node import Node, NodeStatus
from src.worker_node.services.metric_service import MetricService  # adjust import


@pytest.fixture
def service():
    return MetricService()


@pytest.fixture
def mock_post():
    with patch("src.worker_node.services.metric_service.requests.post") as mock:
        yield mock
    

@pytest.fixture
def sample_node():
    return Node(node_id=uuid4(), 
                status=NodeStatus.ACTIVE,  
                job_slots=2, 
                cpu_count_allocated=1, 
                cpu_percentage_allocated=10, 
                memory_allocated=1000, 
                cache_size_allocated=1000,
                cpu_usage=1, 
                memory_usage=100,
                cache_size_usage=100)




def make_response(status: int, json_data: Any, text: str):

    mock_resp = MagicMock()
    mock_resp.status_code = status
    mock_resp.json.return_value = json_data 
    mock_resp.text = text
    return mock_resp


def test_send_job_slots_success(service: MetricService, mock_post: MagicMock, sample_node: Node):
    sample_node.job_slots = 10
    mock_post.return_value = make_response(200, sample_node.model_dump(), "")
    node = service.send_job_slots(10)
    assert isinstance(node, Node)
    mock_post.assert_called_once()
    _, kwargs = mock_post.call_args
    assert kwargs["json"]["job_slots"] == 10


def test_send_resource_usage_success(service: MetricService, mock_post: MagicMock, sample_node: Node):
    sample_node.cpu_usage = 0.5
    sample_node.memory_usage = 1024
    sample_node.cache_size_usage = 128
    mock_post.return_value = make_response(200, sample_node.model_dump(), "")
    node = service.send_resource_usage(0.5, 1024, 128)
    assert isinstance(node, Node)
    data = mock_post.call_args[1]["json"]
    assert data["cpu_usage"] == 0.5
    assert data["memory_usage"] == 1024
    assert data["cache_size_usage"] == 128


def test_send_resource_allocation_success(service: MetricService, mock_post: MagicMock, sample_node: Node):
    sample_node.cpu_count_allocated = 4
    sample_node.cpu_percentage_allocated = 0.8
    sample_node.memory_allocated = 2048
    sample_node.cache_size_allocated = 256
    mock_post.return_value = make_response(200, sample_node.model_dump(), "")
    node = service.send_resource_allocation(4, 0.8, 2048, 256)
    assert isinstance(node, Node)
    data = mock_post.call_args[1]["json"]
    assert data["cpu_count_allocated"] == 4
    assert data["cpu_percentage_allocated"] == 0.8
    assert data["memory_allocated"] == 2048
    assert data["cache_size_allocated"] == 256


def test_update_worker_node_404(service: MetricService, mock_post: MagicMock, sample_node: Node):
    mock_post.return_value = make_response(status=404, json_data={},text="Not found")
    with pytest.raises(KeyError):
        service.send_job_slots(1)


def test_update_worker_node_invalid_input(service: MetricService, mock_post: MagicMock):
    for status in (409, 422):
        mock_post.return_value = make_response(status=status, json_data={}, text="Invalid input")
        with pytest.raises(ValueError):
            service.send_job_slots(1)


def test_update_worker_node_unexpected_error(service: MetricService, mock_post: MagicMock):
    mock_post.return_value = make_response(status=500, json_data={}, text="Internal Server Error")
    with pytest.raises(RuntimeError):
        service.send_job_slots(1)


def test_update_worker_node_request_exception(service: MetricService, mock_post: MagicMock):
    mock_post.side_effect = Exception("Connection failed")
    with pytest.raises(Exception):
        service.send_job_slots(1)
