import json
from typing import Any, Dict, Optional
from uuid import UUID
import websockets
from websockets.exceptions import ConnectionClosed, InvalidURI, InvalidHandshake, WebSocketException
import src.worker_node.config as config

class WorkerNodeWebsocketClientService:
    def __init__(self, worker_id: UUID):
        if not config.MASTER_NODE_API_URL:
            raise ValueError("MASTER_NODE_API_URL not set")
        
        self.worker_id = str(worker_id)
        self.master_node_api_url = config.MASTER_NODE_API_URL
        self.websocket_port = config.MASTER_NODE_WEBSOCKET_PORT
        self.websocket = None
        self.running = False
    
    async def discover_master_node(self) -> str:
        import httpx
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(f"{self.master_node_api_url}/master-node/discover")
                response.raise_for_status()
                master_node_data = response.json()
                master_address = master_node_data.get("master_address")
                if not master_address:
                    raise ValueError("Master node address not found in response")

                websocket_url = f"ws://{master_address}:{self.websocket_port}/ws/connect/{self.worker_id}"
                print(f"Discovered master node websocket at: {websocket_url}")
                return websocket_url
        except httpx.RequestError as e:
            print(f"HTTP request error during master node discovery: {e}")
            raise
        except Exception as e:
            print(f"Unexpected error during master node discovery: {e}")
            raise
    
    async def connect(self, websocket_url: Optional[str] = None) -> None:
        try:
            if not websocket_url:
                websocket_url = await self.discover_master_node()
            
            print(f"Connecting to WebSocket server at: {websocket_url}")
            self.websocket = await websockets.connect(websocket_url)
            self.running = True
            print("Successfully connected to WebSocket server")
        except (InvalidURI, InvalidHandshake) as e:
            print(f"WebSocket connection failed (invalid URI or handshake): {e}")
            raise
        except ConnectionRefusedError as e:
            print(f"WebSocket connection refused: {e}")
            raise
        except Exception as e:
            print(f"Unexpected error during WebSocket connection: {e}")
            raise
    
    async def listen_for_messages(self) -> None:
        if not self.websocket:
            raise RuntimeError("Not connected to WebSocket server")
        print("Listening for messages...")
        
        try:
            while self.running:
                try:
                    message = await self.websocket.recv()
                except ConnectionClosed as e:
                    print(f"WebSocket connection closed: {e}")
                    break
                except WebSocketException as e:
                    print(f"WebSocket error while receiving: {e}")
                    break
                except Exception as e:
                    print(f"Unexpected error while receiving message: {e}")
                    break
                
                try:
                    data = json.loads(message)
                    print(f"Received JSON message: {data}")
                except json.JSONDecodeError:
                    print(f"Received non-JSON message: {message}")
        except Exception as e:
            print(f"Error in listen_for_messages: {e}")
        finally:
            self.running = False
            try:
                await self.disconnect()
            except Exception as e:
                print(f"Error during disconnect: {e}")
    
    async def send_message(self, message: Dict[str, Any]) -> None:
        if not self.websocket:
            raise RuntimeError("Not connected to WebSocket server")
        
        try:
            await self.websocket.send(json.dumps(message))
            print(f"Sent message: {message}")
        except ConnectionClosed as e:
            print(f"WebSocket connection closed while sending: {e}")
            self.running = False
            await self.disconnect()
            raise
        except WebSocketException as e:
            print(f"WebSocket error while sending: {e}")
            raise
        except Exception as e:
            print(f"Unexpected error while sending message: {e}")
            raise
    
    async def disconnect(self) -> None:
        self.running = False
        if self.websocket:
            try:
                await self.websocket.close()
                print("Disconnected from WebSocket server")
            except Exception as e:
                print(f"Error during disconnection: {e}")