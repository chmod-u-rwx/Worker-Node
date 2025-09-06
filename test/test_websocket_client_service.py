import json
import httpx
import pytest
from unittest.mock import AsyncMock, Mock, patch
from uuid import uuid4, UUID
from websockets import ConnectionClosed, WebSocketException
from src.worker_node.models.master_node import MasterNode
from src.worker_node.services.websocket_client_service import (
    WebsocketClientService,
    MasterNodeNotFound,
    MasterNodeInvalidResponse,
    MasterNodeDiscoveryError,
)
from src.worker_node.models.payloads import JobRequestPayload, MessageType, MethodEnum, WebsocketMessage

@pytest.fixture
def worker_id():
    return uuid4()

@pytest.fixture
def websocket_service(worker_id: UUID):
    return WebsocketClientService(worker_id=worker_id, max_reconnect_attempts=3)

@pytest.fixture
def mock_websocket():
    websocket = AsyncMock()
    websocket.recv = AsyncMock()
    websocket.send = AsyncMock()
    websocket.close = AsyncMock()
    return websocket

@pytest.fixture
def sample_master_node_data():
    return MasterNode(
        master_id=uuid4(),
        master_address="192.168.1.100"
    ).model_dump()

class TestWebsocketClientService:
    
    def test_init_with_uuid_object(self):
        worker_id = uuid4()
        service = WebsocketClientService(worker_id=worker_id)
        assert service.worker_id == str(worker_id)
        assert service.websocket is None
        assert service.max_reconnect_attempts == 3
        assert service.current_websocket_url is None
    
    def test_init_with_custom_max_reconnect_attempts(self):
        worker_id = uuid4()
        service = WebsocketClientService(worker_id=worker_id, max_reconnect_attempts=5)
        assert service.max_reconnect_attempts == 5
    
    @pytest.mark.asyncio
    async def test_discover_master_node_success(
        self,
        websocket_service: WebsocketClientService,
        sample_master_node_data: MasterNode
    ): 
        with patch("httpx.AsyncClient") as mock_client_class:
            mock_client = AsyncMock()
            mock_client_class.return_value.__aenter__.return_value = mock_client
            
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = sample_master_node_data
            mock_response.raise_for_status.return_value = None
            mock_client.get.return_value = mock_response
            
            with patch('src.worker_node.models.master_node.MasterNode') as mock_master_node:
                mock_master_node.return_value.master_address = "192.168.1.100"
                
                result = await websocket_service.discover_master_node()
                expected_url = f"ws://192.168.1.100/ws/connect/{websocket_service.worker_id}"
                assert result == expected_url
    
    @pytest.mark.asyncio
    async def test_discover_master_node_404_error(
        self,
        websocket_service: WebsocketClientService
    ):
        with patch("httpx.AsyncClient") as mock_client_class:
            mock_client = AsyncMock()
            mock_client_class.return_value.__aenter__.return_value = mock_client
        
            mock_response = Mock()
            mock_response.status_code = 404
            mock_client.get.return_value = mock_response
            
            with pytest.raises(MasterNodeNotFound, match="Master node discovery endpoint returned 404 Not Found"):
                await websocket_service.discover_master_node()
    
    @pytest.mark.asyncio
    async def test_discover_master_node_http_request_error(
        self,
        websocket_service: WebsocketClientService
    ):
        with patch('httpx.AsyncClient') as mock_client_class:
            mock_client = AsyncMock()
            mock_client_class.return_value.__aenter__.return_value = mock_client
            mock_client.get.side_effect = httpx.RequestError("Network error")
            
            with pytest.raises(MasterNodeDiscoveryError, match="HTTP request failed"):
                await websocket_service.discover_master_node()
    
    @pytest.mark.asyncio
    async def test_discover_master_node_invalid_response_data(
        self,
        websocket_service: WebsocketClientService
    ):
        with patch("httpx.AsyncClient") as mock_client_class:
            mock_client = AsyncMock()
            mock_client_class.return_value.__aenter__.return_value = mock_client
            
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {"invalid": "data"}
            mock_response.raise_for_status.return_value = None
            mock_client.get.return_value = mock_response
            
            with patch('src.worker_node.models.master_node.MasterNode') as mock_master_node:
                mock_master_node.side_effect = ValueError("Missing required fields")
                
                with pytest.raises(MasterNodeInvalidResponse, match="Invalid master node data"):
                    await websocket_service.discover_master_node()

class TestConnect:
    
    @pytest.mark.asyncio
    async def test_connect_success_with_provided_url(
        self,
        websocket_service: WebsocketClientService,
        mock_websocket: AsyncMock
    ):
        async def mock_connect(*args, **kwargs): #type: ignore
            return mock_websocket
        
        websocket_url = "ws://192.168.1.100/ws/connect/test"
        
        with patch("websockets.connect", side_effect=mock_connect):
            await websocket_service.connect(max_reconnect_attempts=3, websocket_url=websocket_url)
            
            assert websocket_service.websocket == mock_websocket
            assert websocket_service.current_websocket_url == websocket_url
    
    @pytest.mark.asyncio
    async def test_connect_success_with_discovered_url(
        self,
        websocket_service: WebsocketClientService,
        mock_websocket: AsyncMock
    ):
        async def mock_connect(*args, **kwargs): #type: ignore
            return mock_websocket
        
        discovered_url = "ws//192.168.1.100/ws/connect/test"
        
        with patch("websockets.connect", side_effect=mock_connect):
            with patch.object(websocket_service, "discover_master_node", return_value=discovered_url) as mock_discover:
                await websocket_service.connect(max_reconnect_attempts=3)
                
                mock_discover.assert_called_once()
                assert websocket_service.current_websocket_url == discovered_url
    
    @pytest.mark.asyncio
    async def test_retry_on_connection_closed(
        self,
        websocket_service: WebsocketClientService,
        mock_websocket: AsyncMock
    ):
        websocket_url = "ws://192.168.1.101/ws/connect/test"
        
        call_count = {"count": 0}
        async def mock_connect(*args, **kwargs): #type: ignore
            if call_count["count"] == 0:
                call_count["count"] += 1
                raise ConnectionClosed(None, None)
            return mock_websocket
        
        with patch("websockets.connect", side_effect=mock_connect):
            
            await websocket_service.connect(max_reconnect_attempts=3, websocket_url=websocket_url)
            assert websocket_service.websocket == mock_websocket
    
    @pytest.mark.asyncio
    async def test_connect_rediscover_after_max_attempts(
        self,
        websocket_service: WebsocketClientService,
        mock_websocket: AsyncMock
    ):
        websocket_url = "ws://192.168.1.100/ws/connect/test"
        new_discovered_url = "ws://192.168.1.101/ws/connect/test"
        
        call_count = {"count": 0}
        async def mock_connect(url, *args, **kwargs): #type: ignore
            if call_count["count"] < 3:
                call_count["count"] += 1
                raise ConnectionClosed(None, None)
            
            assert url == new_discovered_url
            return mock_websocket

        with patch("websockets.connect", side_effect=mock_connect):
            with patch.object(websocket_service, "discover_master_node", return_value=new_discovered_url) as mock_discover:
                await websocket_service.connect(max_reconnect_attempts=3, websocket_url=websocket_url)
                
                assert call_count["count"] == 3
                mock_discover.assert_called_once()
                assert websocket_service.current_websocket_url == new_discovered_url
                assert websocket_service.websocket == mock_websocket
    
    @pytest.mark.asyncio
    async def test_connect_failure_after_all_attempts(
        self,
        websocket_service: WebsocketClientService,
    ):
        websocket_url = "ws://192.168.1.100/ws/connect/test"
        
        with patch("websockets.connect", side_effect = ConnectionClosed(None, None)):
            with patch.object(websocket_service, "discover_master_node", return_value=websocket_url):
                with pytest.raises(ConnectionError, match=f"Failed to connect after {websocket_service.max_reconnect_attempts} attempts"):
                    await websocket_service.connect(max_reconnect_attempts=3, websocket_url=websocket_url, max_rediscoveries=2)
    
    @pytest.mark.asyncio
    async def test_connect_unexpected_exception(
        self,
        websocket_service: WebsocketClientService
    ):
        websocket_url = "ws://localhost:8080/ws/connect/test"
        
        with patch('websockets.connect') as mock_connect:
            mock_connect.side_effect = ValueError("Unexpected error")
            
            with pytest.raises(ConnectionError, match=f"Failed to connect after {websocket_service.max_reconnect_attempts} attempts"):
                await websocket_service.connect(max_reconnect_attempts=3, websocket_url=websocket_url)

class TestListenForMessage:
    
    @pytest.mark.asyncio
    async def test_listen_for_message_not_connected(
        self,
        websocket_service: WebsocketClientService,
    ):
        with pytest.raises(RuntimeError, match="Not connected to WebSocket server"):
            await websocket_service.listen_for_messages()
    
    @pytest.mark.asyncio
    async def test_listen_for_message_json_message(
        self,
        websocket_service: WebsocketClientService,
        mock_websocket: AsyncMock,
    ):
        websocket_service.websocket = mock_websocket
        test_message = {"type": "test", "data": "hello"}
        
        mock_websocket.recv.side_effect = [
            json.dumps(test_message),
            ConnectionClosed(None, None)
        ]
        
        async def fake_disconnect():
            websocket_service.websocket = None
        
        with patch.object(websocket_service, "disconnect", side_effect=fake_disconnect) as mock_disconnect:
            with patch.object(websocket_service, "connect") as mock_connect:
                await websocket_service.listen_for_messages()
                
                mock_disconnect.assert_called()
                mock_connect.assert_called_once_with(websocket_service.max_reconnect_attempts)
    
    @pytest.mark.asyncio
    async def test_listen_for_job_rpc_message(
        self, 
        websocket_service: WebsocketClientService, 
        mock_websocket: AsyncMock, 
        monkeypatch: pytest.MonkeyPatch
    ):
        request_id = uuid4()
        job_request = JobRequestPayload(request_id=request_id, body={"body": "dummy"}, method=MethodEnum.GET)
        msg = WebsocketMessage(
        request_id=request_id,
        type=MessageType.JOB_REQUEST,
        payloads=job_request
        )

        websocket_service.websocket = mock_websocket
        mock_websocket.recv.side_effect = [
            json.dumps(msg.model_dump(mode="json")),
            ConnectionClosed(None, None)
        ]

        payload: JobRequestPayload | None = None
        async def mock_handle_job_rpc_request(request_payload: JobRequestPayload):
            nonlocal payload
            payload = request_payload

        async def fake_disconnect():
            websocket_service.websocket = None

        monkeypatch.setattr(websocket_service, "handle_job_rpc_request", mock_handle_job_rpc_request)
        monkeypatch.setattr(websocket_service, "disconnect", fake_disconnect)
        monkeypatch.setattr(websocket_service, "connect", AsyncMock())

        await websocket_service.listen_for_messages()

        assert payload is not None
        assert payload.request_id == request_id

    @pytest.mark.asyncio
    async def test_listen_for_message_websocket_exception(
        self,
        websocket_service: WebsocketClientService,
        mock_websocket: AsyncMock
    ):
        websocket_service.websocket = mock_websocket
        mock_websocket.recv.side_effect = WebSocketException("WebSocket error")
        
        async def fake_disconnect():
            websocket_service.websocket = None
        
        with patch.object(websocket_service, "disconnect", side_effect=fake_disconnect) as mock_disconnect:
            with patch.object(websocket_service, "connect") as mock_connect:
                await websocket_service.listen_for_messages()
                
                mock_disconnect.assert_called()
                mock_connect.assert_called_once_with(websocket_service.max_reconnect_attempts)

class TestSendMessage:
    """Test message sending functionality."""
    
    @pytest.mark.asyncio
    async def test_send_message_not_connected(
        self,
        websocket_service: WebsocketClientService,
    ):
        message = {"type": "test"}
        
        with pytest.raises(RuntimeError, match="Not connected to WebSocket server"):
            await websocket_service.send_message(message)
    
    @pytest.mark.asyncio
    async def test_send_message_connection_closed_retry(
        self,
        websocket_service: WebsocketClientService,
        mock_websocket: AsyncMock
    ):
        websocket_service.websocket = mock_websocket
        message = {"type": "test"}
        
        # First attempt fails with ConnectionClosed, second succeeds
        mock_websocket.send.side_effect = [ConnectionClosed(None, None), None]
        
        with patch.object(websocket_service, 'disconnect') as mock_disconnect:
            with patch.object(websocket_service, 'connect') as mock_connect:
                await websocket_service.send_message(message)
                
                mock_disconnect.assert_called_once()
                mock_connect.assert_called_once_with(websocket_service.max_reconnect_attempts)
                assert mock_websocket.send.call_count == 2
    
    @pytest.mark.asyncio
    async def test_send_message_websocket_exception_retry(
        self,
        websocket_service: WebsocketClientService,
        mock_websocket: AsyncMock
    ):
        websocket_service.websocket = mock_websocket
        message = {"type": "test"}
        
        mock_websocket.send.side_effect = [WebSocketException("Error"), None]
        
        with patch.object(websocket_service, 'disconnect') as mock_disconnect:
            with patch.object(websocket_service, 'connect') as mock_connect:
                await websocket_service.send_message(message)
                
                mock_disconnect.assert_called_once()
                mock_connect.assert_called_once_with(websocket_service.max_reconnect_attempts)
    
    @pytest.mark.asyncio
    async def test_send_message_max_attempts_exceeded(
        self,
        websocket_service: WebsocketClientService,
        mock_websocket: AsyncMock
    ):
        websocket_service.websocket = mock_websocket
        message = {"type": "test"}
        
        # Fail both attempts with unexpected exception
        mock_websocket.send.side_effect = ValueError("Unexpected error")
        
        with pytest.raises(ValueError):
            await websocket_service.send_message(message)
        
        assert mock_websocket.send.call_count == 2

class TestDisconnect:
    """Test disconnection functionality."""
    
    @pytest.mark.asyncio
    async def test_disconnect_when_connected(
        self,
        websocket_service: WebsocketClientService,
        mock_websocket: AsyncMock
    ):
        websocket_service.websocket = mock_websocket
        
        await websocket_service.disconnect()
        
        mock_websocket.close.assert_called_once()
        assert websocket_service.websocket is None
    
    @pytest.mark.asyncio
    async def test_disconnect_when_not_connected(
        self,
        websocket_service: WebsocketClientService,
    ):
        await websocket_service.disconnect()
        assert websocket_service.websocket is None

class TestIsConnected:
    """Test connection status checking."""
    
    def test_is_connected_true(
        self,
        websocket_service: WebsocketClientService,
        mock_websocket: AsyncMock
    ):
        websocket_service.websocket = mock_websocket
        assert websocket_service.is_connected() is True
    
    def test_is_connected_false(
        self,
        websocket_service: WebsocketClientService,
    ):
        assert websocket_service.is_connected() is False

class TestWebsocketClientIntegration:
    @pytest.mark.asyncio
    async def test_full_connection_flow(
        self,
        websocket_service: WebsocketClientService,
        mock_websocket: AsyncMock,
        sample_master_node_data: MasterNode
    ):
        """Test the complete flow: discover -> connect -> send -> listen -> disconnect."""
        
        async def mock_connect(*args, **kwargs): #type: ignore
            return mock_websocket
        
        with patch("httpx.AsyncClient") as mock_client_class:
            with patch("websockets.connect", side_effect=mock_connect):
                with patch("src.worker_node.models.master_node.MasterNode") as mock_master_node:
                    
                    mock_client = AsyncMock()
                    mock_client_class.return_value.__aenter__.return_value = mock_client
                    mock_response = Mock()
                    mock_response.status_code = 200
                    mock_response.json.return_value = sample_master_node_data
                    mock_response.raise_for_status.return_value = None
                    mock_client.get.return_value = mock_response
                    mock_master_node.return_value.master_addrese = "192.168.1.100"
                    
                    await websocket_service.connect(max_reconnect_attempts=3)
                    assert websocket_service.is_connected()
                    
                    test_message = {"type": "test"}
                    await websocket_service.send_message(test_message)
                    mock_websocket.send.assert_called_with(json.dumps(test_message))
                    
                    await websocket_service.disconnect()
                    assert not websocket_service.is_connected()
    
    @pytest.mark.asyncio
    async def test_error_handling_chain(
        self, 
        websocket_service: WebsocketClientService,
    ):
        """Test that errors in discovery propagate correctly."""
        
        with patch('httpx.AsyncClient') as mock_client_class:
            mock_client = AsyncMock()
            mock_client_class.return_value.__aenter__.return_value = mock_client
            mock_client.get.side_effect = httpx.RequestError("Network failure")
            
            with pytest.raises(MasterNodeDiscoveryError):
                await websocket_service.connect(max_reconnect_attempts=3)
            
            # Service should remain disconnected
            assert not websocket_service.is_connected()