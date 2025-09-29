from PySide6.QtWidgets import QDialog, QVBoxLayout, QStackedWidget, QSizePolicy
from PySide6 import QtCore

from src.worker_node_ui.screens.signup_page1 import SignupWindow1
from src.worker_node_ui.screens.signup_page2 import SignupWindow2
from src.worker_node_ui.screens.signup_page3 import SignupWindow3
from src.worker_node_ui.screens.signup_page4 import SignupWindow4

from src.worker_node_ui.screens.login_page import LoginWindow

class RegistrationStack(QDialog):
    def __init__(self, controller, parent=None):
        super().__init__(parent)
        self.controller = controller

        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint | QtCore.Qt.WindowType.Window)

        self.stack = QStackedWidget(self)
        self.pages = {}

        self.pages["signup1"] = SignupWindow1(controller, parent=self)
        self.pages["signup2"] = SignupWindow2(controller, parent=self)
        self.pages["signup3"] = SignupWindow3(controller, parent=self)
        self.pages["signup4"] = SignupWindow4(controller, parent=self)
        self.pages["login"] = LoginWindow(controller, parent=self)

        for page in self.pages.values():
            self.stack.addWidget(page)

        layout = QVBoxLayout(self)
        layout.addWidget(self.stack)
        layout.setContentsMargins(0, 0, 0, 0)

        self.show_page("signup1")

        self.setMinimumSize(1440, 810)
        self.resize(1440, 810)

    def show_page(self, page_name: str):
        if page_name in self.pages:
            self.stack.setCurrentWidget(self.pages[page_name])

