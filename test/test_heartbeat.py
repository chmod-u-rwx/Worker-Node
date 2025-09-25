import pytest
import asyncio
from unittest.mock import patch
from PySide6.QtWidgets import QApplication
from src.worker_node_ui.providers.websocket_client_provider import get_websocket_client_service
from src.worker_node_ui.providers.heartbeat_timer_provider import get_heartbeat_timer
from uuid import uuid4
from pytestqt import qtbot
from uuid import UUID, uuid4


#  -qtbot
@pytest.mark.integration
@pytest.mark.asyncio
async def test_heartbeat(qtbot):
    # app = QApplication.instance() or QApplication([])
    # loop = QEventLoop(app)
    # asyncio.set_event_loop(loop)
    worker_id = uuid4()
    heartbeat_timer = get_heartbeat_timer(worker_id=worker_id, master_id=uuid4())
    with patch("httpx.post") as mock_post:
        heartbeat_timer.start_timer()
        qtbot.wait(heartbeat_timer.timer.interval() + 50)
        heartbeat_timer.stop_timer()
        assert mock_post.called

# - anyio
#   - pytest-asyncio
#   - pytest-tornasync
#   - pytest-trio
#   - pytest-twisted

@pytest.mark.integration
@pytest.mark.asyncio
async def test_heartbeat_with_async_no_qasync():
    qapp = QApplication.instance() or QApplication([])

    worker_id = uuid4()
    heartbeat_timer = get_heartbeat_timer(worker_id=worker_id, master_id=uuid4())

    heartbeat_timer.start_timer()
    qapp.exec()

    # if i sstop process
    #     heartbeat_timer.stop_timer()
    #     qapp.quit() 
    

@pytest.mark.integration
@pytest.mark.asyncio
async def testt_heartbeat_ai_integration():
    qapp = QApplication.instance() or QApplication([])

    worker_id = uuid4()
    websocket_client_service = get_websocket_client_service(worker_id=worker_id)
    await websocket_client_service.connect(3)
    asyncio.create_task(websocket_client_service.listen_for_messages())
    heartbeat_timer = get_heartbeat_timer(worker_id=worker_id, master_id=UUID(websocket_client_service.worker_id))
    heartbeat_timer.start_timer()
    qapp.exec()

    # if i sstop process
    #     heartbeat_timer.stop_timer()
    #     qapp.quit() 
    