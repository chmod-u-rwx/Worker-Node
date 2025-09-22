from typing import Any
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHeaderView, QSpacerItem, QSizePolicy, QHBoxLayout
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt, QCoreApplication

from src.worker_node_ui.styles.information.ui_py.information_jobs import UiInformatioJobs
from src.worker_node_ui.components.sidebar.sidebar_panel import Sidebar
from src.worker_node_ui.components.header.toggle_button import ToggleSwitch
from src.worker_node_ui.components.header.profile_button import ProfileButton
from src.worker_node_ui.components.header.notification_button import NotificationHandler
from src.worker_node_ui.components.header.notification_state_manager import NotificationManager
from src.worker_node_ui.components.frame_bar.title_bar import TitleBar
from src.worker_node_ui.components.header.toggle_state_manager import ToggleStateManager


class JobWindow(QWidget):
    def __init__(self, controller, username, email):
        super().__init__()
        self.controller = controller
        self.username = username
        self.email = email

        self.ui = UiInformatioJobs()
        self.ui.setupUi(self)

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Window)

        self.container_layout = QVBoxLayout(self)
        self.container_layout.setContentsMargins(0, 0, 0, 0)
        self.container_layout.setSpacing(0)
        self.title_bar = TitleBar(self)
        self.container_layout.addWidget(self.title_bar, 0, Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop)

    # components
        self.sidebar = Sidebar(self.ui, controller)
        self.profile = ProfileButton(self.ui.prof_button, controller)
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

        self.plot_throughput_trend()

        for label_name, default_text in [
            ("avg_label", "Average in 24h: --"),
            ("highest_label", "Highest: --"),
            ("lowest_label", "Cache Consumed: --"),
            ("sys_label", "System capacity: --"),
            ("tsavail_label", "Total slots available: --"),
            ("scurrently_label", "Slots currently in use: --"),
            ("nodeA_label", "Node A: --"),
            ("nodeB_label", "Node B: --"),
            ("nodeC_label", "Node C: --"),
            ("today_label", "Today: --"),
            ("yesterday_label", "Yesterday: --"),
            ("tweek_label", "This week: --"),
            ("lweek_label", "Last week: --"),
            ("currently_label", "Currently: --"),
            ("pload_label", "Peak Load: --"),
            ("lload_label", "Lowest Load: --")
        ]:
            lbl = getattr(self.ui, label_name, None)
            if lbl:
                lbl.setText(QCoreApplication.translate("job_dash", default_text, None))

    def update_user_info(self, username, email):
        self.username = username
        self.email = email

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
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            model.appendRow(row_items)

        table.setModel(model)
        table.verticalHeader().setVisible(False)
        table.horizontalHeader().setStretchLastSection(True)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
