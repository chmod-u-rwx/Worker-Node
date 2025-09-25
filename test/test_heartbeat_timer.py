from unittest.mock import patch
from uuid import uuid4
import pytest
from src.worker_node_ui.providers.heartbeat_timer_provider import get_heartbeat_timer
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QTimer

#  -pip install pytest-qt
async def test_heartbeat_with_mock(qtbot):
    worker_id = uuid4()
    heartbeat_timer = get_heartbeat_timer(worker_id=worker_id, master_id=uuid4())
    with patch("httpx.post") as mock_post:
        heartbeat_timer.start_timer()
        qtbot.wait(heartbeat_timer.timer.interval() + 50)
        heartbeat_timer.stop_timer()
        assert mock_post.called

# run this in debugger to see start timer does start
@pytest.mark.integration
async def test_heartbeat_integration():
    qapp = QApplication.instance() or QApplication([])

    worker_id = uuid4()
    heartbeat_timer = get_heartbeat_timer(worker_id=worker_id, master_id=uuid4())

    heartbeat_timer.start_timer()
    qapp.exec()

    # if i want to stop process do
    #     heartbeat_timer.stop_timer()
    #     qapp.quit()

@pytest.mark.integration
async def test_heartbeat_stop_start():
    qapp = QApplication.instance() or QApplication([])

    worker_id = uuid4()
    heartbeat_timer = get_heartbeat_timer(worker_id=worker_id, master_id=uuid4())

    heartbeat_timer.start_timer()
    QTimer.singleShot(2000,lambda: (heartbeat_timer.stop_timer(), qapp.quit())) # suppoesd to quit after 2000ms
    qapp.exec()


    