from PySide6.QtWidgets import QDialog, QVBoxLayout, QStackedWidget, QSizePolicy
from PySide6 import QtCore

from src.worker_node_ui.screens.dashboard_page import MainDashboard
from src.worker_node_ui.screens.information_earnings import EarnWindow
from src.worker_node_ui.screens.information_jobs import JobWindow
from src.worker_node_ui.screens.information_usage import UsageWindow

class DashboardStack(QDialog):
    def __init__(self, controller, parent=None):
        super().__init__(parent)
        self.controller = controller

        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)

        self.stack = QStackedWidget(self)
        self.pages = {}

        username = controller.current_user.get("username", "")
        email = controller.current_user.get("email", "")

        self.pages["maindash"] = MainDashboard(controller, username, email)
        self.pages["earnings"] = EarnWindow(controller, username, email)
        self.pages["jobs"] = JobWindow(controller, username, email)
        self.pages["usage"] = UsageWindow(controller, username, email)

        for page in self.pages.values():
            self.stack.addWidget(page)

        layout = QVBoxLayout(self)
        layout.addWidget(self.stack)
        layout.setContentsMargins(0, 0, 0, 0)

        self.show_page("maindash")

        self.setMinimumSize(1440, 810)
        self.resize(1440, 810)

    def show_page(self, page_name: str):
        if page_name in self.pages:
            self.stack.setCurrentWidget(self.pages[page_name])