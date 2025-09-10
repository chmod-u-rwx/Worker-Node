from typing import Any
from datetime import date, timedelta
import sys
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QVBoxLayout
from PySide6.QtGui import QIcon, QPainter, QColor, QBrush, QPen
from PySide6.QtCore import Qt, QCoreApplication

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from src.worker_node_ui.styles.info_ui_py.earning_ui import Ui_Earndash
from src.worker_node_ui.components.sidebar.dash_sidebar import Dash_Sidebar
from src.worker_node_ui.components.header.toggle_switch import ToggleSwitch
from src.worker_node_ui.components.header.prof_bt import ProfileButton
from src.worker_node_ui.components.header.notif_wid import NotificationHandler
from src.worker_node_ui.components.frame_bar.title_bar import TitleBar


class EarnDashboard(QMainWindow):
    def __init__(self, controller, username, email):
        super().__init__()
        self.controller = controller
        self.ui = Ui_Earndash()
        self.ui.setupUi(self)

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

        self.add_chart()

        self.ui.accnum_label.setText(QCoreApplication.translate("earning_dash", u"--", None))
        self.ui.avgearning_label.setText(QCoreApplication.translate("earning_dash", u"Average Earning: --", None))
        self.ui.wavg_label.setText(QCoreApplication.translate("earning_dash", u"Weekly Average: --", None))
        self.ui.earning_label.setText(QCoreApplication.translate("earning_dash", u"PHP --/hr", None))
        self.ui.tjexe_label.setText(QCoreApplication.translate("earning_dash", u"Total Jobs Executed: --", None))
        self.ui.tearning_label.setText(QCoreApplication.translate("earning_dash", u"Total Earning: --", None))
        self.ui.avgearning_label.setText(QCoreApplication.translate("earning_dash", u"Average Earning: --", None))
        self.ui.cearning_label.setText(QCoreApplication.translate("earning_dash", u"PHP --", None))
        self.ui.etoday_label.setText(QCoreApplication.translate("earning_dash", u"Gaming Today: --", None))
        self.ui.ppayouts_label.setText(QCoreApplication.translate("earning_dash", u"Pending payouts: --", None))
        self.ui.ajsrate_label.setText(QCoreApplication.translate("earning_dash", u"Average Job Success Rate: --%", None))
        self.ui.trevenue_label.setText(QCoreApplication.translate("earning_dash", u"Today's revenue: --", None))
        self.ui.yrevenue_label.setText(QCoreApplication.translate("earning_dash", u"Yesterday's revenue: --", None))
        self.ui.rweek_label.setText(QCoreApplication.translate("earning_dash", u"revenue this week: --", None))
        self.ui.rlweek_label.setText(QCoreApplication.translate("earning_dash", u"Revenue last week: --", None))
        self.ui.lrevenue_label.setText(QCoreApplication.translate("earning_dash", u"Average Lifetime revenue: --", None))

    def add_chart(self):
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        values = [5, 3, 6, 2, 7, 4, 5]

        eline_fig, eline_ax = plt.subplots(figsize=(3, 2.5), dpi=100, facecolor='none')
        eline_fig.patch.set_alpha(0)
        eline_ax.patch.set_alpha(0)
        eline_ax.plot(days, values, color="#7D5FFF", marker='o', linewidth=2)
        eline_ax.set_facecolor('none')
        eline_ax.grid(True, linestyle="--", alpha=0.3)
        eline_ax.set_xticklabels([])
        eline_ax.set_yticklabels([])

        eline_canvas = FigureCanvas(eline_fig)
        eline_canvas.setStyleSheet("background: transparent;")
        layout_eline = QVBoxLayout(self.ui.eline_chart)
        layout_eline.setContentsMargins(0, 0, 0, 0)
        layout_eline.addWidget(eline_canvas)

        current_fig, current_ax = plt.subplots(figsize=(3, 2.5), dpi=100, facecolor='none')
        current_fig.patch.set_alpha(0)
        current_ax.patch.set_alpha(0)

        values = [5, 3, 6, 2, 7, 4, 5]
        current_ax.fill_between(days, values, color="#7D5FFF", alpha=0.5)
        current_ax.plot(days, values, color="#49067C", linewidth=2)
        current_ax.set_xticklabels([])
        current_ax.set_yticklabels([])
        current_ax.set_facecolor('none')

        current_canvas = FigureCanvas(current_fig)
        current_canvas.setStyleSheet("background: transparent;")
        layout = QVBoxLayout(self.ui.current_chart)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(current_canvas)
        self.ui.current_chart.show()

        tvp_fig, tvp_ax = plt.subplots(figsize=(3, 2.5), dpi=100, facecolor='none')
        tvp_fig.patch.set_alpha(0)
        tvp_ax.patch.set_alpha(0)

        tvp_values = [10, 20, 15, 25, 20, 10]
        colors = ["#7D5FFF", "#49067C", "#D6BDDC", "#4CAF50", "#999ECF", "#795690"]

        tvp_ax.pie(
            tvp_values,
            labels=None,
            colors=colors,
            startangle=90,
            autopct=None,
            wedgeprops={'edgecolor': 'white'}
        )
        tvp_ax.axis('equal')
        tvp_ax.set_facecolor('none')

        tvp_canvas = FigureCanvas(tvp_fig)
        tvp_canvas.setStyleSheet("background: transparent;")
        layout2 = QVBoxLayout(self.ui.tvp_chart)
        layout2.setContentsMargins(0, 0, 0, 0)
        layout2.addWidget(tvp_canvas)
        self.ui.tvp_chart.show()

        revenue_fig, revenue_ax = plt.subplots(figsize=(3, 2.5), dpi=100, facecolor='none')
        revenue_fig.patch.set_alpha(0)
        revenue_ax.patch.set_alpha(0)

        revenue_values = [50, 70, 30, 90, 60]
        revenue_ax.bar(range(len(revenue_values)), revenue_values, color="#7D5FFF")
        revenue_ax.set_xticklabels([])
        revenue_ax.set_yticklabels([])
        revenue_ax.set_facecolor('none')

        revenue_canvas = FigureCanvas(revenue_fig)
        revenue_canvas.setStyleSheet("background: transparent;")
        layout3 = QVBoxLayout(self.ui.revenue_chart)
        layout3.setContentsMargins(0, 0, 0, 0)
        layout3.addWidget(revenue_canvas)
        self.ui.revenue_chart.show()

    def window_buttons(self):
        btn_style = """
            QPushButton {
                background: transparent;
                color: white;
                border: none;
                padding: 5px 10px;
            }
            QPushButton:hover { background: #444444; }
        """

        self.close_btn = QtWidgets.QPushButton("X", self)
        self.close_btn.setGeometry(self.width() - 50, 10, 40, 25)
        self.close_btn.setStyleSheet(btn_style + "QPushButton:hover { background: red; }")
        self.close_btn.clicked.connect(self.close)

        self.fullscreen_btn = QtWidgets.QPushButton("☐", self)
        self.fullscreen_btn.setGeometry(self.width() - 100, 10, 40, 25)
        self.fullscreen_btn.setEnabled(False)
        self.fullscreen_btn.setStyleSheet("""
            QPushButton {
                background: transparent;
                color: gray;
                border: none;
                padding: 5px 10px;
            }
        """)

        self.min_btn = QtWidgets.QPushButton("—", self)
        self.min_btn.setGeometry(self.width() - 150, 10, 40, 25)
        self.min_btn.setStyleSheet(btn_style + "QPushButton:hover { background: #ffbd2e; }")
        self.min_btn.clicked.connect(self.showMinimized)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton and self.drag_pos:
            self.move(self.pos() + event.globalPosition().toPoint() - self.drag_pos)
            self.drag_pos = event.globalPosition().toPoint()
