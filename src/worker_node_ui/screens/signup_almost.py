import psutil
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtWidgets import QMainWindow, QFileDialog
from PySide6.QtGui import QIntValidator
from src.worker_node_ui.styles.signup_ui_py.signup_almost_ui import Ui_signup_almost

class SignupAlmostWindow(QMainWindow):
    def __init__(self, controller=None):
        super().__init__()
        self.controller = controller
        self.ui = Ui_signup_almost()
        self.ui.setupUi(self)

        self.setWindowIcon(QtGui.QIcon("src/worker_node_ui/resources/images/desk_logo.png"))

        self.setup_disk_slider()

        self.apply_effects()
        self.setup_logic()

    def setup_disk_slider(self):
        try:
            usage = psutil.disk_usage("/")
            total_mb = usage.total // (1024**2)
            self.disk_min = 0
            self.disk_max = total_mb
            self.ui.disk_slider.setRange(self.disk_min, self.disk_max)

            self.ui.cores_min_label.setText(f"{self.disk_min} MB")
            self.ui.cores_max_label.setText(f"{self.disk_max} MB")
            self.ui.cores_min_label.adjustSize()
            self.ui.cores_max_label.adjustSize()

            default_value = min(1024, self.disk_max // 10)
            self.ui.disk_slider.setValue(default_value)
            self.ui.disk_line.setText(str(default_value))

            validator = QIntValidator(self.disk_min, self.disk_max, self)
            self.ui.disk_line.setValidator(validator)
            default_value = min(1024, self.disk_max // 10)
            self.ui.disk_slider.setValue(default_value)
            self.ui.disk_line.setText(str(default_value))

        except Exception as e:
            print("Error detecting disk space:", e)
            self.ui.disk_slider.setRange(0, 1600)
            self.ui.cores_min_label.setText("0 MB")
            self.ui.cores_max_label.setText("1600 MB")
            self.ui.disk_line.setText("800")

    def apply_effects(self):
        self.ui.next1_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor)) #type:ignore
        self.ui.back_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor)) #type:ignore

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

        self.ui.pushButton.clicked.connect(self.select_cache_path)

    def update_disk_lineedit(self, value):
        self.ui.disk_line.setText(str(value))

    def update_disk_slider(self):
        try:
            value = int(self.ui.disk_line.text())
            value = max(self.disk_min, min(self.disk_max, value))
            self.ui.disk_slider.setValue(value)
        except ValueError:
            pass

    def select_cache_path(self):
        folder = QFileDialog.getExistingDirectory(self)
        if folder:
            self.ui.cache_line.setText(folder)

    def handle_next(self):
        if self.controller:
            cache_path = self.ui.cache_line.text().strip()
            if not cache_path:
                QtWidgets.QMessageBox.warning(
                    self,
                    "No Path Selected",
                    "Please select a cache directory before continuing."
                )
                return

            disk_allocation = self.ui.disk_slider.value()
            print(f"Cache Path: {cache_path}")
            print(f"Disk Allocation: {disk_allocation} MB")

        self.close()
        self.controller.show_signup_fast()

    def handle_back(self):
        if self.controller:
            self.close()
            self.controller.show_signup_tell()
