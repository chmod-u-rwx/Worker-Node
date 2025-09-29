from PySide6.QtWidgets import QWidget

class Sidebar(QWidget):
    def __init__(self, ui, controller):
        super().__init__()
        self.ui = ui
        self.controller = controller
        self.setup_connections()

    def setup_connections(self):
        self.ui.dash_bt.clicked.connect(lambda: self.controller.show_dashboard("maindash"))
        self.ui.sys_bt.clicked.connect(lambda: self.controller.show_dashboard("usage"))
        self.ui.job_bt.clicked.connect(lambda: self.controller.show_dashboard("jobs"))
        self.ui.earning_bt.clicked.connect(lambda: self.controller.show_dashboard("earnings"))
        self.ui.settings_bt.clicked.connect(self.controller.show_settings)
