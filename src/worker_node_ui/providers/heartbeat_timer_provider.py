from ..timer.heartbeat_timer import HeartbeatTimer
from ...worker_node.config import INGRESS_ROUTER_URI
from uuid import UUID

def get_heartbeat_timer(worker_id: UUID, master_id: UUID) -> HeartbeatTimer:
	return HeartbeatTimer(url=INGRESS_ROUTER_URI, worker_id=worker_id, master_id=master_id,)