# worker_ws_client = WebsocketClientService(UUID("3fa85f64-5717-4562-b3fc-2c963f66afa6"))

from ...worker_node.services.websocket_client_service import WebsocketClientService
from uuid import UUID

websocket_client_service: WebsocketClientService | None = None
def get_websocket_client_service(worker_id: UUID) -> WebsocketClientService:
	global websocket_client_service
	if not websocket_client_service:
		websocket_client_service = WebsocketClientService(worker_id=worker_id)
	return websocket_client_service