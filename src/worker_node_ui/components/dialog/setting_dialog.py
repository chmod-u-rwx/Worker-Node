from PySide6.QtWidgets import QDialog, QVBoxLayout, QStackedWidget, QSizePolicy
from PySide6 import QtCore

from src.worker_node_ui.screens.setting_main import MainSetting
from src.worker_node_ui.screens.setting_password import PasswordSetting
from src.worker_node_ui.screens.setting_profile import ProfileSetting

class SettingsDialog(QDialog):
    def __init__(self, controller, parent=None):
        super().__init__(parent)
        self.controller = controller

        self.setWindowFlags(QtCore.Qt.WindowType.Dialog | QtCore.Qt.WindowType.WindowTitleHint)
        self.setStyleSheet("background-color: #0A0A2A; color: white;")

        self.stack = QStackedWidget(self)
        self.pages = {}

        self.pages["main"] = MainSetting(controller, parent=self)
        self.pages["profile"] = ProfileSetting(controller, parent=self)
        self.pages["password"] = PasswordSetting(controller, parent=self)

        for page in self.pages.values():
            self.stack.addWidget(page)

        layout = QVBoxLayout(self)
        layout.addWidget(self.stack)
        layout.setContentsMargins(0, 0, 0, 0)

        self.show_page("main")

        self.setMinimumSize(800, 600)
        self.resize(1031, 569)

    def show_page(self, page_name: str):
        if page_name in self.pages:
            self.stack.setCurrentWidget(self.pages[page_name])
