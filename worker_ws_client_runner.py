import asyncio
from src.worker_node.services.websocket_client_service import worker_ws_client

async def main():
	await worker_ws_client.connect(3)
	await worker_ws_client.listen_for_messages()

if __name__ == "__main__":
	asyncio.run(main())