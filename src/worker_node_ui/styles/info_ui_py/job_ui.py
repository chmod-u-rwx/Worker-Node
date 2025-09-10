# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'jobs_info.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QSizePolicy, QTableView, QToolButton,
    QVBoxLayout, QWidget)

class Ui_Jobdash(object):
    def setupUi(self, jobs_dash):
        if not jobs_dash.objectName():
            jobs_dash.setObjectName(u"jobs_dash")
        jobs_dash.resize(1440, 810)
        jobs_dash.setMinimumSize(QSize(1440, 810))
        jobs_dash.setMaximumSize(QSize(1440, 810))
        self.centralwidget = QWidget(jobs_dash)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMinimumSize(QSize(1440, 810))
        self.centralwidget.setMaximumSize(QSize(1440, 810))
        self.centralwidget.setStyleSheet("background-image: url('src/worker_node_ui/resources/images/jobs_bg.png');")

        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 2, 2))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(30, 50, 52, 41))
        self.logo.setAutoFillBackground(False)
        self.logo.setStyleSheet(u"background: transparent;")
        self.logo.setPixmap(QPixmap("src/worker_node_ui/resources/images/signup1logo.png"))
        self.logo.setScaledContents(True)
        self.thru_trend = QLabel(self.centralwidget)
        self.thru_trend.setObjectName(u"thru_trend")
        self.thru_trend.setGeometry(QRect(120, 130, 141, 31))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(11)
        font1.setBold(False)
        self.thru_trend.setFont(font1)
        self.thru_trend.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.ttrend_con = QLabel(self.centralwidget)
        self.ttrend_con.setObjectName(u"ttrend_con")
        self.ttrend_con.setGeometry(QRect(100, 120, 658, 271))
        self.ttrend_con.setStyleSheet(u"QLabel {\n"
"	background-color: rgba(20, 20, 50, 10);\n"
"    border: 1px solid rgba(255, 255, 255, 0.3);\n"
"    border-radius: 35px;\n"
"    padding: 8px;\n"
"    color: white;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"QLabel:focus {\n"
"    border: 1px solid #7D5FFF;\n"
"    box-shadow: 0px 0px 8px #7D5FFF;\n"
"}\n"
"")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 120, 43, 301))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayoutWidget.setStyleSheet("background: transparent;")
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.dash_bt = QToolButton(self.verticalLayoutWidget)
        self.dash_bt.setObjectName(u"dash_bt")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(15)
        sizePolicy.setVerticalStretch(15)
        sizePolicy.setHeightForWidth(self.dash_bt.sizePolicy().hasHeightForWidth())
        self.dash_bt.setSizePolicy(sizePolicy)
        self.dash_bt.setStyleSheet(u"background: transparent;")
        icon = QIcon()
        icon.addFile(u"src/worker_node_ui/resources/fbuttons/dashboard.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.dash_bt.setIcon(icon)
        self.dash_bt.setIconSize(QSize(31, 41))

        self.verticalLayout.addWidget(self.dash_bt)

        self.sys_bt = QToolButton(self.verticalLayoutWidget)
        self.sys_bt.setObjectName(u"sys_bt")
        sizePolicy.setHeightForWidth(self.sys_bt.sizePolicy().hasHeightForWidth())
        self.sys_bt.setSizePolicy(sizePolicy)
        self.sys_bt.setStyleSheet(u"background: transparent;")
        icon1 = QIcon()
        icon1.addFile(u"src/worker_node_ui/resources/fbuttons/system.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.sys_bt.setIcon(icon1)
        self.sys_bt.setIconSize(QSize(31, 41))

        self.verticalLayout.addWidget(self.sys_bt)

        self.job_bt = QToolButton(self.verticalLayoutWidget)
        self.job_bt.setObjectName(u"job_bt")
        sizePolicy.setHeightForWidth(self.job_bt.sizePolicy().hasHeightForWidth())
        self.job_bt.setSizePolicy(sizePolicy)
        self.job_bt.setStyleSheet(u"background: transparent;")
        icon2 = QIcon()
        icon2.addFile(u"src/worker_node_ui/resources/fbuttons/jobs.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.job_bt.setIcon(icon2)
        self.job_bt.setIconSize(QSize(31, 41))

        self.verticalLayout.addWidget(self.job_bt)

        self.earning_bt = QToolButton(self.verticalLayoutWidget)
        self.earning_bt.setObjectName(u"earning_bt")
        sizePolicy.setHeightForWidth(self.earning_bt.sizePolicy().hasHeightForWidth())
        self.earning_bt.setSizePolicy(sizePolicy)
        self.earning_bt.setStyleSheet(u"background: transparent;")
        icon3 = QIcon()
        icon3.addFile(u"src/worker_node_ui/resources/fbuttons/earnings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.earning_bt.setIcon(icon3)
        self.earning_bt.setIconSize(QSize(31, 41))

        self.verticalLayout.addWidget(self.earning_bt)

        self.settings_bt = QToolButton(self.centralwidget)
        self.settings_bt.setObjectName(u"settings_bt")
        self.settings_bt.setGeometry(QRect(30, 740, 51, 50))
        sizePolicy.setHeightForWidth(self.settings_bt.sizePolicy().hasHeightForWidth())
        self.settings_bt.setSizePolicy(sizePolicy)
        self.settings_bt.setStyleSheet(u"QToolButton {\n"
"    background: transparent;       /* no fill */\n"
"    color: white;                  /* icon/text color */\n"
"    border: 1px solid #ffffff;     /* white border */\n"
"    border-radius: 25px;           /* make it round (half of width/height) */\n"
"    padding: 3px;                  /* space inside */\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"src/worker_node_ui/resources/fbuttons/settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settings_bt.setIcon(icon4)
        self.settings_bt.setIconSize(QSize(35, 35))
        self.ttrend_chart = QWidget(self.centralwidget)
        self.ttrend_chart.setObjectName(u"ttrend_chart")
        self.ttrend_chart.setGeometry(QRect(370, 150, 361, 211))
        self.ttrend_chart.setStyleSheet(u"background: transparent;")
        self.prof_button = QToolButton(self.centralwidget)
        self.prof_button.setObjectName(u"prof_button")
        self.prof_button.setGeometry(QRect(1320, 50, 51, 50))
        sizePolicy.setHeightForWidth(self.prof_button.sizePolicy().hasHeightForWidth())
        self.prof_button.setSizePolicy(sizePolicy)
        self.prof_button.setStyleSheet(u"QToolButton {\n"
"    background: transparent;       /* no fill */\n"
"    color: white;                  /* icon/text color */\n"
"    border: 1px solid #ffffff;     /* white border */\n"
"    border-radius: 25px;           /* make it round (half of width/height) */\n"
"    padding: 3px;                  /* space inside */\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u"src/worker_node_ui/resources/fbuttons/Profile.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.prof_button.setIcon(icon5)
        self.prof_button.setIconSize(QSize(35, 35))
        self.notif_button = QToolButton(self.centralwidget)
        self.notif_button.setObjectName(u"notif_button")
        self.notif_button.setGeometry(QRect(1250, 50, 51, 50))
        sizePolicy.setHeightForWidth(self.notif_button.sizePolicy().hasHeightForWidth())
        self.notif_button.setSizePolicy(sizePolicy)
        self.notif_button.setStyleSheet(u"QToolButton {\n"
"    background: transparent;       /* no fill */\n"
"    color: white;                  /* icon/text color */\n"
"    border: 1px solid #ffffff;     /* white border */\n"
"    border-radius: 25px;           /* make it round (half of width/height) */\n"
"    padding: 3px;                  /* space inside */\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u"src/worker_node_ui/resources/fbuttons/Notification.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.notif_button.setIcon(icon6)
        self.notif_button.setIconSize(QSize(35, 35))
        self.toggle_switch = QWidget(self.centralwidget)
        self.toggle_switch.setObjectName(u"toggle_switch")
        self.toggle_switch.setGeometry(QRect(1158, 56, 91, 21))
        self.toggle_switch.setStyleSheet(u"background: transparent;\n"
"")
        self.workerM_label = QLabel(self.centralwidget)
        self.workerM_label.setObjectName(u"workerM_label")
        self.workerM_label.setGeometry(QRect(1150, 90, 81, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(9)
        font2.setBold(False)
        self.workerM_label.setFont(font2)
        self.workerM_label.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.scurrently_label = QLabel(self.centralwidget)
        self.scurrently_label.setObjectName(u"scurrently_label")
        self.scurrently_label.setGeometry(QRect(800, 190, 131, 16))
        self.scurrently_label.setFont(font2)
        self.scurrently_label.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.tsavail_label = QLabel(self.centralwidget)
        self.tsavail_label.setObjectName(u"tsavail_label")
        self.tsavail_label.setGeometry(QRect(800, 170, 131, 16))
        self.tsavail_label.setFont(font2)
        self.tsavail_label.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.sutilization_con = QLabel(self.centralwidget)
        self.sutilization_con.setObjectName(u"sutilization_con")
        self.sutilization_con.setGeometry(QRect(773, 120, 251, 271))
        self.sutilization_con.setStyleSheet(u"QLabel {\n"
"	background-color: rgba(20, 20, 50, 10);\n"
"    border: 1px solid rgba(255, 255, 255, 0.3);\n"
"    border-radius: 35px;\n"
"    padding: 8px;\n"
"    color: white;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"QLabel:focus {\n"
"    border: 1px solid #7D5FFF;\n"
"    box-shadow: 0px 0px 8px #7D5FFF;\n"
"}\n"
"")
        self.avg_label = QLabel(self.centralwidget)
        self.avg_label.setObjectName(u"avg_label")
        self.avg_label.setGeometry(QRect(120, 180, 151, 20))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        self.avg_label.setFont(font3)
        self.avg_label.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.highest_label = QLabel(self.centralwidget)
        self.highest_label.setObjectName(u"highest_label")
        self.highest_label.setGeometry(QRect(120, 200, 151, 21))
        self.highest_label.setFont(font3)
        self.highest_label.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.slots_util = QLabel(self.centralwidget)
        self.slots_util.setObjectName(u"slots_util")
        self.slots_util.setGeometry(QRect(800, 130, 141, 31))
        self.slots_util.setFont(font1)
        self.slots_util.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.lowest_label = QLabel(self.centralwidget)
        self.lowest_label.setObjectName(u"lowest_label")
        self.lowest_label.setGeometry(QRect(120, 220, 151, 21))
        self.lowest_label.setFont(font3)
        self.lowest_label.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.sys_label = QLabel(self.centralwidget)
        self.sys_label.setObjectName(u"sys_label")
        self.sys_label.setGeometry(QRect(120, 240, 151, 21))
        self.sys_label.setFont(font3)
        self.sys_label.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.nodeA_label = QLabel(self.centralwidget)
        self.nodeA_label.setObjectName(u"nodeA_label")
        self.nodeA_label.setGeometry(QRect(800, 230, 131, 16))
        self.nodeA_label.setFont(font2)
        self.nodeA_label.setStyleSheet(u"color: #a2a1a1;\n"
"background: transparent;\n"
"\n"
"")
        self.nodeB_label = QLabel(self.centralwidget)
        self.nodeB_label.setObjectName(u"nodeB_label")
        self.nodeB_label.setGeometry(QRect(800, 250, 131, 16))
        self.nodeB_label.setFont(font2)
        self.nodeB_label.setStyleSheet(u"color: #a2a1a1;\n"
"background: transparent;\n"
"\n"
"")
        self.nodeC_label = QLabel(self.centralwidget)
        self.nodeC_label.setObjectName(u"nodeC_label")
        self.nodeC_label.setGeometry(QRect(800, 270, 131, 16))
        self.nodeC_label.setFont(font2)
        self.nodeC_label.setStyleSheet(u"color: #a2a1a1;\n"
"background: transparent;\n"
"\n"
"")
        self.tstats_con = QLabel(self.centralwidget)
        self.tstats_con.setObjectName(u"tstats_con")
        self.tstats_con.setGeometry(QRect(1040, 120, 371, 271))
        self.tstats_con.setStyleSheet(u"QLabel {\n"
"	background-color: rgba(20, 20, 50, 10);\n"
"    border: 1px solid rgba(255, 255, 255, 0.3);\n"
"    border-radius: 35px;\n"
"    padding: 8px;\n"
"    color: white;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"QLabel:focus {\n"
"    border: 1px solid #7D5FFF;\n"
"    box-shadow: 0px 0px 8px #7D5FFF;\n"
"}\n"
"")
        self.t_statistics = QLabel(self.centralwidget)
        self.t_statistics.setObjectName(u"t_statistics")
        self.t_statistics.setGeometry(QRect(1060, 130, 141, 31))
        self.t_statistics.setFont(font1)
        self.t_statistics.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.today_label = QLabel(self.centralwidget)
        self.today_label.setObjectName(u"today_label")
        self.today_label.setGeometry(QRect(1060, 170, 151, 16))
        self.today_label.setFont(font2)
        self.today_label.setStyleSheet(u"color: #a2a1a1;\n"
"background: transparent;\n"
"\n"
"")
        self.yesterday_label = QLabel(self.centralwidget)
        self.yesterday_label.setObjectName(u"yesterday_label")
        self.yesterday_label.setGeometry(QRect(1060, 190, 171, 16))
        self.yesterday_label.setFont(font2)
        self.yesterday_label.setStyleSheet(u"color: #a2a1a1;\n"
"background: transparent;\n"
"")
        self.tweek_label = QLabel(self.centralwidget)
        self.tweek_label.setObjectName(u"tweek_label")
        self.tweek_label.setGeometry(QRect(1060, 210, 171, 16))
        self.tweek_label.setFont(font2)
        self.tweek_label.setStyleSheet(u"color: #a2a1a1;\n"
"background: transparent;\n"
"\n"
"")
        self.lweek_label = QLabel(self.centralwidget)
        self.lweek_label.setObjectName(u"lweek_label")
        self.lweek_label.setGeometry(QRect(1060, 230, 171, 16))
        self.lweek_label.setFont(font2)
        self.lweek_label.setStyleSheet(u"color: #a2a1a1;\n"
"background: transparent;\n"
"\n"
"")
        self.rj_overtime = QLabel(self.centralwidget)
        self.rj_overtime.setObjectName(u"rj_overtime")
        self.rj_overtime.setGeometry(QRect(1060, 270, 171, 31))
        self.rj_overtime.setFont(font1)
        self.rj_overtime.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.currently_label = QLabel(self.centralwidget)
        self.currently_label.setObjectName(u"currently_label")
        self.currently_label.setGeometry(QRect(1060, 310, 151, 16))
        self.currently_label.setFont(font2)
        self.currently_label.setStyleSheet(u"color: #a2a1a1;\n"
"background: transparent;\n"
"\n"
"")
        self.pload_label = QLabel(self.centralwidget)
        self.pload_label.setObjectName(u"pload_label")
        self.pload_label.setGeometry(QRect(1060, 330, 151, 16))
        self.pload_label.setFont(font2)
        self.pload_label.setStyleSheet(u"color: #a2a1a1;\n"
"background: transparent;\n"
"\n"
"")
        self.lload_label = QLabel(self.centralwidget)
        self.lload_label.setObjectName(u"lload_label")
        self.lload_label.setGeometry(QRect(1060, 350, 151, 16))
        self.lload_label.setFont(font2)
        self.lload_label.setStyleSheet(u"color: #a2a1a1;\n"
"background: transparent;\n"
"\n"
"")
        self.jhis_tview = QTableView(self.centralwidget)
        self.jhis_tview.setObjectName(u"jhis_tview")
        self.jhis_tview.setGeometry(QRect(770, 430, 641, 361))
        self.jhis_tview.setStyleSheet(u"QTableView {\n"
"    background: transparent;\n"
"    border: 1px solid #ffffff;\n"
"    gridline-color: rgba(255,255,255,0.2);\n"
"    color: white;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 13px;\n"
"    selection-background-color: rgba(125, 95, 255, 0.4);\n"
"}\n"
"\n"
"/* Internal viewport must also be rounded */\n"
"QTableView::viewport {\n"
"    background: transparent;\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"/* Header styling */\n"
"QHeaderView::section {\n"
"    background-color: rgba(20,20,50,0.6);\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 6px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Optional: first/last header corners */\n"
"QHeaderView::section:first {\n"
"    border-top-left-radius: 20px;\n"
"}\n"
"QHeaderView::section:last {\n"
"    border-top-right-radius: 20px;\n"
"}\n"
"")
        self.crjobs_tview = QTableView(self.centralwidget)
        self.crjobs_tview.setObjectName(u"crjobs_tview")
        self.crjobs_tview.setGeometry(QRect(100, 430, 654, 361))
        self.crjobs_tview.setStyleSheet(u"QTableView {\n"
"    background: transparent;\n"
"    border: 1px solid #ffffff;\n"
"    gridline-color: rgba(255,255,255,0.2);\n"
"    color: white;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 13px;\n"
"    selection-background-color: rgba(125, 95, 255, 0.4);\n"
"}\n"
"\n"
"/* Internal viewport must also be rounded */\n"
"QTableView::viewport {\n"
"    background: transparent;\n"
"    border-radius: 20px;\n"
"}\n"
"\n"
"/* Header styling */\n"
"QHeaderView::section {\n"
"    background-color: rgba(20,20,50,0.6);\n"
"    color: white;\n"
"    border: none;\n"
"    padding: 6px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Optional: first/last header corners */\n"
"QHeaderView::section:first {\n"
"    border-top-left-radius: 20px;\n"
"}\n"
"QHeaderView::section:last {\n"
"    border-top-right-radius: 20px;\n"
"}\n"
"")
        self.cr_jobs = QLabel(self.centralwidget)
        self.cr_jobs.setObjectName(u"cr_jobs")
        self.cr_jobs.setGeometry(QRect(120, 400, 141, 21))
        self.cr_jobs.setFont(font1)
        self.cr_jobs.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.job_history = QLabel(self.centralwidget)
        self.job_history.setObjectName(u"job_history")
        self.job_history.setGeometry(QRect(790, 400, 141, 20))
        self.job_history.setFont(font1)
        self.job_history.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        jobs_dash.setCentralWidget(self.centralwidget)
        self.sutilization_con.raise_()
        self.crjobs_tview.raise_()
        self.ttrend_con.raise_()
        self.horizontalLayoutWidget.raise_()
        self.logo.raise_()
        self.thru_trend.raise_()
        self.verticalLayoutWidget.raise_()
        self.settings_bt.raise_()
        self.prof_button.raise_()
        self.notif_button.raise_()
        self.toggle_switch.raise_()
        self.workerM_label.raise_()
        self.scurrently_label.raise_()
        self.tsavail_label.raise_()
        self.avg_label.raise_()
        self.highest_label.raise_()
        self.slots_util.raise_()
        self.lowest_label.raise_()
        self.sys_label.raise_()
        self.nodeA_label.raise_()
        self.nodeB_label.raise_()
        self.nodeC_label.raise_()
        self.tstats_con.raise_()
        self.t_statistics.raise_()
        self.today_label.raise_()
        self.yesterday_label.raise_()
        self.tweek_label.raise_()
        self.lweek_label.raise_()
        self.rj_overtime.raise_()
        self.currently_label.raise_()
        self.pload_label.raise_()
        self.lload_label.raise_()
        self.jhis_tview.raise_()
        self.cr_jobs.raise_()
        self.job_history.raise_()
        self.ttrend_chart.raise_()

        self.retranslateUi(jobs_dash)

        QMetaObject.connectSlotsByName(jobs_dash)
    # setupUi

    def retranslateUi(self, jobs_dash):
        jobs_dash.setWindowTitle(QCoreApplication.translate("jobs_dash", u"CrowdCloud", None))
        self.logo.setText("")
        self.thru_trend.setText(QCoreApplication.translate("jobs_dash", u"Throughput Trend", None))
        self.ttrend_con.setText("")
        self.dash_bt.setText("")
        self.sys_bt.setText("")
        self.job_bt.setText("")
        self.earning_bt.setText("")
        self.settings_bt.setText("")
        self.prof_button.setText("")
        self.notif_button.setText("")
        self.workerM_label.setText(QCoreApplication.translate("jobs_dash", u"Worker Mode", None))
        self.scurrently_label.setText(QCoreApplication.translate("jobs_dash", u"Slots currently in use: 8", None))
        self.tsavail_label.setText(QCoreApplication.translate("jobs_dash", u"Total slots available: 20", None))
        self.sutilization_con.setText("")
        self.avg_label.setText(QCoreApplication.translate("jobs_dash", u"Average in 24h: 3 jobs", None))
        self.highest_label.setText(QCoreApplication.translate("jobs_dash", u"Highest: 6 jobs", None))
        self.slots_util.setText(QCoreApplication.translate("jobs_dash", u"Slots Utilization", None))
        self.lowest_label.setText(QCoreApplication.translate("jobs_dash", u"Lowest: 1.5 jobs", None))
        self.sys_label.setText(QCoreApplication.translate("jobs_dash", u"System capacity: 20", None))
        self.nodeA_label.setText(QCoreApplication.translate("jobs_dash", u"Node A: 6/8 slots used", None))
        self.nodeB_label.setText(QCoreApplication.translate("jobs_dash", u"Node B: 4/6 slots used", None))
        self.nodeC_label.setText(QCoreApplication.translate("jobs_dash", u"Node C: 2/6 slots used", None))
        self.tstats_con.setText("")
        self.t_statistics.setText(QCoreApplication.translate("jobs_dash", u"Today's Statistics", None))
        self.today_label.setText(QCoreApplication.translate("jobs_dash", u"Today: 255 jobs completed", None))
        self.yesterday_label.setText(QCoreApplication.translate("jobs_dash", u"Yesterday: 105 jobs completed", None))
        self.tweek_label.setText(QCoreApplication.translate("jobs_dash", u"This week: 555 jobs completed", None))
        self.lweek_label.setText(QCoreApplication.translate("jobs_dash", u"Last week: 334 jobs completed", None))
        self.rj_overtime.setText(QCoreApplication.translate("jobs_dash", u"Running Jobs Over Time", None))
        self.currently_label.setText(QCoreApplication.translate("jobs_dash", u"Currently: 3 jobs running", None))
        self.pload_label.setText(QCoreApplication.translate("jobs_dash", u"Peak Load: 7 jobs", None))
        self.lload_label.setText(QCoreApplication.translate("jobs_dash", u"Lowest Load: 2 jobs", None))
        self.cr_jobs.setText(QCoreApplication.translate("jobs_dash", u"Current Running Jobs", None))
        self.job_history.setText(QCoreApplication.translate("jobs_dash", u"Job history", None))
    # retranslateUi

