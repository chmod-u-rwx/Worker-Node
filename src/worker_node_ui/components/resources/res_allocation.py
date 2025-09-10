import psutil
from PySide6 import QtWidgets

class ResourceAllocation(QtWidgets.QWidget):
    def __init__(self,
                 cpu_slider, cpu_lineedit,
                 cores_slider, cores_lineedit,
                 ram_slider, ram_lineedit,
                 cpu_min_label, cpu_max_label,
                 cores_min_label, cores_max_label,
                 ram_min_label, ram_max_label):
        super().__init__()

        # Assign widgets
        self.cpu_slider = cpu_slider
        self.cpu_lineedit = cpu_lineedit
        self.cores_slider = cores_slider
        self.cores_lineedit = cores_lineedit
        self.ram_slider = ram_slider
        self.ram_lineedit = ram_lineedit

        self.cpu_min_label = cpu_min_label
        self.cpu_max_label = cpu_max_label
        self.cores_min_label = cores_min_label
        self.cores_max_label = cores_max_label
        self.ram_min_label = ram_min_label
        self.ram_max_label = ram_max_label

        # Detect hardware
        self.total_threads = psutil.cpu_count(logical=True) or 1
        self.total_ram = int(psutil.virtual_memory().total / (1024 * 1024))  # MB

        # Setup sliders, labels, and logic
        self.setup_slider_ranges()
        self.setup_logic()

    def setup_slider_ranges(self):
        # CPU
        self.cpu_slider.setRange(1, 100)
        self.cpu_min_label.setText("1")
        self.cpu_max_label.setText("100%")
        self.cpu_max_label.adjustSize()

        # Cores
        self.cores_slider.setRange(1, self.total_threads)
        self.cores_min_label.setText("1")
        self.cores_max_label.setText(str(self.total_threads))
        self.cores_max_label.adjustSize()

        # RAM
        self.ram_slider.setRange(256, self.total_ram)
        self.ram_min_label.setText("256")
        self.ram_max_label.setText(f"{self.total_ram}MB")
        self.ram_max_label.adjustSize()

        # Initialize line edits with current slider values
        self.update_cpu_lineedit(self.cpu_slider.value())
        self.update_cores_lineedit(self.cores_slider.value())
        self.update_ram_lineedit(self.ram_slider.value())

    def setup_logic(self):
        # Slider → LineEdit
        self.cpu_slider.valueChanged.connect(self.update_cpu_lineedit)
        self.cores_slider.valueChanged.connect(self.update_cores_lineedit)
        self.ram_slider.valueChanged.connect(self.update_ram_lineedit)

        # LineEdit → Slider
        self.cpu_lineedit.editingFinished.connect(self.update_cpu_slider)
        self.cores_lineedit.editingFinished.connect(self.update_cores_slider)
        self.ram_lineedit.editingFinished.connect(self.update_ram_slider)

    # === CPU ===
    def update_cpu_lineedit(self, value):
        self.cpu_lineedit.setText(f"{value}%")

    def update_cpu_slider(self):
        try:
            value = int(self.cpu_lineedit.text().replace("%", ""))
            value = max(1, min(100, value))
            self.cpu_slider.setValue(value)
        except ValueError:
            pass

    # === Cores ===
    def update_cores_lineedit(self, value):
        self.cores_lineedit.setText(str(value))

    def update_cores_slider(self):
        try:
            value = int(self.cores_lineedit.text())
            value = max(1, min(self.total_threads, value))
            self.cores_slider.setValue(value)
        except ValueError:
            pass

    # === RAM ===
    def update_ram_lineedit(self, value):
        self.ram_lineedit.setText(f"{value} MB")

    def update_ram_slider(self):
        try:
            value = int(self.ram_lineedit.text().replace("MB", "").strip())
            value = max(256, min(self.total_ram, value))
            self.ram_slider.setValue(value)
        except ValueError:
            pass

    # === Save / Restore Data ===
    def get_data(self):
        return {
            "cpu": self.cpu_slider.value(),
            "cores": self.cores_slider.value(),
            "ram": self.ram_slider.value()
        }

    def set_data(self, data: dict):
        if not data:
            return
        if "cpu" in data:
            self.cpu_slider.setValue(data["cpu"])
        if "cores" in data:
            self.cores_slider.setValue(data["cores"])
        if "ram" in data:
            self.ram_slider.setValue(data["ram"])
