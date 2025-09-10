import psutil
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtWidgets import QMainWindow, QVBoxLayout
from src.worker_node_ui.styles.signup_ui_py.signup_almost_ui import Ui_signup_almost
from src.worker_node_ui.components.frame_bar.title_bar import TitleBar
from src.worker_node_ui.components.resources.disk_cache import DiskCache


class SignupAlmostWindow(QMainWindow):
    def __init__(self, controller = None):
        super().__init__()
        self.controller = controller
        self.ui = Ui_signup_almost()
        self.ui.setupUi(self)

        self.setWindowIcon(QtGui.QIcon("src/worker_node_ui/resources/images/desk_logo.png"))
        
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Window)
        self.title_bar = TitleBar(self)
        container_layout = QVBoxLayout(self.centralWidget())
        container_layout.setContentsMargins(0, 0, 0, 0)
        container_layout.setSpacing(0)
        container_layout.addWidget(self.title_bar, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignTop)

        self.disk_widget = DiskCache(
            disk_slider=self.ui.disk_slider,
            disk_lineedit=self.ui.disk_line,
            cores_min_label=self.ui.cores_min_label,
            cores_max_label=self.ui.cores_max_label,
            cache_lineedit=self.ui.cache_line,
            browse_button=self.ui.pushButton
        )
        if self.controller.user_resources:
            self.disk_widget.set_data(self.controller.user_resources)

        self.apply_effects()
        self.ui.next1_button.clicked.connect(self.handle_next)
        self.ui.back_button.clicked.connect(self.handle_back)

    def apply_effects(self):
        self.ui.next1_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ui.back_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        glow_effect = QtWidgets.QGraphicsDropShadowEffect()
        glow_effect.setBlurRadius(15)
        glow_effect.setOffset(0)
        glow_effect.setColor(QtGui.QColor(125, 95, 255))
        self.ui.next1_button.setGraphicsEffect(glow_effect)

    def update_resources(self):
        if not self.controller.user_resources:
            self.controller.user_resources = {}
        self.controller.user_resources.update(self.disk_widget.get_data())

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

        print(f"Cache Path: {data['cache_path']}")
        print(f"Disk Allocation: {data['disk_mb']} MB")

        self.controller.show_signup_fast()
        self.close()

    def handle_back(self):
        if self.controller:
            self.close()
            self.controller.show_signup_tell()