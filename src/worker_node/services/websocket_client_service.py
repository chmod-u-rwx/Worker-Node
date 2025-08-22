import asyncio
import json
import httpx
from typing import Any, Dict, Optional
from uuid import UUID
import websockets
from websockets.exceptions import ConnectionClosed, InvalidURI, InvalidHandshake, WebSocketException
from src.worker_node.config import CORE_API_URI

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
    
    async def discover_master_node(self) -> str:
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f"{CORE_API_URI}/master-node/discover")
                response.raise_for_status()
                master_node_data = response.json()
                master_address = master_node_data.get("master_address")
                if not master_address:
                    raise ValueError("Master node address not found in response")
                
                websocket_url = f"ws://{master_address}/ws/connect/{self.worker_id}"
                print(f"Discovered master node websocket at: {websocket_url}")
                return websocket_url
        except httpx.RequestError as e:
            print(f"HTTP request error during master node discovery: {e}")
            raise
        except Exception as e:
            print(f"Unexpected error during master node discovery: {e}")
            raise
    
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
            
            except (InvalidURI, InvalidHandshake) as e:
                print(f"WebSocket connection failed (invalid URI or handshake): {e}")
                if attempt == self.max_reconnect_attempts:
                    raise
                await asyncio.sleep(self.reconnect_delay)
                attempt += 1
                
            except ConnectionClosed as e:
                print(f"WebSocket connection failed (invalid URI or handshake): {e}")
                if attempt == self.max_reconnect_attempts:
                    print("Max reconnect attempts reached, trying to discover new master node")
                    
                    try:
                        websocket_url = await self.discover_master_node()
                        self.current_websocket_url = websocket_url
                        print(f"Got new master node URL: {websocket_url}, retrying connection...")
                        
                        attempt = 1
                        continue
                    except Exception as discovery_error:
                        print(f"Failed to discover new master node: {discovery_error}")
                        raise
                await asyncio.sleep(self.reconnect_delay)
                attempt += 1
                
            except Exception as e:
                print(f"Unexpected error during WebSocket connection (attempt {attempt}): {e}")
                if attempt == self.max_reconnect_attempts:
                    break
                await asyncio.sleep(self.reconnect_delay)
                attempt += 1
        
        raise ConnectionError(f"Failed to connect after {self.max_reconnect_attempts} attempts")
    
    async def reconnect(self) -> bool:
        print("Attempting to reconnect...")
        self.reconnect_attempts += 1
        
        if self.websocket:
            try:
                await self.websocket.close()
            except Exception as e:
                print(f"Error closing existing websocket: {e}")
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
                except ConnectionClosed as e:
                    print(f"WebSocket connection closed: {e}")
                    if self.running:
                        if await self.reconnect():
                            continue
                        else:
                            print("Failed to reconnect, stopping message listener")
                            break
                    else:
                        break
                
                except WebSocketException as e:
                    print(f"WebSocket error while receiving: {e}")
                    if self.running:
                        if await self.reconnect():
                            continue
                        else:
                            print("Failed to reconnect after WebSocket error")
                            break
                    else:
                        break
                        
                except Exception as e:
                    print(f"Unexpected error while receiving message: {e}")
                    if self.running:
                        if await self.reconnect():
                            continue
                        else:
                            print("Failed to reconnect after unexpected error")
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
            
            except ConnectionClosed as e:
                print(f"WebSocket connection closed while sending: {e}")
                if retry_on_failure and attempt < max_send_attempts - 1:
                    if await self.reconnect():
                        continue
                self.running = False
                raise
            
            except WebSocketException as e:
                print(f"WebSocket error while sending: {e}")
                if retry_on_failure and attempt < max_send_attempts - 1:
                    if await self.reconnect():
                        continue
                raise
            
            except Exception as e:
                print(f"Unexpected error while sending message: {e}")
                if retry_on_failure and attempt < max_send_attempts - 1:
                    if await self.reconnect():
                        continue
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