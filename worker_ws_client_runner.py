import asyncio
import src.worker_node.core.qemu_pool # type: ignore instantiate qemu pools 
from src.worker_node.services.websocket_client_service import WebsocketClientService

async def main(worker_ws_client: WebsocketClientService):
	await worker_ws_client.connect(3)
	await worker_ws_client.listen_for_messages()

# if __name__ == "__main__":
# 	# asyncio.run(main())