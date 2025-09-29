from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6 import QtGui
from src.worker_node_ui.styles.signup.ui_py.signup_page4 import UiSignupLast
from src.worker_node_ui.components.frame_bar.title_bar import TitleBar


class SignupWindow4(QWidget):
    def __init__(self, controller=None, parent = None):
        super().__init__()
        self.controller = controller
        self.ui = UiSignupLast()
        self.ui.setupUi(self)

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Window)

        self.container_layout = QVBoxLayout(self)
        self.container_layout.setContentsMargins(0, 0, 0, 0)
        self.container_layout.setSpacing(0)
        self.title_bar = TitleBar(self)
        self.container_layout.addWidget(self.title_bar, 0, Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop)

        self.seconds_left = 3
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self._tick)

        self.ui.info_label_2.setText(f"Redirecting in {self.seconds_left}s")

        self.ui.dashboard_button.clicked.connect(self._skip)

    def showEvent(self, event):
        super().showEvent(event)
        self.timer.start()

    def _tick(self):
        self.seconds_left -= 1
        if self.seconds_left > 0:
            self.ui.info_label_2.setText(f"Redirecting in {self.seconds_left}s")
        else:
            self._skip()

    def _skip(self):
        if self.timer.isActive():
            self.timer.stop()
        if self.controller:
            self.controller.show_dashboard("maindash")
        if self.parent():
            self.parent().hide() #type:ignore


