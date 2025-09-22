from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PySide6 import QtCore
from PySide6.QtCore import Qt
from src.worker_node_ui.styles.settings.ui_py.setting_profile import UiProfileSetting

class ProfileSetting(QWidget):
    def __init__(self, controller, username="User", join_date=None, worker_id=None):
        super().__init__()
        self.controller = controller
        
        self.ui = UiProfileSetting()
        self.ui.setupUi(self)

        self.setWindowFlags(
            QtCore.Qt.WindowType.FramelessWindowHint |
            QtCore.Qt.WindowType.WindowStaysOnTopHint |
            QtCore.Qt.WindowType.Dialog
        )
        self.setStyleSheet("background-color: #0A0A2A; color: white;")

        if join_date is None:
            from datetime import datetime
            join_date = datetime.now().strftime("%m/%d/%Y")
        if worker_id is None:
            import uuid
            worker_id = str(uuid.uuid4())

        self.ui.jdate_label.setText(join_date)
        self.ui.uname_label.setText(username)
        self.ui.wid_label.setText(worker_id)

        self.ui.logout_bt.clicked.connect(self.logout)
        self.ui.cancel_bt.clicked.connect(self.go_to_general_settings)
        self.ui.rallocation_bt.clicked.connect(self.go_to_general_settings)
        self.ui.chpass_bt.clicked.connect(self.open_change_password)

    def open_change_password(self):
        self.close()
        self.controller.show_password_settings()

    def go_to_general_settings(self):
        self.close()
        self.controller.show_main_settings()

    def logout(self):
        from PySide6.QtWidgets import QMessageBox
        reply = QMessageBox.question(
            self, "Logout", "Are you sure you want to log out?",
            QMessageBox.Yes | QMessageBox.No  # type: ignore
        )
        if reply == QMessageBox.Yes:  # type: ignore
            self.close()
            self.controller.show_login()

    def back_to_general(self):
        self.close()
        self.controller.show_main_settings()
