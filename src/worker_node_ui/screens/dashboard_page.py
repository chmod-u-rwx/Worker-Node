from typing import Any
import sys
from datetime import date, timedelta
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from PySide6 import QtWidgets
from PySide6.QtCore import QRect, QPropertyAnimation, QEasingCurve, Qt, Slot, QAbstractAnimation
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QToolButton, QLabel, QTableWidgetItem, QHeaderView, QVBoxLayout, QSpacerItem, QSizePolicy, QHBoxLayout

from src.worker_node_ui.styles.dashboard.dashboard_page import UiDashboardPage

from src.worker_node_ui.components.sidebar.sidebar_panel import Sidebar
from src.worker_node_ui.components.header.toggle_button import ToggleSwitch
from src.worker_node_ui.components.header.profile_button import ProfileButton
from src.worker_node_ui.components.header.notification_button import NotificationHandler
from src.worker_node_ui.components.header.notification_state_manager import NotificationManager
from src.worker_node_ui.components.frame_bar.title_bar import TitleBar
from src.worker_node_ui.components.header.toggle_state_manager import ToggleStateManager

def set_label_default(label: QLabel, placeholder: str = "--"):
    label.setText(placeholder)

def refresh_table_data(ui):
    new_data = [
        ["a7e6fe9a-9aba-4603-8865-6babb41f8df2", "Success", "12ms", "01/09/2025"],
        ["Job B", "Failed", "8ms", "01/09/2025"],
        ["Job C", "Success", "20ms", "02/09/2025"],
    ]

    ui.hist_table.clearContents()
    ui.hist_table.setRowCount(len(new_data))

    for row, row_data in enumerate(new_data):
        for col, value in enumerate(row_data):
            ui.hist_table.setItem(row, col, QTableWidgetItem(value))

    ui.hist_table.verticalHeader().setVisible(False)
    ui.hist_table.resizeColumnsToContents()
    ui.hist_table.resizeRowsToContents()
    header = ui.hist_table.horizontalHeader()
    header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)


class MainDashboard(QWidget):
    def __init__(self, controller, username, email):
        super().__init__()
        self.controller = controller
        self.username = username
        self.email = email
        self.ui = UiDashboardPage()
        self.ui.setupUi(self)

        self.chart_canvases = []

        self.setWindowIcon(QIcon("src/worker_node_ui/resources/images/desk_logo.png"))
        self.ui.welcome_label.setText(f"Hi {username}, Welcome Back")

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Window)
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        self.title_bar = TitleBar(self)
        self.main_layout.addWidget(self.title_bar, 0, Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight)

        self.sidebar = Sidebar(self.ui, controller)
        self.profile = ProfileButton(self.ui.prof_button, self.controller)
        self.notif_handler = NotificationHandler(self.ui.notif_button, self)
        NotificationManager.add_notification("New job request received!")


        self.ui.toggle_switch.setMinimumSize(100, 35)
        layout = QHBoxLayout(self.ui.toggle_switch)
        layout.setContentsMargins(0, 0, 30, 5)  
        layout.setSpacing(0)
        self.toggle = ToggleSwitch(self.ui.toggle_switch)
        self.toggle.setFixedSize(60, 34)
        self.toggle.setChecked(ToggleStateManager.get_state())
        layout.addWidget(self.toggle, alignment=Qt.AlignmentFlag.AlignRight)

        self.toggle.set_widgets(
            labels=[
                self.ui.rjobs_label,
                self.ui.jslots_label,
                self.ui.jexe_label,
                self.ui.ajob_label,
                self.ui.avgtp_label,
                self.ui.exet_label
            ],
            table=self.ui.hist_table,
            charts=self.chart_canvases,
            update_func=self.update_dashboard
        )
        self._backup_data()

        self.add_charts()
        self._set_default_labels()
        self.ui.refresh_bt.clicked.connect(self.on_refresh_clicked)

    def update_user_info(self, username, email):
        self.username = username
        self.email = email
        self.ui.welcome_label.setText(f"Hi {username}, Welcome Back")

    def update_dashboard(self):
        self._set_default_labels()
        refresh_table_data(self.ui)

    def _backup_data(self):
        self.labels_backup = {
            "rjobs_label": self.ui.rjobs_label.text(),
            "jslots_label": self.ui.jslots_label.text(),
            "jexe_label": self.ui.jexe_label.text(),
            "ajob_label": self.ui.ajob_label.text(),
            "avgtp_label": self.ui.avgtp_label.text(),
            "exet_label": self.ui.exet_label.text()
        }

    def _set_default_labels(self):
        set_label_default(self.ui.rjobs_label, "0")
        set_label_default(self.ui.jslots_label, "--")
        set_label_default(self.ui.jexe_label, "0")
        set_label_default(self.ui.ajob_label, "--")
        self.ui.avgtp_label.setText("Avg Throughput: --")
        self.ui.exet_label.setText("-- days")

    @Slot()
    def on_refresh_clicked(self):
        self._animate_button(self.ui.refresh_bt)
        refresh_table_data(self.ui)

    def _animate_button(self, button: QToolButton):
        geom = button.geometry()
        anim = QPropertyAnimation(button, b"geometry", button)
        anim.setDuration(150)
        anim.setStartValue(geom)
        anim.setKeyValueAt(0.5, QRect(geom.x()-3, geom.y()-3, geom.width()+6, geom.height()+6))
        anim.setEndValue(geom)
        anim.setEasingCurve(QEasingCurve.Type.OutQuad)
        anim.start(QPropertyAnimation.DeletionPolicy.DeleteWhenStopped)

    def add_charts(self):
        cpu_fig, cpu_ax = plt.subplots(figsize=(2.5, 2.5), dpi=100, facecolor='none')
        cpu_fig.patch.set_alpha(0)
        cpu_ax.patch.set_alpha(0)
        used = 30
        cpu_data = [used, 100 - used]
        cpu_ax.pie(cpu_data, startangle=90, colors=["#D6BDDC", "#49067C"],
                   wedgeprops={'width': 0.3, 'edgecolor': 'white'})
        cpu_ax.axis('equal')
        cpu_ax.text(0, 0, f"{used}%", ha='center', va='center', fontsize=12, color='white', fontname="Segoe UI")
        cpu_canvas = FigureCanvas(cpu_fig)
        cpu_canvas.setStyleSheet("background: transparent;")
        layout_cpu = QVBoxLayout(self.ui.cpu_chart)
        layout_cpu.setContentsMargins(0, 0, 0, 0)
        layout_cpu.addWidget(cpu_canvas)
        self.chart_canvases.append(cpu_canvas)

        mem_fig, mem_ax = plt.subplots(figsize=(2.5, 2.5), dpi=100, facecolor='none')
        mem_fig.patch.set_alpha(0)
        mem_ax.patch.set_alpha(0)
        mem_data = [60, 40]
        used = mem_data[0]
        total = sum(mem_data)
        used_percent = round((used / total) * 100)
        mem_ax.pie(mem_data, startangle=90, colors=["#49067C", "#151A20"],
                   wedgeprops={'width': 0.5, 'edgecolor': 'white'})
        mem_ax.axis('equal')
        mem_ax.text(0, 0, f"{used_percent}%", ha='center', va='center', fontsize=12, color='white', fontname="Segoe UI")
        mem_canvas = FigureCanvas(mem_fig)
        mem_canvas.setStyleSheet("background: transparent;")
        layout_mem = QVBoxLayout(self.ui.mem_chart)
        layout_mem.setContentsMargins(0, 0, 0, 0)
        layout_mem.addWidget(mem_canvas)
        self.chart_canvases.append(mem_canvas)

        cache_fig, cache_ax = plt.subplots(figsize=(2.5, 0.4), dpi=100, facecolor='none')
        cache_fig.patch.set_alpha(0)
        cache_ax.patch.set_alpha(0)
        cache_used = 75
        cache_remaining = 100 - cache_used
        cache_ax.barh(["Cache"], [cache_used], color="#7D5FFF", height=0.6,
                      edgecolor="none", align="center", left=0, linewidth=0, zorder=2)
        cache_ax.barh(["Cache"], [cache_remaining], color="#FFE5E8", height=0.6,
                      edgecolor="none", align="center", left=cache_used, linewidth=0, zorder=1)
        cache_ax.set_xlim(0, 100)
        cache_ax.axis("off")
        cache_canvas = FigureCanvas(cache_fig)
        cache_canvas.setStyleSheet("background: transparent;")
        layout_cache = QVBoxLayout(self.ui.cache_chart)
        layout_cache.setContentsMargins(0, 0, 0, 0)
        layout_cache.addWidget(cache_canvas)
        self.chart_canvases.append(cache_canvas)

        rate_fig, rate_ax = plt.subplots(figsize=(2.5, 2), dpi=100, facecolor='none')
        rate_fig.patch.set_alpha(0)
        rate_ax.patch.set_alpha(0)
        time = [1, 2, 3, 4, 5]
        rate = [100, 125, 130, 120, 150]
        rate_ax.plot(time, rate, marker='o', color="#F7B267")
        rate_ax.set_title("Earning Rate", color='white')
        rate_ax.set_facecolor('none')
        rate_ax.tick_params(axis='x', colors='white')
        rate_ax.tick_params(axis='y', colors='white')
        rate_canvas = FigureCanvas(rate_fig)
        rate_canvas.setStyleSheet("background: transparent;")
        layout_rate = QVBoxLayout(self.ui.rate_chart)
        layout_rate.setContentsMargins(0, 0, 0, 0)
        layout_rate.addWidget(rate_canvas)
        self.chart_canvases.append(rate_canvas)

        pass
