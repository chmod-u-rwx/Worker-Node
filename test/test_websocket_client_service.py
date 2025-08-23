import asyncio
import json
from datetime import datetime, timezone
from typing import Any, List
import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from uuid import uuid4, UUID
from websockets import InvalidURI
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
    def websocket_client_service(self, worker_id: UUID):
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
            assert service.max_reconnect_attempts == 3
            assert service.reconnect_delay == 5
            assert service.current_websocket_url is None
            assert service.reconnect_attempts == 0
    
    def test_init_with_custom_params(self, worker_id: UUID):
        """
        Test initialization with custom parameters
        """
        
        with patch("src.worker_node.config.CORE_API_URI", "ws://mocked-api:1234"):
            service = WebsocketClientService(
                worker_id=worker_id,
                max_reconnect_attempts=5,
                reconnect_delay=10
            )
            
            assert service.worker_id == str(worker_id)
            assert service.max_reconnect_attempts == 5
            assert service.reconnect_delay == 10
    
    @pytest.mark.asyncio
    async def test_discover_master_node_success(self, websocket_client_service: WebsocketClientService):
        """
        Test successful master node discovery
        """
        mock_response = MagicMock()
        mock_response.json.return_value = {"master_address": "192.168.1.100:8001"}
        mock_response.raise_for_status.return_value = None
        
        with patch('httpx.AsyncClient') as mock_client:
            mock_client.return_value.__aenter__.return_value.get = AsyncMock(return_value=mock_response)
            
            result = await websocket_client_service.discover_master_node()
            
            expected_url = f"ws://192.168.1.100:8001/ws/connect/{websocket_client_service.worker_id}"
            assert result == expected_url
    
    @pytest.mark.asyncio
    async def test_connect_success_with_provided_url(self, websocket_client_service: WebsocketClientService):
        """
        Test successful connection with provided websocket URL
        """
        
        mock_websocket = AsyncMock()
        async def mock_connect_function(*args, **kwargs): # type: ignore
            return mock_websocket
        
        websocket_url = "ws://localhost:8001/ws/connect/test"
        
        with patch('websockets.connect', side_effect=mock_connect_function) as mock_connect:
            await websocket_client_service.connect(websocket_url)
            
            mock_connect.assert_called_once_with(websocket_url)
            assert websocket_client_service.websocket == mock_websocket
            assert websocket_client_service.running is True
            assert websocket_client_service.current_websocket_url == websocket_url
            assert websocket_client_service.reconnect_attempts == 0
    
    @pytest.mark.asyncio
    async def test_connect_success_with_discovery(self, websocket_client_service: WebsocketClientService):
        """
        Test successful connection using master node discovery
        """
        
        mock_websocket = AsyncMock()
        async def mock_connect_function(*args, **kwargs): # type: ignore
            return mock_websocket
        
        discovered_url = f"ws://192.168.1.100:8001/ws/connect/{websocket_client_service.worker_id}"
        
        with patch.object(websocket_client_service, 'discover_master_node', return_value=discovered_url) as mock_discover, \
            patch('websockets.connect', side_effect=mock_connect_function) as mock_connect:
            
            await websocket_client_service.connect()
            
            mock_discover.assert_called_once()
            mock_connect.assert_called_once_with(discovered_url)
            assert websocket_client_service.websocket == mock_websocket
            assert websocket_client_service.running is True
            assert websocket_client_service.current_websocket_url == discovered_url
    
    @pytest.mark.asyncio
    async def test_connect_invalid_uri(self, websocket_client_service: WebsocketClientService):
        """
        Test connection with invalid URI
        """        
        
        websocket_url = "invalid://url"
        
        with patch('websockets.connect', side_effect=InvalidURI("invalid://url", "Invalid URI")):
            with pytest.raises(ConnectionError, match="Failed to connect after 3 attempts"):
                await websocket_client_service.connect(websocket_url)
    
    @pytest.mark.asyncio
    async def test_connect_retry_connection_closed(self, websocket_client_service: WebsocketClientService):
        """
        Test connection retries on ConnectionClosed and then discover new master node
        """
        
        websocket_url = "ws://localhost:8001/ws/connect/test"
        new_url = "ws://192.168.1.101:8001/ws/connect/test"
        mock_websocket = AsyncMock()
        
        attempts: List[Any] = []

        async def connect_side_effect(*args, **kwargs): # type: ignore
            if len(attempts) < 3:
                attempts.append(1)
                raise ConnectionClosed(None, None)
            return mock_websocket

        with patch("websockets.connect", side_effect=connect_side_effect) as mock_connect, \
            patch.object(websocket_client_service, "discover_master_node", return_value=new_url) as mock_discover:
            await websocket_client_service.connect(websocket_url)
            
            assert mock_connect.call_count == 4
            mock_discover.assert_called_once()
            assert websocket_client_service.websocket == mock_websocket
            assert websocket_client_service.running is True
            assert websocket_client_service.current_websocket_url == new_url
    
    @pytest.mark.asyncio
    async def test_connect_max_retries_exceeded(self, websocket_client_service: WebsocketClientService):
        """
        Test connection failure after max retries
        """
        
        websocket_url = "ws://localhost:8001/ws/connect/test"
        
        with patch('websockets.connect', side_effect=Exception("Connection error")), \
            patch('asyncio.sleep'):
            
            with pytest.raises(ConnectionError, match="Failed to connect after 3 attempts"):
                await websocket_client_service.connect(websocket_url)
    
    @pytest.mark.asyncio
    async def test_send_message_success(self, websocket_client_service: WebsocketClientService):
        """
        Test successful message sending
        """
        
        mock_websocket = AsyncMock()
        websocket_client_service.websocket = mock_websocket
        message = {"type": "heartbeat", "timestamp": "2024-01-01T00:00:00Z"}
        
        await websocket_client_service.send_message(message)
        
        mock_websocket.send.assert_called_once_with(json.dumps(message))
    
    @pytest.mark.asyncio
    async def test_send_message_not_connected(self, websocket_client_service: WebsocketClientService):
        """
        Test sending message when not connected
        """
        
        message = {"type": "heartbeat"}
        
        with pytest.raises(RuntimeError, match="Not connected to WebSocket server"):
            await websocket_client_service.send_message(message)

    @pytest.mark.asyncio
    async def test_send_message_connection_closed_with_retry(self, websocket_client_service: WebsocketClientService):
        """
        Test sending message when connection is closed with retry
        """
        
        mock_websocket = AsyncMock()
        new_websocket = AsyncMock()
        websocket_client_service.websocket = mock_websocket
        websocket_client_service.running = True
        message = {"type": "heartbeat"}
        
        mock_websocket.send.side_effect = ConnectionClosed(None, None)
        
        async def fake_reconnect():
            websocket_client_service.websocket = new_websocket
            return True
        
        with patch.object(websocket_client_service, 'reconnect', side_effect=fake_reconnect) as mock_reconnect:
            await websocket_client_service.send_message(message)
            
            mock_reconnect.assert_called_once()
            new_websocket.send.assert_called_once_with(json.dumps(message))
            
    @pytest.mark.asyncio
    async def test_send_message_connection_closed_no_retry(self, websocket_client_service: WebsocketClientService):
        """
        Test sending message when connection is closed without retry
        """
        
        mock_websocket = AsyncMock()
        mock_websocket.send.side_effect = ConnectionClosed(None, None)
        websocket_client_service.websocket = mock_websocket
        websocket_client_service.running = True
        message = {"type": "heartbeat"}
        
        with pytest.raises(ConnectionClosed):
            await websocket_client_service.send_message(message, retry_on_failure=False)
        
        assert websocket_client_service.running is False
    
    @pytest.mark.asyncio
    async def test_send_message_websocket_exception(self, websocket_client_service: WebsocketClientService):
        """
        Test sending message with WebSocket exception
        """
        mock_websocket = AsyncMock()
        mock_websocket.send.side_effect = WebSocketException("WebSocket error")
        websocket_client_service.websocket = mock_websocket
        
        message = {"type": "heartbeat"}
        
        with pytest.raises(WebSocketException):
            await websocket_client_service.send_message(message)
    
    @pytest.mark.asyncio
    async def test_disconnect_success(self, websocket_client_service: WebsocketClientService):
        """
        Test successful disconnection
        """
        
        mock_websocket = AsyncMock()
        websocket_client_service.websocket = mock_websocket
        websocket_client_service.running = True
        
        await websocket_client_service.disconnect()
        
        mock_websocket.close.assert_called_once()
        assert websocket_client_service.running is False
    
    @pytest.mark.asyncio
    async def test_disconnect_no_websocket(self, websocket_client_service: WebsocketClientService):
        """Test disconnection when no websocket is set"""
        websocket_client_service.running = True
        websocket_client_service.websocket = None
        
        with patch.object(websocket_client_service, 'websocket', None):
            await websocket_client_service.disconnect()
            
            assert websocket_client_service.websocket is None
            assert websocket_client_service.running is False
    
    @pytest.mark.asyncio
    async def test_disconnect_with_error(self, websocket_client_service: WebsocketClientService):
        """
        Test disconnection with error during close
        """
        
        mock_websocket = AsyncMock()
        mock_websocket.close.side_effect = Exception("Close error")
        websocket_client_service.websocket = mock_websocket
        websocket_client_service.running = True
        
        await websocket_client_service.disconnect()
        assert websocket_client_service.running is False

class TestWebsocketClientServiceReconnection:
    """
    Test reconnection functionality
    """
    
    @pytest.fixture
    def worker_id(self):
        return uuid4()
    
    @pytest.fixture
    def websocket_client_service(self, worker_id: UUID):
        with patch('src.worker_node.config.CORE_API_URI', 'http://localhost:8000'):
            return WebsocketClientService(worker_id)
    
    @pytest.mark.asyncio
    async def test_reconnect_success(self, websocket_client_service: WebsocketClientService):
        """
        Test successful reconnection
        """
        
        old_websocket = AsyncMock()
        new_websocket = AsyncMock()
        async def mock_connect(*args, **kwargs): # type: ignore
            return new_websocket
        
        websocket_client_service.websocket = old_websocket
        websocket_client_service.current_websocket_url = "ws://localhost:8001/ws/connect/test"
        websocket_client_service.reconnect_attempts = 0
        
        with patch('websockets.connect', side_effect=mock_connect):
            result = await websocket_client_service.reconnect()
            
            assert result is True
            old_websocket.close.assert_called_once()
            assert websocket_client_service.websocket == new_websocket
            assert websocket_client_service.running is True
            assert websocket_client_service.reconnect_attempts == 0
    
    @pytest.mark.asyncio
    async def test_reconnect_max_attempts_discovery(self, websocket_client_service: WebsocketClientService):
        """
        Test reconnection with max attempts exceeded, triggering discovery
        """
        
        websocket_client_service.websocket = AsyncMock()
        websocket_client_service.reconnect_attempts = 4
        new_url = "ws://192.168.1.101:8001/ws/connect/test"
        new_websocket = AsyncMock()
        
        async def mock_connect(*args, **kwargs): # type: ignore
            return new_websocket
        
        with patch.object(websocket_client_service, 'discover_master_node', return_value=new_url), \
            patch('websockets.connect', side_effect=mock_connect):
            
            result = await websocket_client_service.reconnect()
            
            assert result is True
            assert websocket_client_service.websocket == new_websocket
            assert websocket_client_service.running == True
    
    @pytest.mark.asyncio
    async def test_reconnect_failure(self, websocket_client_service: WebsocketClientService):
        """Test reconnection failure"""
        websocket_client_service.websocket = AsyncMock()
        websocket_client_service.current_websocket_url = "ws://localhost:8001/ws/connect/test"
        
        with patch('websockets.connect', side_effect=Exception("Connection failed")):
            result = await websocket_client_service.reconnect()
            
            assert result is False

class TestWebsocketClientServiceUtilities:
    """
    Test utility methods
    """
    
    @pytest.fixture
    def worker_id(self):
        return uuid4()
    
    @pytest.fixture
    def websocket_client_service(self, worker_id: UUID):
        with patch('src.worker_node.config.CORE_API_URI', 'http://localhost:8000'):
            return WebsocketClientService(worker_id)
    
    @pytest.mark.asyncio
    async def test_is_connected_true(self, websocket_client_service: WebsocketClientService):
        """
        Test is_connected when connected
        """
        
        mock_websocket = MagicMock()
        mock_websocket.close.return_value = False
        websocket_client_service.websocket = mock_websocket
        
        assert websocket_client_service.is_connected() is True
        
        
class TestWebsocketClientServiceIntegration:
    """
    Integration tests that test multiple methods together
    """
    
    @pytest.fixture
    def worker_id(self):
        return uuid4()
    
    @pytest.fixture
    def websocket_client_service(self, worker_id: UUID):
        with patch('src.worker_node.config.CORE_API_URI', 'http://localhost:8000'):
            return WebsocketClientService(worker_id)
    
    @pytest.mark.asyncio
    async def test_full_workflow_without_reconnection(self, websocket_client_service: WebsocketClientService):
        """
        Test the full workflow without reconnection complications
        Testing this first since I'm experiencing hung time
        """
        
        mock_websocket = AsyncMock()
        async def mock_websocket_connect(*args, **kwargs): # type: ignore
            return mock_websocket
        
        discovered_url = f"ws://192.168.1.100:8001/ws/connect/{websocket_client_service.worker_id}"
        
        now = datetime.now(timezone.utc)
        test_message = {"type": "heartbeat", "timestamp": str(now)}
        
        mock_response = MagicMock()
        mock_response.json.return_value = {"master_address": "192.168.1.100:8001"}
        mock_response.raise_for_status.return_value = None
        
        with patch('httpx.AsyncClient') as mock_client, \
            patch('websockets.connect', side_effect=mock_websocket_connect) as mock_connect:
            mock_client.return_value.__aenter__.return_value.get = AsyncMock(return_value=mock_response)
            
            # Test discovery and connection
            await websocket_client_service.connect()
            assert websocket_client_service.running is True
            assert websocket_client_service.websocket == mock_websocket
            mock_connect.assert_called_once_with(discovered_url)
            
            # Test sending message
            await websocket_client_service.send_message(test_message)
            mock_websocket.send.assert_called_once_with(json.dumps(test_message))
            
            # Test manual disconnection
            await websocket_client_service.disconnect()
            mock_websocket.close.assert_called_once()
            assert websocket_client_service.running is False
            
    @pytest.mark.asyncio
    async def test_full_workflow_success(self, websocket_client_service: WebsocketClientService):
        """
        Test the full workflow: discover -> connect -> send -> listen -> disconnect
        """
        
        mock_websocket = AsyncMock()
        async def mock_connect(*args, **kwargs): # type: ignore
            return mock_websocket
        
        discovered_url = f"ws://192.168.1.100:8001/ws/connect/{websocket_client_service.worker_id}"
        
        now = datetime.now(timezone.utc)
        test_message = {"type": "heartbeat", "timestamp": str(now)}
        received_message = {"type": "task", "data": "test_task"}
        
        mock_response = MagicMock()
        mock_response.json.return_value = {"master_address": "192.168.1.100:8001"}
        mock_response.raise_for_status.return_value = None

        mock_websocket.recv.side_effect = [
            json.dumps(received_message),
            ConnectionClosed(None, None),
        ]
        
        with patch('httpx.AsyncClient') as mock_client, \
            patch('websockets.connect', side_effect=mock_connect) as mock_connect_path, \
            patch.object(websocket_client_service, 'reconnect', return_value=False) as mock_reconnect:
            
            mock_client.return_value.__aenter__.return_value.get = AsyncMock(return_value=mock_response)
            
            await websocket_client_service.connect()
            assert websocket_client_service.running is True
            mock_connect_path.assert_called_once_with(discovered_url)
            
            await websocket_client_service.send_message(test_message)
            mock_websocket.send.assert_called_once_with(json.dumps(test_message))
            
            await websocket_client_service.listen_for_messages()
            assert mock_websocket.recv.call_count == 2
            assert mock_reconnect.call_count == 1
            assert websocket_client_service.running is False
    
    @pytest.mark.asyncio
    async def test_reconnection_workflow(self, websocket_client_service: WebsocketClientService):
        """
        Test the reconnection workflow during message listening
        """
        
        mock_websocket1 = AsyncMock()
        async def mock_connect(*args, **kwargs): # type: ignore
            return mock_websocket1
        
        mock_websocket2 = AsyncMock()
        websocket_url = "ws://localhost:8001/ws/connect/test"
        
        # First websocket fails, second succeeds
        mock_websocket1.recv.side_effect = ConnectionClosed(None, None)
        mock_websocket2.recv.side_effect = [
            json.dumps({"type": "test"}),
            ConnectionClosed(None, None)
        ]
        
        reconnect_calls = 0
        async def mock_reconnect():
            nonlocal reconnect_calls
            reconnect_calls += 1
            if reconnect_calls == 1:
                # First reconnect succeeds - switch to second websocket
                websocket_client_service.websocket = mock_websocket2
                websocket_client_service.running = True
                return True
            else:
                # Second reconnect fails - break the loop
                websocket_client_service.running = False
                return False
        
        with patch('websockets.connect', side_effect=mock_connect):
            # Initial connection
            await websocket_client_service.connect(websocket_url)
            assert websocket_client_service.websocket == mock_websocket1
            
            # Patch the reconnect method to control its behavior
            with patch.object(websocket_client_service, 'reconnect', side_effect=mock_reconnect):
                # Listen - should reconnect when websockets fail
                try:
                    await asyncio.wait_for(websocket_client_service.listen_for_messages(), timeout=2.0)
                except asyncio.TimeoutError:
                    pytest.fail("listen_for_messages() timed out - likely infinite loop")
                
                # Should have attempted to receive from both websockets
                mock_websocket1.recv.assert_called_once()
                mock_websocket2.recv.assert_called()
                assert reconnect_calls == 2
                assert websocket_client_service.running is False
    
    @pytest.mark.asyncio
    async def test_connect_send_disconnect_workflow(self, websocket_client_service: WebsocketClientService):
        """
        Test connect -> send -> disconnect workflow
        """
        
        mock_websocket = AsyncMock()
        async def mock_connect(*args, **kwargs): # type: ignore
            return mock_websocket
        
        websocket_url = "ws://localhost:8001/ws/connect/test"
        test_message = {"type": "status_update", "status": "ready"}
        
        with patch('websockets.connect', side_effect=mock_connect):
            await websocket_client_service.connect(websocket_url)
            assert websocket_client_service.running is True
            
            await websocket_client_service.send_message(test_message)
            mock_websocket.send.assert_called_once_with(json.dumps(test_message))
            
            await websocket_client_service.disconnect()
            mock_websocket.close.assert_called_once()
            assert websocket_client_service.running is False
    
    @pytest.mark.asyncio
    async def test_reconnection_success_then_failure(self, websocket_client_service: WebsocketClientService):
        """
        Test reconnection that succeeds once then fails
        """
        
        mock_websocket = AsyncMock()
        
        websocket_client_service.websocket = mock_websocket
        websocket_client_service.current_websocket_url = "ws://localhost:8001/ws/connect/test"
        websocket_client_service.running = True
        
        mock_websocket.recv.side_effect = ConnectionClosed(None, None)
        
        reconnect_calls = 0
        async def mock_reconnect():
            nonlocal reconnect_calls
            reconnect_calls += 1
            if reconnect_calls == 1:
                mock_websocket.recv.side_effect = [
                    json.dumps({"type": "reconnected"}),
                    ConnectionClosed(None, None)
                ]
                return True
            else:
                return False
        
        with patch.object(websocket_client_service, 'reconnect', side_effect=mock_reconnect):
            try:
                await asyncio.wait_for(websocket_client_service.listen_for_messages(), timeout=2.0)
            except asyncio.TimeoutError:
                pytest.fail("listen_for_messages() timed out")
            
            assert reconnect_calls == 2
            assert websocket_client_service.running is False