from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSizePolicy
from PySide6.QtCore import Qt

class Dash_Sidebar(QWidget):
    def __init__(self, ui, controller):
        super().__init__()
        self.ui = ui
        self.controller = controller
        self.setup_connections()

    def setup_connections(self):
        self.ui.dash_bt.clicked.connect(lambda: self.controller.show_gendashboard())
        self.ui.sys_bt.clicked.connect(lambda: self.controller.show_info_usage())
        self.ui.job_bt.clicked.connect(lambda: self.controller.show_info_job())
        self.ui.earning_bt.clicked.connect(lambda: self.controller.show_info_earning())
        self.ui.settings_bt.clicked.connect(self.controller.show_gen_settings)