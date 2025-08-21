import json
import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from uuid import uuid4, UUID
from websockets.exceptions import ConnectionClosed, WebSocketException
from src.worker_node.services.websocket_client_service import WebsocketClientService

class TestWebsocketClientService:
    
    @pytest.fixture
    def worker_id(self):
        return uuid4()
    
    @pytest.fixture
    def mock_env_vars(self):
        """
        Mock environment variables
        """
        
        with patch.dict('os.environ', {
            'CORE_API_URI': 'http://localhost:8000',
        }):
            yield
    
    @pytest.fixture
    def worker_service(self, worker_id: UUID):
        with patch('src.worker_node.config.CORE_API_URI', 'ws://localhost:8000'):
            return WebsocketClientService(worker_id)
    
    def test_init_success(self, worker_id: UUID):
        """
        Test successful initialization
        """

        with patch("src.worker_node.config.CORE_API_URI", "ws://mocked-api:1234"):

            service = WebsocketClientService(worker_id)

            assert service.worker_id == str(worker_id)
            assert service.websocket is None
            assert service.running is False
    
    @pytest.mark.asyncio
    async def test_discover_master_node_success(self, worker_service: WebsocketClientService):
        """
        Test successful master node discovery
        """
        mock_response = MagicMock()
        mock_response.json.return_value = {"master_address": "192.168.1.100:8001"}
        mock_response.raise_for_status.return_value = None
        
        with patch('httpx.AsyncClient') as mock_client:
            mock_client.return_value.__aenter__.return_value.get = AsyncMock(return_value=mock_response)
            
            result = await worker_service.discover_master_node()
            
            expected_url = f"ws://192.168.1.100:8001/ws/connect/{worker_service.worker_id}"
            assert result == expected_url
    
    @pytest.mark.asyncio
    async def test_connect_success_with_provided_url(self, worker_service: WebsocketClientService):
        """
        Test successful connection with provided websocket URL
        """
        
        mock_websocket = AsyncMock()
        async def mock_connect_function(*args, **kwargs): # type: ignore
            return mock_websocket
        
        websocket_url = "ws://localhost:8001/ws/connect/test"
        
        with patch('websockets.connect', side_effect=mock_connect_function) as mock_connect:
            await worker_service.connect(websocket_url)
            
            mock_connect.assert_called_once_with(websocket_url)
            assert worker_service.websocket == mock_websocket
            assert worker_service.running is True
    
    @pytest.mark.asyncio
    async def test_connect_success_with_discovery(self, worker_service: WebsocketClientService):
        """
        Test successful connection using master node discovery
        """
        
        mock_websocket = AsyncMock()
        async def mock_connect_function(*args, **kwargs): # type: ignore
            return mock_websocket
        
        discovered_url = f"ws://192.168.1.100:8001/ws/connect/{worker_service.worker_id}"
        
        with patch.object(worker_service, 'discover_master_node', return_value=discovered_url) as mock_discover, \
            patch('websockets.connect', side_effect=mock_connect_function) as mock_connect:
            
            await worker_service.connect()
            
            mock_discover.assert_called_once()
            mock_connect.assert_called_once_with(discovered_url)
            assert worker_service.websocket == mock_websocket
            assert worker_service.running is True
    
    @pytest.mark.asyncio
    async def test_send_message_success(self, worker_service: WebsocketClientService):
        """
        Test successful message sending
        """
        
        mock_websocket = AsyncMock()
        worker_service.websocket = mock_websocket
        message = {"type": "heartbeat", "timestamp": "2024-01-01T00:00:00Z"}
        
        await worker_service.send_message(message)
        
        mock_websocket.send.assert_called_once_with(json.dumps(message))
    
    @pytest.mark.asyncio
    async def test_send_message_not_connected(self, worker_service: WebsocketClientService):
        """
        Test sending message when not connected
        """
        
        message = {"type": "heartbeat"}
        
        with pytest.raises(RuntimeError, match="Not connected to WebSocket server"):
            await worker_service.send_message(message)
            
    @pytest.mark.asyncio
    async def test_send_message_connection_closed(self, worker_service: WebsocketClientService):
        """
        Test sending message when connection is closed
        """
        mock_websocket = AsyncMock()
        mock_websocket.send.side_effect = ConnectionClosed(None, None)
        worker_service.websocket = mock_websocket
        worker_service.running = True
        
        message = {"type": "heartbeat"}
        
        with patch.object(worker_service, 'disconnect', new_callable=AsyncMock) as mock_disconnect:
            with pytest.raises(ConnectionClosed):
                await worker_service.send_message(message)
            
            assert worker_service.running is False
            mock_disconnect.assert_called_once()
    
    @pytest.mark.asyncio
    async def test_send_message_websocket_exception(self, worker_service: WebsocketClientService):
        """
        Test sending message with WebSocket exception
        """
        mock_websocket = AsyncMock()
        mock_websocket.send.side_effect = WebSocketException("WebSocket error")
        worker_service.websocket = mock_websocket
        
        message = {"type": "heartbeat"}
        
        with pytest.raises(WebSocketException):
            await worker_service.send_message(message)
    
    @pytest.mark.asyncio
    async def test_disconnect_success(self, worker_service: WebsocketClientService):
        """
        Test successful disconnection
        """
        
        mock_websocket = AsyncMock()
        worker_service.websocket = mock_websocket
        worker_service.running = True
        
        await worker_service.disconnect()
        
        mock_websocket.close.assert_called_once()
        assert worker_service.running is False
    
    @pytest.mark.asyncio
    async def test_disconnect_no_websocket(self, worker_service: WebsocketClientService):
        """Test disconnection when no websocket is set"""
        worker_service.running = True
        worker_service.websocket = None
        
        with patch.object(worker_service, 'websocket', None):
            await worker_service.disconnect()
            
            assert worker_service.websocket is None
            assert worker_service.running is False
    
    @pytest.mark.asyncio
    async def test_disconnect_with_error(self, worker_service: WebsocketClientService):
        """Test disconnection with error during close"""
        mock_websocket = AsyncMock()
        mock_websocket.close.side_effect = Exception("Close error")
        worker_service.websocket = mock_websocket
        worker_service.running = True
        
        await worker_service.disconnect()
        assert worker_service.running is False
    
class TestWebsocketClientServiceIntegration:
    """
    Integration tests that test multiple methods together
    """
    
    @pytest.fixture
    def worker_id(self):
        return uuid4()
    
    @pytest.fixture
    def worker_service(self, worker_id: UUID):
        with patch('src.worker_node.config.CORE_API_URI', 'http://localhost:8000'):
            return WebsocketClientService(worker_id)
    
    @pytest.mark.asyncio
    async def test_full_workflow_success(self, worker_service: WebsocketClientService):
        """
        Test the full workflow: discover -> connect -> send -> listen -> disconnect
        """
        
        mock_websocket = AsyncMock()
        async def mock_connect_function(*args, **kwargs): # type: ignore
            return mock_websocket
        
        discovered_url = f"ws://192.168.1.100:8001/ws/connect/{worker_service.worker_id}"
        test_message = {"type": "heartbeat", "timestamp": "2024-01-01T00:00:00Z"}
        received_message = {"type": "task", "data": "test_task"}
        
        mock_response = MagicMock()
        mock_response.json.return_value = {"master_address": "192.168.1.100:8001"}
        mock_response.raise_for_status.return_value = None
        
        mock_websocket.recv.side_effect = [
            json.dumps(received_message),
            ConnectionClosed(None, None)
        ]
        
        with patch('httpx.AsyncClient') as mock_client, \
            patch('websockets.connect', side_effect=mock_connect_function) as mock_connect:
            
            mock_client.return_value.__aenter__.return_value.get = AsyncMock(return_value=mock_response)
            
            await worker_service.connect()
            assert worker_service.running is True
            mock_connect.assert_called_once_with(discovered_url)
            
            await worker_service.send_message(test_message)
            mock_websocket.send.assert_called_once_with(json.dumps(test_message))
            
            await worker_service.listen_for_messages()
            assert mock_websocket.recv.call_count == 2
            assert worker_service.running is False
    
    @pytest.mark.asyncio
    async def test_connect_send_disconnect_workflow(self, worker_service: WebsocketClientService):
        """
        Test connect -> send -> disconnect workflow
        """
        
        mock_websocket = AsyncMock()
        async def mock_connect_function(*args, **kwargs): # type: ignore
            return mock_websocket
        
        websocket_url = "ws://localhost:8001/ws/connect/test"
        test_message = {"type": "status_update", "status": "ready"}
        
        with patch('websockets.connect', side_effect=mock_connect_function):
            await worker_service.connect(websocket_url)
            assert worker_service.running is True
            
            await worker_service.send_message(test_message)
            mock_websocket.send.assert_called_once_with(json.dumps(test_message))
            
            await worker_service.disconnect()
            mock_websocket.close.assert_called_once()
            assert worker_service.running is False