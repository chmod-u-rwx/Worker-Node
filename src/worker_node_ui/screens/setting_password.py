from PySide6.QtWidgets import QWidget, QVBoxLayout, QMessageBox, QLineEdit
from src.worker_node_ui.styles.settings.ui_py.setting_password import UiPasswordSetting


class PasswordSetting(QWidget):
    def __init__(self, controller, parent=None):
        super().__init__(parent)
        self.controller = controller
        self.settings_dialog = parent
        self.ui = UiPasswordSetting()
        self.ui.setupUi(self)

        self.ui.opass_label.setEchoMode(QLineEdit.EchoMode.Password)
        self.ui.npass_label.setEchoMode(QLineEdit.EchoMode.Password)
        self.ui.cnew_pass.setEchoMode(QLineEdit.EchoMode.Password)

        self.ui.schanges_bt.clicked.connect(self.confirm_password_change)
        self.ui.cancel_bt.clicked.connect(self.back_to_general)

    def back_to_general(self):
        if self.settings_dialog:
            self.settings_dialog.show_page("main")

    def confirm_password_change(self):
        old_pass = self.ui.opass_label.text().strip()
        new_pass = self.ui.npass_label.text().strip()
        confirm_pass = self.ui.cnew_pass.text().strip()

        if not old_pass or not new_pass or not confirm_pass:
            QMessageBox.warning(self, "Error", "All fields must be filled before saving changes.")
            return

        if new_pass != confirm_pass:
            QMessageBox.warning(self, "Error", "New password and confirmation do not match.")
            return

        reply = QMessageBox.question(
            self,
            "Confirm Password Change",
            "Are you sure you want to change your password?\n"
            "You will need to use the new password the next time you log in.",
            QMessageBox.Yes | QMessageBox.No,  # type: ignore
            QMessageBox.No  # type: ignore
        )

        if reply == QMessageBox.Yes:  # type: ignore
            self.apply_password_change()
            if self.settings_dialog:
                self.settings_dialog.show_page("main")
        else:
            self.ui.opass_label.clear()
            self.ui.npass_label.clear()
            self.ui.cnew_pass.clear()

    def apply_password_change(self):
        #update pass
        QMessageBox.information(self, "Success", "Password successfully changed!")
