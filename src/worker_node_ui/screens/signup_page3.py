import psutil
from PySide6.QtCore import Qt
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtWidgets import QVBoxLayout, QWidget, QLabel, QLineEdit, QVBoxLayout

from src.worker_node_ui.styles.signup.ui_py.signup_page3 import UiSignupAlmost
from src.worker_node_ui.components.frame_bar.title_bar import TitleBar
from src.worker_node_ui.components.resources.disk_cache import DiskCache


class SignupWindow3(QWidget):
    def __init__(self, controller=None, parent = None):
        super().__init__()
        self.controller = controller
        self.ui = UiSignupAlmost()
        self.ui.setupUi(self)

        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint | QtCore.Qt.WindowType.Window) 

        container_layout = QVBoxLayout(self)
        container_layout.setContentsMargins(0, 0, 0, 0)
        container_layout.setSpacing(0)

        self.title_bar = TitleBar(self)
        container_layout.addWidget(self.title_bar, 0, Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop)

        self.disk_widget = DiskCache(
            disk_slider=self.ui.disk_slider,
            disk_lineedit=self.ui.disk_line,
            cores_min_label=self.ui.cores_min_label,
            cores_max_label=self.ui.cores_max_label,
            cache_lineedit=self.ui.cache_line,
            browse_button=self.ui.pushButton
        )

        if getattr(self.controller, "user_resources", None):
            self.disk_widget.set_data(self.controller.user_resources) #type: ignore

        self.apply_effects()
        self.ui.next1_button.clicked.connect(self.handle_next)
        self.ui.back_button.clicked.connect(self.handle_back)

    def apply_effects(self):
        self.ui.next1_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.ui.back_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))

        glow_effect = QtWidgets.QGraphicsDropShadowEffect()
        glow_effect.setBlurRadius(15)
        glow_effect.setOffset(0)
        glow_effect.setColor(QtGui.QColor(125, 95, 255))
        self.ui.next1_button.setGraphicsEffect(glow_effect)

    def update_resources(self):
        if not getattr(self.controller, "user_resources", None):
            self.controller.user_resources = {} #type: ignore
        self.controller.user_resources.update(self.disk_widget.get_data()) #type: ignore

    def handle_next(self):
        if not self.controller:
            return

        self.update_resources()

        data = self.controller.user_resources
        if not data.get("cache_path"):
            QtWidgets.QMessageBox.warning(
                self,
                "No Path Selected",
                "Please select a cache directory before continuing."
            )
            return

        self.controller.show_signup("signup4")

    def handle_back(self):
        if self.controller:
            self.controller.show_signup("signup2")
