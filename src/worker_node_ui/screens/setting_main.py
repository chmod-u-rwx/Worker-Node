from PySide6.QtWidgets import QWidget, QVBoxLayout, QMessageBox
from PySide6 import QtGui, QtCore

from src.worker_node_ui.styles.settings.ui_py.setting_main import UiMainSetting
from src.worker_node_ui.components.resources.res_allocation import ResourceAllocation
from src.worker_node_ui.components.resources.disk_cache import DiskCache

class MainSetting(QWidget):
    def __init__(self, controller, parent=None):
        super().__init__(parent)
        self.controller = controller
        self.ui = UiMainSetting()
        self.ui.setupUi(self)

        self.setWindowFlags(
            QtCore.Qt.WindowType.FramelessWindowHint | QtCore.Qt.WindowType.WindowStaysOnTopHint | QtCore.Qt.WindowType.Dialog)
        self.setStyleSheet("background-color: #0A0A2A; color: white;")

        wrapper_layout = QVBoxLayout(self)
        wrapper_layout.addWidget(self.ui.set_con)
        wrapper_layout.setContentsMargins(15, 15, 15, 15)
        wrapper_layout.setSpacing(15)
        self.setFixedSize(self.size())

        # Fetch from signup
        self.resource_config = ResourceAllocation(
            cpu_slider=self.ui.cpu_slider,
            cpu_lineedit=self.ui.cpu_lineedit,
            cores_slider=self.ui.cores_slider,
            cores_lineedit=self.ui.core_lineedit,
            ram_slider=self.ui.ram_slider,
            ram_lineedit=self.ui.ram_lineedit,
            cpu_min_label=self.ui.cpu_min_label,
            cpu_max_label=self.ui.cpu_max_label,
            cores_min_label=self.ui.core_min_label,
            cores_max_label=self.ui.core_max_label_,
            ram_min_label=self.ui.ram_min_label,
            ram_max_label=self.ui.ram_max_label
        )

        self.disk_widget = DiskCache(
            disk_slider=self.ui.cache_slider,
            disk_lineedit=self.ui.cache_lineedit_2,
            cores_min_label=self.ui.cache_min_label,
            cores_max_label=self.ui.cache_max_label,
            cache_lineedit=self.ui.cache_lineedit,
            browse_button=self.ui.clearc_bt_2
        )

        if self.controller.user_resource:
            self.resource_config.set_data(self.controller.user_resource)
            self.disk_widget.set_data(self.controller.user_resource)

        # Settings Navigation Buttons
        self.ui.schanges_bt.clicked.connect(self.handle_save)
        self.ui.cancel_bt.clicked.connect(self.close)
        self.ui.logout_bt.clicked.connect(self.handle_logout)
        self.ui.clearc_bt.clicked.connect(self.handle_clear_cache)
        self.ui.eprofile_bt.clicked.connect(self.open_edit_profile)

    def open_edit_profile(self):
        if self.controller:
            self.hide() 
            self.controller.show_profile_settings()

    def handle_save(self):
        data = self.resource_config.get_data()
        data.update(self.disk_widget.get_data())
        self.controller.user_resource = data
        QMessageBox.information(self, "Saved", "Settings updated successfully.")

    def handle_logout(self):
        reply = QMessageBox.question(
            self,
            "Confirm Logout",
            "Are you sure you want to log out?",
            QMessageBox.Yes | QMessageBox.No, #type: ignore
            QMessageBox.No #type: ignore
        )
        if reply == QMessageBox.Yes: #type: ignore
            self.close()
            self.controller.show_login()

    def handle_clear_cache(self):
        self.ui.cache_lineedit.clear()
        self.ui.cache_lineedit_2.clear()
        QMessageBox.information(self, "Cleared", "Cache cleared successfully.")
