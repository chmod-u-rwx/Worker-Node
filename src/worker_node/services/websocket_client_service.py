import json
import httpx
from typing import Any, Dict, Optional
from uuid import UUID
import websockets
from websockets.exceptions import ConnectionClosed, InvalidURI, InvalidHandshake, WebSocketException
from src.worker_node.config import CORE_API_URI

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
            reconnect_delay: int = 5
        ):
        self.worker_id = str(worker_id)
        self.websocket = None
        self.running = False
        self.max_reconnect_attempts = max_reconnect_attempts
        self.reconnect_delay = reconnect_delay
        self.current_websocket_url = None
        self.reconnect_attempts = 0
    
    async def connect(self, websocket_url: Optional[str] = None) -> None:
        if not websocket_url:
                websocket_url = await self.discover_master_node()
        
        self.current_websocket_url = websocket_url
        
        attempt = 1
        while attempt <= self.max_reconnect_attempts:
            try:
                print(f"Connecting to WebSocket server at: {websocket_url} (attempt {attempt})")
                self.websocket = await websockets.connect(websocket_url)
                self.running = True
                self.reconnect_attempts = 0
                print("Successfully connected to WebSocket server")
                return
            
            except (InvalidURI, InvalidHandshake, ConnectionClosed) as e:
                print(f"{type(e).__name__} during WebSocket connection (attempt {attempt}): {e}")
                if isinstance(e, ConnectionClosed) and attempt == self.max_reconnect_attempts:
                    print("Max reconnect attempts reached, trying to discover new master node")
                    websocket_url = await self.discover_master_node()
                    self.current_websocket_url = websocket_url
                    print(f"Got new master node URL: {websocket_url}, retrying connection...")
                    attempt = 1
                    continue
                
                if attempt == self.max_reconnect_attempts:
                    break
                
            except Exception as e:
                print(f"Unexpected error during WebSocket connection (attempt {attempt}): {e}")
                if attempt == self.max_reconnect_attempts:
                    break
            finally:
                attempt += 1
        
        raise ConnectionError(f"Failed to connect after {self.max_reconnect_attempts} attempts")
    
    async def reconnect(self) -> bool:
        print("Attempting to reconnect...")
        self.reconnect_attempts += 1
        
        # Always close and clear any existing websocket
        if self.websocket:
            try:
                await self.websocket.close()
            except Exception as e:
                print(f"Error closing existing websocket: {e}")
            finally:
                self.websocket = None
        
        try:
            if self.reconnect_attempts <= self.max_reconnect_attempts:
                await self.connect(self.current_websocket_url)
                print(f"Reconnection successful (attempt {self.reconnect_attempts})")
                return True
            else:
                print("Max reconnect attempts reached, discovering new master node")
                await self.connect()
                print("Reconnection with new master node successful")
                return True
        
        except ConnectionError as e:
            print(f"Reconnecition failed with ConnectionError: {e}")
            await self.disconnect()
            try:
                await self.connect()
                print("Reconnection after forced disconnect successful")
                return True
            except Exception as e:
                print(f"Final reconnection attempt failed: {e}")
                return False
        
        except Exception as e:
            print(f"Reconnection failed: {e}")
            return False
    
    async def listen_for_messages(self) -> None:
        if not self.websocket:
            raise RuntimeError("Not connected to WebSocket server")
        
        print("Listening for messages...")
        
        while self.running:
            try:
                try:
                    message = await self.websocket.recv()
                except (ConnectionClosed, WebSocketException, Exception) as e:
                    print(f"{type(e).__name__} while listening for message: {e}")
                    if self.running:
                        if await self.reconnect():
                            continue
                        else:
                            print("Failed to reconnect, stopping message listener")
                            break
                    else:
                        break
                
                try:
                    data = json.loads(message)
                    print(f"Received JSON message: {data}")
                except json.JSONDecodeError:
                    print(f"Received non-JSON message: {message}")
                    
            except Exception as e:
                print(f"Error in listen_for_messages: {e}")
                if self.running and not await self.reconnect():
                    break
        
        self.running = False
        await self.disconnect()
    
    async def send_message(self, message: Dict[str, Any], retry_on_failure: bool = True) -> None:
        if not self.websocket:
            raise RuntimeError("Not connected to WebSocket server")
        
        max_send_attempts = 2
        
        for attempt in range(max_send_attempts):
            try:
                await self.websocket.send(json.dumps(message))
                print(f"Sent message: {message}")
                return
            
            except (ConnectionClosed, WebSocketException, Exception) as e:
                print(f"{type(e).__name__} while sending message: {e}")
                if retry_on_failure and attempt < max_send_attempts - 1:
                    if await self.reconnect():
                        continue
                if isinstance(e, ConnectionClosed):
                    self.running = False
                raise
    
    async def disconnect(self) -> None:
        print("Disconnecting from WebSocket server")
        self.running = False
        
        if self.websocket:
            try:
                await self.websocket.close()
                print("Disconnected from WebSocket server")
            except Exception as e:
                print(f"Error during disconnection: {e}")
            finally:
                self.websocket = None
    
    def is_connected(self) -> bool:
        """
        Check if the websocket is currently connected
        """
        
        return self.websocket is not None
    
    async def ensure_connected(self) -> None:
        if not self.is_connected():
            print("WebSocket not connected, attempting to connect...")
            await self.connect()
    
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
                master_address = master_node_data.get("master_address")
                if not master_address:
                    raise MasterNodeInvalidResponse("Master node address not found in response")
            except httpx.RequestError as e:
                raise MasterNodeDiscoveryError(f"HTTP request failed: {e}") from e
            
            websocket_url = f"ws://{master_address}/ws/connect/{self.worker_id}"
            print(f"Discovered master node websocket at: {websocket_url}")
            return websocket_url