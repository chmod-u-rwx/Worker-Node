from PySide6.QtWidgets import QWidget, QMessageBox, QVBoxLayout
from PySide6 import QtCore
from src.worker_node_ui.styles.settings.ui_py.setting_profile import UiProfileSetting
from src.worker_node_ui.components.helper.storage_helper import clear_session


class ProfileSetting(QWidget):
    def __init__(self, controller, parent=None):
        super().__init__(parent)
        self.controller = controller
        self.settings_dialog = parent
        self.ui = UiProfileSetting()
        self.ui.setupUi(self)

        user = controller.current_user or {}
        username = user.get("username", "User")
        join_date = user.get("join_date", "N/A")
        worker_id = user.get("worker_id", "N/A")

        self.ui.uname_label.setText(username)
        self.ui.jdate_label.setText(join_date)
        self.ui.wid_label.setText(worker_id)

        self.ui.logout_bt.clicked.connect(self.logout)
        self.ui.cancel_bt.clicked.connect(self.back_to_main)
        self.ui.rallocation_bt.clicked.connect(self.back_to_main)
        self.ui.chpass_bt.clicked.connect(self.open_change_password)


    def open_change_password(self):
        if self.settings_dialog:
            self.settings_dialog.show_page("password")

    def back_to_main(self):
        if self.settings_dialog:
            self.settings_dialog.show_page("main")

    def logout(self):
        reply = QMessageBox.question(
            self,
            "Logout",
            "Are you sure you want to log out?",
            QMessageBox.Yes | QMessageBox.No  # type: ignore
        )
        if reply == QMessageBox.Yes:  # type: ignore
            clear_session()
            self.controller.current_user = {}
            self.controller.current_email = None
            if self.settings_dialog:
                self.settings_dialog.close()
            self.controller.show_login()
