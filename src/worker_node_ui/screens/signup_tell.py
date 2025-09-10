import psutil
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QVBoxLayout
from PySide6 import QtWidgets, QtCore, QtGui
from src.worker_node_ui.styles.signup_ui_py.signup_tell_ui import Ui_SignupTell
from src.worker_node_ui.components.frame_bar.title_bar import TitleBar
from src.worker_node_ui.components.resources.res_allocation import ResourceAllocation


class SignupTellWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.ui = Ui_SignupTell()
        self.ui.setupUi(self)

        self.setWindowIcon(QtGui.QIcon("src/worker_node_ui/resources/images/desk_logo.png"))

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)
        self.title_bar = TitleBar(self)
        container_layout = QVBoxLayout(self.centralWidget())
        container_layout.setContentsMargins(0, 0, 0, 0)
        container_layout.setSpacing(0)
        container_layout.addWidget(self.title_bar, 0, Qt.AlignRight | Qt.AlignTop)

        self.resource_config = ResourceAllocation(
            cpu_slider=self.ui.cpu_slider,
            cpu_lineedit=self.ui.cpu_lineedit,
            cores_slider=self.ui.cores_slider,
            cores_lineedit=self.ui.cores_lineedit,
            ram_slider=self.ui.ram_slider,
            ram_lineedit=self.ui.ram_lineedit,
            cpu_min_label=self.ui.cpu_min_label,
            cpu_max_label=self.ui.cpu_max_label,
            cores_min_label=self.ui.cores_min_label,
            cores_max_label=self.ui.cores_max_label,
            ram_min_label=self.ui.ram_min_label,
            ram_max_label=self.ui.ram_max_label
        )

        if self.controller.user_resources:
            self.resource_config.set_data(self.controller.user_resources)


        self.ui.next1_button.clicked.connect(self.handle_next)
        self.apply_effects()
        self.setup_logic()

    def apply_effects(self):
        self.ui.next1_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ui.back_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        glow_effect = QtWidgets.QGraphicsDropShadowEffect()
        glow_effect.setBlurRadius(15)
        glow_effect.setOffset(0)
        glow_effect.setColor(QtGui.QColor(125, 95, 255))
        self.ui.next1_button.setGraphicsEffect(glow_effect)

    def setup_logic(self):
        self.ui.next1_button.clicked.connect(self.handle_next)
        self.ui.back_button.clicked.connect(self.handle_back)

    def handle_next(self):
        self.controller.user_resources = self.resource_config.get_data()
        self.controller.show_signup_almost()

    def handle_back(self):
        self.controller.show_signup_create()