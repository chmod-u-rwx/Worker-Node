from PySide6.QtCore import Qt
from PySide6 import QtGui, QtWidgets
from PySide6.QtWidgets import QWidget, QMessageBox, QVBoxLayout
from src.worker_node_ui.styles.login.login_page import UiLoginPage
from src.worker_node_ui.components.frame_bar.title_bar import TitleBar
from src.worker_node_ui.components.dialog.dialog_message import show_custom_error

class LoginWindow(QWidget):
    def __init__(self, controller, parent = None):
        super().__init__()
        self.controller = controller
        self.ui = UiLoginPage()
        self.ui.setupUi(self)

        self.setWindowIcon(QtGui.QIcon("src/worker_node_ui/resources/images/desk_logo.png"))
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Window)

        self.title_bar = TitleBar(self)

        container_layout = QVBoxLayout(self)
        container_layout.setContentsMargins(0, 0, 0, 0)
        container_layout.setSpacing(0)
        container_layout.addWidget(self.title_bar, 0, Qt.AlignmentFlag.AlignTop)
        container_layout.addStretch()

        self.ui.password_field.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.ui.login_button_2.clicked.connect(self.handle_login)
        self.ui.signup_button.clicked.connect(self.handle_signup)

        self.drag_pos = None

    def handle_login(self):
        email = self.ui.email_field.text().strip()
        password = self.ui.password_field.text().strip()

        if not email or not password:
            show_custom_error(self, "Please enter both email address and password.")
            return

        success = self.controller.login_user({
            "email": email,
            "password": password
        })

        if success:
            self.controller.show_dashboard()
        else:
            show_custom_error(self, "Invalid email or password.")
            self.ui.email_field.clear()
            self.ui.password_field.clear()
            self.ui.email_field.setFocus()

    def handle_signup(self):
        self.close()
        self.controller.show_signup("signup1")
