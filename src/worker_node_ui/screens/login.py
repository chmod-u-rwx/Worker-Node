from PySide6.QtCore import Qt
from PySide6 import QtGui, QtWidgets
from PySide6.QtWidgets import QMainWindow, QMessageBox, QVBoxLayout
from src.worker_node_ui.styles.login_ui_py.login_ui import Ui_login
from src.worker_node_ui.components.frame_bar.title_bar import TitleBar


class LoginWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.ui = Ui_login()
        self.ui.setupUi(self)

        self.setWindowIcon(QtGui.QIcon("src/worker_node_ui/resources/images/desk_logo.png"))

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)
        self.title_bar = TitleBar(self)
        container_layout = QVBoxLayout(self.centralWidget())
        container_layout.setContentsMargins(0, 0, 0, 0)
        container_layout.setSpacing(0)
        container_layout.addWidget(self.title_bar, 0, Qt.AlignRight | Qt.AlignTop)

        self.ui.password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.login_button_2.clicked.connect(self.handle_login)
        self.ui.signup_button.clicked.connect(self.handle_signup)

    def handle_login(self):
        username = self.ui.username_field.text().strip()
        password = self.ui.password_field.text().strip()

        if not username or not password:
            QMessageBox.warning(self, "Error", "Please enter both username and password.")
            return

        if self.authenticate_user(username, password):
            self.controller.show_gendashboard(username)
        else:
            QMessageBox.critical(self, "Login Failed", "Invalid username or password.")
            self.ui.username_field.clear()
            self.ui.password_field.clear()
            self.ui.username_field.setFocus()

        self.controller.current_user = username
        self.controller.current_email = f"{username}@whatever.com" 

    def handle_signup(self):
        self.close()
        self.controller.show_signup_create()

    def authenticate_user(self, username: str, password: str) -> bool:
        return username == "None" and password == "1234"
    
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton and self.drag_pos:
            self.move(self.pos() + event.globalPosition().toPoint() - self.drag_pos)
            self.drag_pos = event.globalPosition().toPoint()
