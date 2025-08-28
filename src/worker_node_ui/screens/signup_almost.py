from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtWidgets import QMainWindow
from src.worker_node_ui.styles.signup_ui_py.signup_almost_ui import Ui_signup_almost

class SignupAlmostWindow(QMainWindow):
    def __init__(self, controller=None):
        super().__init__()
        self.controller = controller
        self.ui = Ui_signup_almost()
        self.ui.setupUi(self)

        self.setWindowIcon(QtGui.QIcon("src/worker_node_ui/resources/images/signup1logo.png"))

        self.ui.disk_slider.setRange(0, 1600)

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

        self.ui.disk_slider.valueChanged.connect(self.update_disk_lineedit)
        self.ui.disk_line.editingFinished.connect(self.update_disk_slider)

    def update_disk_lineedit(self, value):
        self.ui.disk_line.setText(str(value))

    def update_disk_slider(self):
        try:
            value = int(self.ui.disk_line.text())
            value = max(0, min(100, value))
            self.ui.disk_slider.setValue(value)
        except ValueError:
            pass

    def handle_next(self):
        if self.controller:
            self.close()
            self.controller.show_signup_fast()

    def handle_back(self):
        if self.controller:
            self.close()
            self.controller.show_signup_tell()
