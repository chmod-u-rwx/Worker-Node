import json
import httpx
from typing import Any, Dict, Optional
from uuid import UUID
import websockets
from websockets.exceptions import ConnectionClosed, WebSocketException
from src.worker_node.config import CORE_API_URI
from src.worker_node.models.master_node import MasterNode

class MasterNodeDiscoveryError(Exception):
    ...

class MasterNodeNotFound(MasterNodeDiscoveryError):
    ...

class MasterNodeServerError(MasterNodeDiscoveryError):
    ...

class MasterNodeInvalidResponse(MasterNodeDiscoveryError):
    ...

class WebsocketClientService:
    def __init__(self,
            worker_id: UUID,
            max_reconnect_attempts: int = 3,
        ):
        self.worker_id = str(worker_id)
        self.websocket = None
        self.max_reconnect_attempts = max_reconnect_attempts
        self.current_websocket_url = None
    
    async def connect(
        self,
        max_reconnect_attempts: int,
        max_rediscoveries: int = 2,
        websocket_url: Optional[str] = None
    ) -> None:
        if not websocket_url:
            websocket_url = await self.discover_master_node()
        
        current_address = websocket_url
        rediscoveries = 0
        
        while rediscoveries <= max_rediscoveries:
            for attempt in range(1, self.max_reconnect_attempts + 1):
                try:
                    self.websocket = await websockets.connect(current_address)
                    self.current_websocket_url = current_address
                    return

                except ConnectionClosed:
                    if attempt == self.max_reconnect_attempts:
                        new_address = await self.discover_master_node()
                    
                        if new_address != current_address:
                            current_address = new_address
                            break # Break inner loop to restart with new address
                        else:
                            break # Break inner loop, rediscoveries will increment
                        
                except Exception as e:
                    print(f"Unexpected error during WebSocket connection (attempt {attempt}): {e}")
            
            rediscoveries += 1

        raise ConnectionError(f"Failed to connect after {max_reconnect_attempts} attempts")
    
    async def listen_for_messages(self) -> None:
        if not self.websocket:
            raise RuntimeError("Not connected to WebSocket server")
        
        while self.websocket:
            message: str | bytes = ""
            try:
                message = await self.websocket.recv()
                
                data = json.loads(message)
                print(f"Received JSON message: {data}")
            except (ConnectionClosed, WebSocketException):
                await self.disconnect()
                await self.connect(self.max_reconnect_attempts)
            except json.JSONDecodeError:
                print(f"Received non-JSON message: {message}")
            except Exception:
                await self.disconnect()
                raise
            
        await self.disconnect()
    
    async def send_message(self, message: Dict[str, Any]) -> None:
        if not self.websocket:
            raise RuntimeError("Not connected to WebSocket server")
        
        max_send_attempts = 2
        current_attempts = 0
        
        while current_attempts < max_send_attempts:
            try:
                await self.websocket.send(json.dumps(message))
                print(f"Sent message: {message}")
                return
            
            except (ConnectionClosed, WebSocketException):
                await self.disconnect()
                await self.connect(self.max_reconnect_attempts)
            except Exception:
                current_attempts += 1
                if current_attempts < max_send_attempts:
                    continue
                raise
    
    async def disconnect(self) -> None:
        if self.websocket:
            try:
                await self.websocket.close()
            finally:
                self.websocket = None
    
    def is_connected(self) -> bool:
        """
        Check if the websocket is currently connected
        """
        
        return self.websocket is not None
    
    async def discover_master_node(self) -> str:
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(f"{CORE_API_URI}/master-node/discover")
                if response.status_code == 404:
                    raise MasterNodeNotFound("Master node discovery endpoint returned 404 Not Found")
                elif 500 <= response.status_code < 600:
                    raise MasterNodeServerError(f"Master node discovery failed with status {response.status_code}")
                response.raise_for_status()
                master_node_data = response.json()
                try:
                    master_node = MasterNode(**master_node_data)
                except Exception as e:
                    raise MasterNodeInvalidResponse(f"Invalid master node data: {e}")
                
                master_address = str(master_node.master_address)
            except httpx.RequestError as e:
                raise MasterNodeDiscoveryError(f"HTTP request failed: {e}") from e
            
            websocket_url = f"ws://{master_address}/ws/connect/{self.worker_id}"
            print(f"Discovered master node websocket at: {websocket_url}")
            return websocket_url