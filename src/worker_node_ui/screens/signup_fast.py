from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QMainWindow, QVBoxLayout
from PySide6 import QtGui
from src.worker_node_ui.styles.signup_ui_py.signup_fast_ui import Ui_signup_toDashboard
from src.worker_node_ui.components.frame_bar.title_bar import TitleBar

class SignupToDashboardWindow(QMainWindow):
    def __init__(self, controller=None):
        super().__init__()
        self.controller = controller
        self.ui = Ui_signup_toDashboard()
        self.ui.setupUi(self)

        self.setWindowIcon(QtGui.QIcon("src/worker_node_ui/resources/images/desk_logo.png"))

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)
        self.title_bar = TitleBar(self)
        container_layout = QVBoxLayout(self.centralWidget())
        container_layout.setContentsMargins(0, 0, 0, 0)
        container_layout.setSpacing(0)
        container_layout.addWidget(self.title_bar, 0, Qt.AlignRight | Qt.AlignTop)

        self.seconds_left = 3
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_countdown)
        self.timer.start(1000)

        self.ui.dashboard_button.clicked.connect(self.go_to_dashboard)

        self.update_countdown_label()

    def update_countdown_label(self):
        self.ui.info_label_2.setText(f"Automatic redirect in {self.seconds_left}s")

    def update_countdown(self):
        self.seconds_left -= 1
        if self.seconds_left > 0:
            self.update_countdown_label()
        else:
            self.timer.stop()
            self.go_to_dashboard()

    def go_to_dashboard(self):
        if not self.controller:
            print("Controller is not set")
            return

        if not self.controller.current_user or not self.controller.current_email:
            print("Username or email not set in controller")
            return

        if not hasattr(self.controller, "user_resources") or self.controller.user_resources is None:
            self.controller.user_resources = {}

        self.controller.show_gendashboard(
            username=self.controller.current_user,
            email=self.controller.current_email
        )

        if hasattr(self, "timer") and self.timer.isActive():
            self.timer.stop()

        self.close()
