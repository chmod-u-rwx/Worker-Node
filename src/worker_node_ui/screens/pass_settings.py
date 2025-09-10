from PySide6.QtWidgets import QWidget, QVBoxLayout, QMessageBox, QLineEdit
from PySide6 import QtCore, QtGui
from src.worker_node_ui.styles.settings_ui_py.passet_ui import Ui_PassSetting

class Pass_Settings(QWidget):
    def __init__(self, controller, parent=None):
        super().__init__(parent)  
        self.controller = controller
        
        self.ui = Ui_PassSetting()
        self.ui.setupUi(self)

        self.setWindowFlags(
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.Dialog
        )
        self.setWindowIcon(QtGui.QIcon("src/worker_node_ui/resources/images/desk_logo.png"))
        self.setStyleSheet("background-color: #0A0A2A; color: white;")

        wrapper_layout = QVBoxLayout(self)
        wrapper_layout.addWidget(self.ui.passet_con)
        wrapper_layout.setContentsMargins(15, 15, 15, 15)
        wrapper_layout.setSpacing(15)

        self.setFixedSize(self.size())

        self.ui.opass_label.setEchoMode(QLineEdit.Password)
        self.ui.npass_label.setEchoMode(QLineEdit.Password)
        self.ui.cnew_pass.setEchoMode(QLineEdit.Password)

        self.ui.schanges_bt.clicked.connect(self.confirm_passowrd_change)
        self.ui.cancel_bt.clicked.connect(self.back_to_general)

    def back_to_general(self):
        self.close()
        self.controller.show_gen_settings()


    def confirm_passowrd_change(self):
        old_pass = self.ui.opass_label.text().strip()
        new_pass = self.ui.npass_label.text().strip()
        confirm_pass = self.ui.cnew_pass.text().strip()

        if not old_pass or not new_pass or not confirm_pass:
            QMessageBox.warning(
                self,
                "Error",
                "All fields must be filled before saving changes."
            )
            return

        if new_pass != confirm_pass:
            QMessageBox.warning(
                self,
                "Error",
                "New password and confirmation do not match."
            )
            return
        
        reply = QMessageBox.question(
            self,
            "Confirm Password Change",
            "Are you sure you want to change your password?\n"
            "You will need to use the new password the next time you log in.",
            QMessageBox.Yes | QMessageBox.No, #type: ignore
            QMessageBox.No #type: ignore
        )

        if reply == QMessageBox.Yes: #type: ignore
            self.apply_password_change()
            self.controller.show_gen_settings()
        
        if reply == QMessageBox.No: #type: ignore
            self.ui.opass_label.clear()
            self.ui.npass_label.clear()
            self.ui.cnew_pass.clear()

    def apply_password_change(self):
        QMessageBox.information(self, "Success", "Password successfully changed!")