
import sys
from datetime import date, timedelta
from typing import Any
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib import patches
from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QHeaderView, QVBoxLayout
from PySide6.QtGui import QIcon, QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt, QCoreApplication

from src.worker_node_ui.styles.info_ui_py.job_ui import Ui_Jobdash
from src.worker_node_ui.components.sidebar.dash_sidebar import Dash_Sidebar
from src.worker_node_ui.components.header.toggle_switch import ToggleSwitch
from src.worker_node_ui.components.header.prof_bt import ProfileButton
from src.worker_node_ui.components.header.notif_wid import NotificationHandler
from src.worker_node_ui.components.frame_bar.title_bar import TitleBar

class JobDashboard(QMainWindow):
    def __init__(self, controller, username, email):
        super().__init__()
        self.controller = controller
        self.ui = Ui_Jobdash()
        self.ui.setupUi(self)

        self.setWindowIcon(QIcon("src/worker_node_ui/resources/images/desk_logo.png"))

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)
        self.title_bar = TitleBar(self)
        container_layout = QVBoxLayout(self.centralWidget())
        container_layout.setContentsMargins(0, 0, 0, 0)
        container_layout.setSpacing(0)
        container_layout.addWidget(self.title_bar, 0, Qt.AlignRight | Qt.AlignTop)

        self.sidebar = Dash_Sidebar(self.ui, controller)
        self.profile = ProfileButton(self.ui.prof_button, self.controller)
        self.notif_handler = NotificationHandler(self.ui.notif_button, self.centralWidget())
        self.notif_handler.add_notification("New job request received!")

        # Toggle switch
        self.ui.toggle_switch.setMinimumSize(60, 34)
        self.toggle = ToggleSwitch(self.ui.toggle_switch)
        self.toggle.setFixedSize(60, 34)
        self.toggle.setChecked(True)
        layout = QVBoxLayout(self.ui.toggle_switch)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.toggle)

        self.plot_throughput_trend()

    def plot_throughput_trend(self):
        hours = ["1hr", "2hr", "3hr", "4hr", "5hr", "6hr", "7hr"]
        throughput = [50, 70, 65, 80, 60, 75, 90]
        avg_throughput = [55, 68, 63, 77, 62, 70, 85]

        fig, ax = plt.subplots(figsize=(6.5, 2.7), dpi=100, facecolor='none')
        fig.patch.set_alpha(0)
        ax.patch.set_alpha(0)

        ax.bar(hours, throughput, color="#49067C", alpha=0.6)
        ax.plot(hours, avg_throughput, color="#ffffff", marker='o', linewidth=2)

        ax.set_facecolor("none")
        ax.grid(True, linestyle="--", alpha=0.3)
        ax.set_ylabel("Value", color="white")
        ax.set_xlabel("Time", color="white")
        ax.tick_params(axis='x', colors='white')
        ax.tick_params(axis='y', colors='white')
        ax.spines['bottom'].set_color('white')
        ax.spines['left'].set_color('white')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.legend(facecolor='none', edgecolor='white', labelcolor='white')
        plt.tight_layout()

        canvas = FigureCanvas(fig)
        canvas.setStyleSheet("background: transparent;")
        layout = QVBoxLayout(self.ui.ttrend_chart)
        layout.setContentsMargins(0, 0, 0, 0)

        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().setParent(None)
        layout.addWidget(canvas)

        self.ui.avg_label.setText(QCoreApplication.translate("job_dash", u"Average in 24h: --", None))
        self.ui.highest_label.setText(QCoreApplication.translate("job_dash", u"Highest: --", None))
        self.ui.lowest_label.setText(QCoreApplication.translate("job_dash", u"Cache Consumed: --", None))
        self.ui.sys_label.setText(QCoreApplication.translate("job_dash", u"System capacity: --", None))
        self.ui.tsavail_label.setText(QCoreApplication.translate("job_dash", u"Total slots available: --", None))
        self.ui.scurrently_label.setText(QCoreApplication.translate("job_dash", u"Slots currently in use: --", None))
        self.ui.nodeA_label.setText(QCoreApplication.translate("job_dash", u"Node A: --", None))
        self.ui.nodeB_label.setText(QCoreApplication.translate("job_dash", u"Node B: --", None))
        self.ui.nodeC_label.setText(QCoreApplication.translate("job_dash", u"Node C: --", None))
        self.ui.today_label.setText(QCoreApplication.translate("job_dash", u"Today: --", None))
        self.ui.yesterday_label.setText(QCoreApplication.translate("job_dash", u"Yesterday: --", None))
        self.ui.tweek_label.setText(QCoreApplication.translate("job_dash", u"This week: --", None))
        self.ui.lweek_label.setText(QCoreApplication.translate("job_dash", u"Last week: --", None))
        self.ui.currently_label.setText(QCoreApplication.translate("job_dash", u"Currently: --", None))
        self.ui.pload_label.setText(QCoreApplication.translate("job_dash", u"Peak Load: --", None))
        self.ui.lload_label.setText(QCoreApplication.translate("job_dash", u"Lowest Load: --", None))

        self._populate_table(
            self.ui.crjobs_tview,
            [{"job_id": "JOB123", "status": "Running", "start_time": "2025-09-06 14:00",
              "duration": "00:45:00", "node": "Node-1", "slots": 4, "result": "--"}]
        )

        self._populate_table(
            self.ui.jhis_tview,
            [{"job_id": "JOB122", "status": "Completed", "start_time": "2025-09-05 10:00",
              "duration": "01:15:00", "node": "Node-2", "slots": 2, "result": "Success"}]
        )

    def _populate_table(self, table, jobs):
        columns = ["Job ID", "Status", "Start Time", "Duration", "Node", "Slots", "Result"]
        model = QStandardItemModel(0, len(columns))
        model.setHorizontalHeaderLabels(columns)

        for job in jobs:
            row_items = [
                QStandardItem(job["job_id"]),
                QStandardItem(job["status"]),
                QStandardItem(job["start_time"]),
                QStandardItem(job["duration"]),
                QStandardItem(job["node"]),
                QStandardItem(str(job["slots"])),
                QStandardItem(job["result"])
            ]
            for item in row_items[1:]:
                item.setTextAlignment(Qt.AlignCenter)
            model.appendRow(row_items)

        table.setModel(model)
        table.verticalHeader().setVisible(False)
        table.horizontalHeader().setStretchLastSection(True)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton and self.drag_pos:
            self.move(self.pos() + event.globalPosition().toPoint() - self.drag_pos)
            self.drag_pos = event.globalPosition().toPoint()
