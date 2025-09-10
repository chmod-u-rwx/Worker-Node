from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PySide6 import QtCore
from PySide6.QtCore import Qt
from src.worker_node_ui.styles.settings_ui_py.editset_ui import Ui_Editdash

class Edit_Settings(QWidget):
    def __init__(self, controller, username="User", join_date=None, worker_id=None, parent=None):
        super().__init__()
        self.controller = controller
        
        self.ui = Ui_Editdash()
        self.ui.setupUi(self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.Dialog)
        self.setStyleSheet("background-color: #0A0A2A; color: white;")
        if parent:
            self.resize(parent.size())
        else:
            self.resize(500, 400)

        if parent:
            parent_rect = parent.frameGeometry()
            self_rect = self.frameGeometry()
            new_x = parent_rect.center().x() - self_rect.width() // 2
            new_y = parent_rect.center().y() - self_rect.height() // 2
            self.move(new_x, new_y)

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
        self.controller.show_pass_settings()

    def go_to_general_settings(self):
        self.close()
        self.controller.show_gen_settings()


    def logout(self):
        from PySide6.QtWidgets import QMessageBox
        reply = QMessageBox.question(
            self, "Logout", "Are you sure you want to log out?",
            QMessageBox.Yes | QMessageBox.No #type: ignore
        )
        if reply == QMessageBox.Yes: #type: ignore
            self.close()
            self.controller.show_login()

    def back_to_general(self):
        self.close()
        self.controller.show_gen_settings()
