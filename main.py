import sys
from PySide6.QtWidgets import QApplication
from src.worker_node_ui.screens.app_controller import AppController
from worker_ws_client_runner import main
import asyncio
from uuid import uuid4
from src.worker_node_ui.providers.heartbeat_timer_provider import get_heartbeat_timer

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = AppController()
    sys.exit(app.exec())
    
    # asyncio.run(main())
	
    # heartbeat_timer = get_heartbeat_timer(worker_id=uuid4(), master_id=uuid4())
    # # await heartbeat_timer.send_heartbeat()
    # heartbeat_timer.start_timer()
    # print("reachl")
    # print("breakpoint")
    
