from typing import Any
import matplotlib.pyplot as plt
from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget, QVBoxLayout, QSpacerItem, QSizePolicy, QHBoxLayout
from PySide6.QtCore import Qt, QCoreApplication
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

from src.worker_node_ui.styles.information.ui_py.information_earnings import UiInformationEarnings
from src.worker_node_ui.components.sidebar.sidebar_panel import Sidebar
from src.worker_node_ui.components.header.toggle_button import ToggleSwitch
from src.worker_node_ui.components.header.profile_button import ProfileButton
from src.worker_node_ui.components.header.notification_button import NotificationHandler
from src.worker_node_ui.components.header.notification_state_manager import NotificationManager
from src.worker_node_ui.components.frame_bar.title_bar import TitleBar
from src.worker_node_ui.components.header.toggle_state_manager import ToggleStateManager


class EarnWindow(QWidget):
    def __init__(self, controller, username, email):
        super().__init__()
        self.controller = controller
        self.username = username
        self.email = email

        self.ui = UiInformationEarnings()
        self.ui.setupUi(self)

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Window)

        self.container_layout = QVBoxLayout(self)
        self.container_layout.setContentsMargins(0, 0, 0, 0)
        self.container_layout.setSpacing(0)
        self.title_bar = TitleBar(self)
        self.container_layout.addWidget(self.title_bar, 0, Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop)

    #components
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

        self.add_chart()

        for label_name, default_text in [
            ("accnum_label", "--"),
            ("avgearning_label", "Average Earning: --"),
            ("wavg_label", "Weekly Average: --"),
            ("earning_label", "PHP --/hr"),
            ("tjexe_label", "Total Jobs Executed: --"),
            ("tearning_label", "Total Earning: --"),
            ("cearning_label", "PHP --"),
            ("etoday_label", "Gaming Today: --"),
            ("ppayouts_label", "Pending payouts: --"),
            ("ajsrate_label", "Average Job Success Rate: --%"),
            ("trevenue_label", "Today's revenue: --"),
            ("yrevenue_label", "Yesterday's revenue: --"),
            ("rweek_label", "Revenue this week: --"),
            ("rlweek_label", "Revenue last week: --"),
            ("lrevenue_label", "Average Lifetime revenue: --")
        ]:
            lbl = getattr(self.ui, label_name, None)
            if lbl:
                lbl.setText(QCoreApplication.translate("earning_dash", default_text, None))

    def update_user_info(self, username, email):
        self.username = username
        self.email = email

    def add_chart(self):
        #mock data
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        values = [5, 3, 6, 2, 7, 4, 5]

        fig, ax = plt.subplots(figsize=(3, 2.5), dpi=100, facecolor='none')
        ax.plot(days, values, color="#7D5FFF", marker='o', linewidth=2)
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set_facecolor('none')
        ax.grid(True, linestyle="--", alpha=0.3)

        canvas = FigureCanvas(fig)
        canvas.setStyleSheet("background: transparent;")
        layout = QVBoxLayout(self.ui.eline_chart)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(canvas)
        self.ui.eline_chart.show()
