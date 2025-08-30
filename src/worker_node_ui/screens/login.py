from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6 import QtGui
from src.worker_node_ui.styles.login_ui_py.login_ui import Ui_login

class LoginWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.ui = Ui_login()
        self.ui.setupUi(self)

        self.setWindowIcon(QtGui.QIcon("src/worker_node_ui/resources/images/desk_logo.png"))

        self.ui.login_button_2.clicked.connect(self.handle_login)
        self.ui.signup_button.clicked.connect(self.handle_signup)

    def handle_login(self):
        username = self.ui.username_field.text().strip()
        password = self.ui.password_field.text().strip()

        if not username or not password:
            QMessageBox.warning(self, "Error", "Please enter both username and password.")
            return

        #temporary 
        if username == "admin" and password == "admin":
            QMessageBox.information(self, "Success", "Login successful!")
            self.close()
            # self.controller.show_signup_fast() to dashboard
        else:
            QMessageBox.critical(self, "Error", "Invalid username or password.")

    def handle_signup(self):
        self.close()
        self.controller.show_signup_create()
