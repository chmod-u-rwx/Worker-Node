import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from typing import Any
from datetime import date, datetime, timedelta

from PySide6 import QtWidgets
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, QCoreApplication
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QVBoxLayout

from src.worker_node_ui.styles.info_ui_py.usage_ui import Ui_Usagedash
from src.worker_node_ui.components.sidebar.dash_sidebar import Dash_Sidebar
from src.worker_node_ui.components.header.toggle_switch import ToggleSwitch
from src.worker_node_ui.components.header.prof_bt import ProfileButton
from src.worker_node_ui.components.header.notif_wid import NotificationHandler
from src.worker_node_ui.components.frame_bar.title_bar import TitleBar

class UsageDashboard(QMainWindow):
    def __init__(self, controller, username, email):
        super().__init__()
        self.controller = controller

        self.ui = Ui_Usagedash()
        self.ui.setupUi(self)

        self.setWindowIcon(QIcon("src/worker_node_ui/resources/images/desk_logo.png"))

        self.sidebar = Dash_Sidebar(self.ui, controller)
        self.profile = ProfileButton(self.ui.prof_button, self.controller)
        self.notif_handler = NotificationHandler(self.ui.notif_button, self.centralWidget())
        self.notif_handler.add_notification("New job request received!")

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)
        self.title_bar = TitleBar(self)
        container_layout = QVBoxLayout(self.centralWidget())
        container_layout.setContentsMargins(0, 0, 0, 0)
        container_layout.setSpacing(0)
        container_layout.addWidget(self.title_bar, 0, Qt.AlignRight | Qt.AlignTop)

        # Toggle switch
        self.ui.toggle_switch.setMinimumSize(60, 34)
        self.toggle = ToggleSwitch(self.ui.toggle_switch)
        self.toggle.setFixedSize(60, 34)
        self.toggle.setChecked(True)
        layout = QVBoxLayout(self.ui.toggle_switch)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.toggle)

        self.add_chart()

    def add_chart(self):
        cpu_fig, cpu_ax = plt.subplots(figsize=(2.5, 2.5), dpi=100, facecolor='none')
        cpu_fig.patch.set_alpha(0)
        cpu_ax.patch.set_alpha(0)

        used = 30
        cpu_data = [used, 100 - used]

        cpu_ax.pie(
            cpu_data,
            startangle=90,
            colors=["#D6BDDC", "#49067C"],
            wedgeprops={'width': 0.3, 'edgecolor': 'white'}
        )
        cpu_ax.axis('equal')
        cpu_ax.set_facecolor('none')
        cpu_ax.text(0, 0, f"{used}%", ha='center', va='center',
                    fontsize=12, color='white', fontname="Segoe UI")

        cpu_canvas = FigureCanvas(cpu_fig)
        cpu_canvas.setStyleSheet("background: transparent;")
        layout_cpu = QVBoxLayout(self.ui.cpu_chart)
        layout_cpu.setContentsMargins(0, 0, 0, 0)
        layout_cpu.addWidget(cpu_canvas)

        mem_fig, mem_ax = plt.subplots(figsize=(2.5, 2.5), dpi=100, facecolor='none')
        mem_fig.patch.set_alpha(0)
        mem_ax.patch.set_alpha(0)

        mem_data = [60, 40]
        used_percent = round((mem_data[0] / sum(mem_data)) * 100)

        mem_ax.pie(
            mem_data,
            startangle=90,
            colors=["#49067C", "#151A20"],
            wedgeprops={'width': 0.5, 'edgecolor': 'white'}
        )
        mem_ax.axis('equal')
        mem_ax.set_facecolor('none')
        mem_ax.text(0, 0, f"{used_percent}%",
                    ha='center', va='center',
                    fontsize=12, color='white', fontname="Segoe UI")

        mem_canvas = FigureCanvas(mem_fig)
        mem_canvas.setStyleSheet("background: transparent;")
        layout_mem = QVBoxLayout(self.ui.mem_chart)
        layout_mem.setContentsMargins(0, 0, 0, 0)
        layout_mem.addWidget(mem_canvas)

        cache_fig, cache_ax = plt.subplots(figsize=(2.5, 0.4), dpi=100, facecolor='none')
        cache_fig.patch.set_alpha(0)
        cache_ax.patch.set_alpha(0)

        cache_used = 75
        cache_ax.barh(["Cache"], [cache_used], color="#7D5FFF", height=0.6, zorder=2)
        cache_ax.barh(["Cache"], [100 - cache_used], color="#FFE5E8", height=0.6,
                      left=cache_used, zorder=1)

        cache_ax.set_xlim(0, 100)
        cache_ax.axis("off")
        cache_ax.set_facecolor("none")

        cache_canvas = FigureCanvas(cache_fig)
        cache_canvas.setStyleSheet("background: transparent;")
        layout_cache = QVBoxLayout(self.ui.cache_chart)
        layout_cache.setContentsMargins(0, 0, 0, 0)
        layout_cache.addWidget(cache_canvas)

        trend_values = [20, 25, 30, 28, 35, 40, 50]
        hour_labels = ["1hr", "2hr", "3hr", "4hr", "5hr", "6hr", "7hr"]

        trend_fig, trend_ax = plt.subplots(figsize=(5, 2.5), dpi=100, facecolor='none')
        trend_fig.patch.set_alpha(0)
        trend_ax.patch.set_alpha(0)

        trend_ax.plot(hour_labels, trend_values, color="#9C7DFF", marker='o', linewidth=2)
        trend_ax.set_yticks([0, 25, 50, 75])
        trend_ax.grid(True, linestyle="--", alpha=0.3)
        trend_ax.spines['top'].set_visible(False)
        trend_ax.spines['right'].set_visible(False)
        trend_ax.spines['bottom'].set_color('white')
        trend_ax.spines['left'].set_color('white')

        plt.tight_layout()

        trend_canvas = FigureCanvas(trend_fig)
        trend_canvas.setStyleSheet("background: transparent;")

        layout_trend = QVBoxLayout(self.ui.trend_chart)
        layout_trend.setContentsMargins(0, 0, 0, 0)
        for i in reversed(range(layout_trend.count())):
            layout_trend.itemAt(i).widget().setParent(None)
        layout_trend.addWidget(trend_canvas)

        self.ui.memcon_label.setText(QCoreApplication.translate("usage_dash", "Memory Consumed: --"))
        self.ui.cputime_label.setText(QCoreApplication.translate("usage_dash", "CPU Time Used: --"))
        self.ui.cachecon_label.setText(QCoreApplication.translate("usage_dash", "Cache Consumed: --"))

        table = self.ui.history_table
        table.verticalHeader().setVisible(False)
        dummy_vms = [
            {"vm_name": "VM1", "cpu_avg": 20, "cpu_peak": 40, "mem_used": 512, "mem_total": 2048,
             "cache_used": 102, "cache_total": 2048, "status": "Running"},
            {"vm_name": "VM2", "cpu_avg": 35, "cpu_peak": 60, "mem_used": 1024, "mem_total": 2048,
             "cache_used": 500, "cache_total": 2048, "status": "Stopped"},
            {"vm_name": "VM3", "cpu_avg": 50, "cpu_peak": 75, "mem_used": 1536, "mem_total": 2048,
             "cache_used": 1024, "cache_total": 2048, "status": "Running"},
        ]

        table.setRowCount(len(dummy_vms))
        for row, vm in enumerate(dummy_vms):
            table.setItem(row, 0, QTableWidgetItem(vm["vm_name"]))
            table.setItem(row, 1, QTableWidgetItem(str(vm["cpu_avg"])))
            table.setItem(row, 2, QTableWidgetItem(str(vm["cpu_peak"])))
            table.setItem(row, 3, QTableWidgetItem(f"{vm['mem_used']} / {vm['mem_total']}"))
            table.setItem(row, 4, QTableWidgetItem(f"{vm['cache_used']} / {vm['cache_total']}"))
            table.setItem(row, 5, QTableWidgetItem(vm["status"]))
            for col in range(1, 6):
                table.item(row, col).setTextAlignment(Qt.AlignCenter)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton and self.drag_pos:
            self.move(self.pos() + event.globalPosition().toPoint() - self.drag_pos)
            self.drag_pos = event.globalPosition().toPoint()

