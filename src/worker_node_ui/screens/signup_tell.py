from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtWidgets import QMainWindow
from src.worker_node_ui.styles.signup_ui_py.signup_tell_ui import Ui_SignupTell


class SignupTellWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.ui = Ui_SignupTell()
        self.ui.setupUi(self)

        self.setWindowIcon(QtGui.QIcon("src/worker_node_ui/resources/images/signup1logo.png"))

        self.ui.cpu_slider.setRange(0, 100)
        self.ui.cores_slider.setRange(1, 8) 
        self.ui.ram_slider.setRange(0, 1600)

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

        self.ui.cpu_slider.valueChanged.connect(self.update_cpu_lineedit)
        self.ui.cores_slider.valueChanged.connect(self.update_cores_lineedit)
        self.ui.ram_slider.valueChanged.connect(self.update_ram_lineedit)

        self.ui.cpu_lineedit.editingFinished.connect(self.update_cpu_slider)
        self.ui.cores_lineedit.editingFinished.connect(self.update_cores_slider)
        self.ui.ram_lineedit.editingFinished.connect(self.update_ram_slider)

    def update_cpu_lineedit(self, value):
        self.ui.cpu_lineedit.setText(f"{value}%")

    def update_cpu_slider(self):
        try:
            value = int(self.ui.cpu_lineedit.text().replace("%", ""))
            value = max(0, min(100, value))
            self.ui.cpu_slider.setValue(value)
        except ValueError:
            pass

    def update_cores_lineedit(self, value):
        self.ui.cores_lineedit.setText(str(value))

    def update_cores_slider(self):
        try:
            value = int(self.ui.cores_lineedit.text())
            value = max(1, min(8, value))
            self.ui.cores_slider.setValue(value)
        except ValueError:
            pass

    def update_ram_lineedit(self, value):
        self.ui.ram_lineedit.setText(f"{value} MB")

    def update_ram_slider(self):
        try:
            value = int(self.ui.ram_lineedit.text().replace("MB", ""))
            value = max(0, min(1600, value))
            self.ui.ram_slider.setValue(value)
        except ValueError:
            pass

    def handle_next(self):
        cpu = self.ui.cpu_slider.value()
        cores = self.ui.cores_slider.value()
        ram = self.ui.ram_slider.value()

        self.controller.show_signup_almost()
        self.close()

    def handle_back(self):
        self.controller.show_signup_create()
