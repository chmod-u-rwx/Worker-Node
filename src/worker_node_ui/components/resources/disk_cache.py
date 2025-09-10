import psutil
from PySide6 import QtWidgets
from PySide6.QtWidgets import QFileDialog


class DiskCache(QtWidgets.QWidget):
    def __init__(self,
                 disk_slider, disk_lineedit,
                 cores_min_label, cores_max_label,
                 cache_lineedit, browse_button,
                 disk_min=0, disk_max=None):
        super().__init__()

        # Assign widgets
        self.disk_slider = disk_slider
        self.disk_lineedit = disk_lineedit
        self.cores_min_label = cores_min_label
        self.cores_max_label = cores_max_label
        self.cache_lineedit = cache_lineedit
        self.browse_button = browse_button

        # Set disk limits
        self.disk_min = disk_min
        self.disk_max = disk_max or (psutil.disk_usage("/").total // (1024**2))  # in MB

        # Setup slider, labels, lineedit, and logic
        self.setup_slider_range()
        self.setup_logic()

    # ----------------------------
    # Setup
    # ----------------------------
    def setup_slider_range(self):
        self.disk_slider.setRange(self.disk_min, self.disk_max)
        self.cores_min_label.setText(f"{self.disk_min}MB")
        self.cores_max_label.setText(f"{self.disk_max}MB")
        self.cores_max_label.adjustSize()

        # initialize lineedit with current slider value
        self.disk_slider.setValue(min(1024, self.disk_max // 10))
        self.disk_lineedit.setText(str(self.disk_slider.value()))

    def setup_logic(self):
        # Slider → LineEdit
        self.disk_slider.valueChanged.connect(self.update_disk_lineedit)
        # LineEdit → Slider
        self.disk_lineedit.editingFinished.connect(self.update_disk_slider)
        # Browse button
        self.browse_button.clicked.connect(self.select_cache_path)

    # ----------------------------
    # Slider ↔ LineEdit
    # ----------------------------
    def update_disk_lineedit(self, value):
        self.disk_lineedit.setText(str(value))

    def update_disk_slider(self):
        try:
            value = int(self.disk_lineedit.text())
            value = max(self.disk_min, min(self.disk_max, value))
            self.disk_slider.setValue(value)
        except ValueError:
            pass

    def select_cache_path(self):
        folder = QFileDialog.getExistingDirectory(self)
        if folder:
            self.cache_lineedit.setText(folder)

    # ----------------------------
    # Get / Set Data
    # ----------------------------
    def get_data(self):
        return {
            "cache_path": self.cache_lineedit.text().strip(),
            "disk_mb": self.disk_slider.value()
        }

    def set_data(self, data: dict):
        if not data:
            return
        if "cache_path" in data:
            self.cache_lineedit.setText(data["cache_path"])
        if "disk_mb" in data:
            value = max(self.disk_min, min(self.disk_max, data["disk_mb"]))
            self.disk_slider.setValue(value)
            self.disk_lineedit.setText(str(value))
