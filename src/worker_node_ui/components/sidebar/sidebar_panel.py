from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSizePolicy
from PySide6.QtCore import Qt

class Sidebar(QWidget):
    def __init__(self, ui, controller):
        super().__init__()
        self.ui = ui
        self.controller = controller
        self.setup_connections()

    def setup_connections(self):
        self.ui.dash_bt.clicked.connect(lambda: self.controller.show_dashboard())
        self.ui.sys_bt.clicked.connect(lambda: self.controller.show_usage_dashboard())
        self.ui.job_bt.clicked.connect(lambda: self.controller.show_job_dashboard())
        self.ui.earning_bt.clicked.connect(lambda: self.controller.show_earning_dashboard())
        self.ui.settings_bt.clicked.connect(self.controller.show_main_settings)