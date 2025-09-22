from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtWidgets import QMainWindow
from src.worker_node_ui.styles.signup_ui_py.signup_fast_ui import Ui_signup_toDashboard


class SignupToDashboardWindow(QMainWindow):
    def __init__(self, controller=None):
        super().__init__()
        self.controller = controller
        self.ui = Ui_signup_toDashboard()
        self.ui.setupUi(self)

        self.setWindowIcon(QtGui.QIcon("src/worker_node_ui/resources/images/desk_logo.png"))

        self.seconds_left = 3
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_countdown)
        self.timer.start(1000)

        self.ui.dashboard_button.clicked.connect(self.controller.show_login)

        self.update_countdown_label()

    def update_countdown_label(self):
        self.ui.info_label_2.setText(f"Automatic redirect in {self.seconds_left}s")

    def update_countdown(self):
        self.seconds_left -= 1
        if self.seconds_left > 0:
            self.update_countdown_label()
        else:
            self.timer.stop()
            #self.controller.show_login()

    def go_to_login(self):
        if self.controller:
            self.controller.show_login()
            self.close()
