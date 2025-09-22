from PySide6.QtWidgets import QApplication
import sys
from src.worker_node_ui.screens.app_controller import AppController

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = AppController()
    controller.show_signup_create()
    sys.exit(app.exec())
