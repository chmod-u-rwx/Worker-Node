from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGraphicsView, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QToolButton, QVBoxLayout,
    QWidget)

class Ui_weldash(object):
    def setupUi(self, welcome_dash):
        if not welcome_dash.objectName():
            welcome_dash.setObjectName(u"welcome_dash")
        welcome_dash.resize(1440, 810)
        welcome_dash.setMinimumSize(QSize(1440, 810))
        welcome_dash.setMaximumSize(QSize(1440, 810))
        self.centralwidget = QWidget(welcome_dash)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMinimumSize(QSize(1440, 810))
        self.centralwidget.setMaximumSize(QSize(1440, 810))
        self.centralwidget.setStyleSheet("background-image: url('src/worker_node_ui/resources/images/gen_dashboard.png');")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 2, 2))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(30, 40, 52, 41))
        self.logo.setAutoFillBackground(False)
        self.logo.setStyleSheet(u"background: transparent;")
        self.logo.setPixmap(QPixmap("src/worker_node_ui/resources/images/signup1logo.png"))
        self.logo.setScaledContents(True)
        self.welcome_label = QLabel(self.centralwidget)
        self.welcome_label.setObjectName(u"welcome_label")
        self.welcome_label.setGeometry(QRect(100, 50, 461, 31))
        font = QFont()
        font.setFamilies([u"Century Gothic"])
        font.setPointSize(22)
        font.setBold(True)
        self.welcome_label.setFont(font)
        self.welcome_label.setStyleSheet(u"background: transparent;\n"
"color: white;\n"
"\n"
"")
        self.cpu_usage = QLabel(self.centralwidget)
        self.cpu_usage.setObjectName(u"cpu_usage")
        self.cpu_usage.setGeometry(QRect(130, 120, 141, 31))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(11)
        font1.setBold(False)
        self.cpu_usage.setFont(font1)
        self.cpu_usage.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"")
        self.usage_con = QLabel(self.centralwidget)
        self.usage_con.setObjectName(u"usage_con")
        self.usage_con.setGeometry(QRect(100, 110, 903, 341))
        self.usage_con.setStyleSheet(u"QLabel {\n"
"	background: transparent;\n"
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
        self.verticalLayoutWidget.setGeometry(QRect(30, 110, 43, 301))
        self.verticalLayoutWidget.setStyleSheet("background: transparent;")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
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
        self.rate_con = QLabel(self.centralwidget)
        self.rate_con.setObjectName(u"rate_con")
        self.rate_con.setGeometry(QRect(100, 470, 288, 319))
        self.rate_con.setStyleSheet(u"QLabel {\n"
"	background: transparent;\n"
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
        self.current_con = QLabel(self.centralwidget)
        self.current_con.setObjectName(u"current_con")
        self.current_con.setGeometry(QRect(410, 470, 288, 319))
        self.current_con.setStyleSheet(u"QLabel {\n"
"	background: transparent;\n"
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
        self.run_con = QLabel(self.centralwidget)
        self.run_con.setObjectName(u"run_con")
        self.run_con.setGeometry(QRect(1020, 110, 182, 161))
        self.run_con.setStyleSheet(u"QLabel {\n"
"	background: transparent;\n"
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
        self.avg_con = QLabel(self.centralwidget)
        self.avg_con.setObjectName(u"avg_con")
        self.avg_con.setGeometry(QRect(1020, 290, 182, 161))
        self.avg_con.setStyleSheet(u"QLabel {\n"
"	background: transparent;\n"
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
        self.exe_con = QLabel(self.centralwidget)
        self.exe_con.setObjectName(u"exe_con")
        self.exe_con.setGeometry(QRect(1220, 290, 182, 161))
        self.exe_con.setStyleSheet(u"QLabel {\n"
"	background: transparent;\n"
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
        self.slots_con = QLabel(self.centralwidget)
        self.slots_con.setObjectName(u"slots_con")
        self.slots_con.setGeometry(QRect(1220, 110, 182, 161))
        self.slots_con.setStyleSheet(u"QLabel {\n"
"	background: transparent;\n"
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
        self.memory_usage = QLabel(self.centralwidget)
        self.memory_usage.setObjectName(u"memory_usage")
        self.memory_usage.setGeometry(QRect(420, 120, 171, 31))
        self.memory_usage.setFont(font1)
        self.memory_usage.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"")
        self.cache_usage = QLabel(self.centralwidget)
        self.cache_usage.setObjectName(u"cache_usage")
        self.cache_usage.setGeometry(QRect(690, 120, 141, 31))
        self.cache_usage.setFont(font1)
        self.cache_usage.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"")
        self.earning_rate = QLabel(self.centralwidget)
        self.earning_rate.setObjectName(u"earning_rate")
        self.earning_rate.setGeometry(QRect(120, 480, 101, 31))
        self.earning_rate.setFont(font1)
        self.earning_rate.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"")
        self.current_earnings = QLabel(self.centralwidget)
        self.current_earnings.setObjectName(u"current_earnings")
        self.current_earnings.setGeometry(QRect(430, 480, 141, 31))
        self.current_earnings.setFont(font1)
        self.current_earnings.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"")
        self.avg_job = QLabel(self.centralwidget)
        self.avg_job.setObjectName(u"avg_job")
        self.avg_job.setGeometry(QRect(1040, 300, 81, 31))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(9)
        font2.setBold(False)
        self.avg_job.setFont(font2)
        self.avg_job.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"")
        self.jobs_executed = QLabel(self.centralwidget)
        self.jobs_executed.setObjectName(u"jobs_executed")
        self.jobs_executed.setGeometry(QRect(1240, 300, 81, 31))
        self.jobs_executed.setFont(font2)
        self.jobs_executed.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"")
        self.running_jobs = QLabel(self.centralwidget)
        self.running_jobs.setObjectName(u"running_jobs")
        self.running_jobs.setGeometry(QRect(1040, 120, 81, 31))
        self.running_jobs.setFont(font2)
        self.running_jobs.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"")
        self.jobs_slots = QLabel(self.centralwidget)
        self.jobs_slots.setObjectName(u"jobs_slots")
        self.jobs_slots.setGeometry(QRect(1240, 120, 51, 31))
        self.jobs_slots.setFont(font2)
        self.jobs_slots.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"")
        self.rate_chart = QGraphicsView(self.centralwidget)
        self.rate_chart.setObjectName(u"rate_chart")
        self.rate_chart.setGeometry(QRect(120, 570, 256, 192))
        self.rate_chart.setStyleSheet(u"background: transparent;")
        self.cpu_chart = QWidget(self.centralwidget)
        self.cpu_chart.setObjectName(u"cpu_chart")
        self.cpu_chart.setGeometry(QRect(150, 200, 191, 191))
        self.cpu_chart.setStyleSheet(u"background: transparent;")
        self.mem_chart = QWidget(self.centralwidget)
        self.mem_chart.setObjectName(u"mem_chart")
        self.mem_chart.setGeometry(QRect(410, 200, 191, 191))
        self.mem_chart.setStyleSheet(u"background: transparent;")
        self.cache_chart = QWidget(self.centralwidget)
        self.cache_chart.setObjectName(u"cache_chart")
        self.cache_chart.setGeometry(QRect(700, 210, 251, 31))
        self.cache_chart.setStyleSheet(u"background: transparent;")
        self.rjobs_label = QLabel(self.centralwidget)
        self.rjobs_label.setObjectName(u"rjobs_label")
        self.rjobs_label.setGeometry(QRect(1040, 160, 61, 61))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(36)
        font3.setBold(True)
        self.rjobs_label.setFont(font3)
        self.rjobs_label.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"")
        self.jslots_label = QLabel(self.centralwidget)
        self.jslots_label.setObjectName(u"jslots_label")
        self.jslots_label.setGeometry(QRect(1240, 160, 61, 61))
        self.jslots_label.setFont(font3)
        self.jslots_label.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"")
        self.jexe_label = QLabel(self.centralwidget)
        self.jexe_label.setObjectName(u"jexe_label")
        self.jexe_label.setGeometry(QRect(1240, 340, 101, 61))
        self.jexe_label.setFont(font3)
        self.jexe_label.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"")
        self.ajob_label = QLabel(self.centralwidget)
        self.ajob_label.setObjectName(u"ajob_label")
        self.ajob_label.setGeometry(QRect(1040, 340, 141, 61))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(24)
        font4.setBold(True)
        self.ajob_label.setFont(font4)
        self.ajob_label.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"")
        self.avgtp_label = QLabel(self.centralwidget)
        self.avgtp_label.setObjectName(u"avgtp_label")
        self.avgtp_label.setGeometry(QRect(1040, 410, 141, 31))
        self.avgtp_label.setFont(font2)
        self.avgtp_label.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"")
        self.exet_label = QLabel(self.centralwidget)
        self.exet_label.setObjectName(u"exet_label")
        self.exet_label.setGeometry(QRect(1240, 410, 81, 31))
        self.exet_label.setFont(font2)
        self.exet_label.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"")
        self.current_label = QLabel(self.centralwidget)
        self.current_label.setObjectName(u"current_label")
        self.current_label.setGeometry(QRect(430, 520, 171, 61))
        self.current_label.setFont(font4)
        self.current_label.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"")
        self.prof_button = QToolButton(self.centralwidget)
        self.prof_button.setObjectName(u"prof_button")
        self.prof_button.setGeometry(QRect(1320, 40, 51, 50))
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
        self.notif_button.setGeometry(QRect(1250, 40, 51, 50))
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
        self.inc_label = QLabel(self.centralwidget)
        self.inc_label.setObjectName(u"inc_label")
        self.inc_label.setGeometry(QRect(470, 580, 31, 31))
        self.inc_label.setFont(font1)
        self.inc_label.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"")
        self.inc_wid = QWidget(self.centralwidget)
        self.inc_wid.setObjectName(u"inc_wid")
        self.inc_wid.setGeometry(QRect(440, 590, 21, 21))
        self.inc_wid.setStyleSheet(u"background: transparent;")
        self.currentp_label = QLabel(self.centralwidget)
        self.currentp_label.setObjectName(u"currentp_label")
        self.currentp_label.setGeometry(QRect(540, 580, 61, 31))
        self.currentp_label.setFont(font1)
        self.currentp_label.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"")
        self.rate_label = QLabel(self.centralwidget)
        self.rate_label.setObjectName(u"rate_label")
        self.rate_label.setGeometry(QRect(120, 520, 201, 31))
        self.rate_label.setFont(font4)
        self.rate_label.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"")
        self.hist_con = QWidget(self.centralwidget)
        self.hist_con.setObjectName(u"hist_con")
        self.hist_con.setGeometry(QRect(720, 470, 681, 321))
        self.hist_con.setStyleSheet(u"background: transparent;\n"
"border: 1px solid rgba(255, 255, 255, 0.3);\n"
"border-radius: 35px;\n"
"")
        self.hist_table = QTableWidget(self.hist_con)
        if (self.hist_table.columnCount() < 4):
            self.hist_table.setColumnCount(4)
        font5 = QFont()
        font5.setFamilies([u"Century Gothic"])
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font5);
        self.hist_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.hist_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.hist_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.hist_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.hist_table.setObjectName(u"hist_table")
        self.hist_table.setGeometry(QRect(0, 40, 681, 281))
        self.hist_table.setStyleSheet(u"QTableWidget {\n"
"    background: transparent; /* translucent background */\n"
"    border: transparent;\n"
"    border-radius: 35px;   /* smaller radius looks cleaner for tables */\n"
"    padding: 8px;\n"
"    color: white;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 13px;\n"
"    gridline-color: rgba(255,255,255,0.2);  /* faint gridlines */\n"
"    selection-background-color: rgba(125, 95, 255, 0.4); /* selected row */\n"
"}\n"
"\n"
"QTableWidget:focus {\n"
"    border: 1px solid #7D5FFF;\n"
"    box-shadow: 0px 0px 8px #7D5FFF;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: rgba(20,20,50,0.6); \n"
"    color: white;\n"
"    border: none;\n"
"    padding: 6px;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.hist_table.horizontalHeader().setDefaultSectionSize(150)
        self.hist_table.horizontalHeader().setStretchLastSection(True)
        self.job_history = QLabel(self.hist_con)
        self.job_history.setObjectName(u"job_history")
        self.job_history.setGeometry(QRect(20, 10, 141, 31))
        self.job_history.setFont(font1)
        self.job_history.setStyleSheet(u"color: white;\n"
"border-color: transparent;")
        self.refresh_bt = QToolButton(self.hist_con)
        self.refresh_bt.setObjectName(u"refresh_bt")
        self.refresh_bt.setGeometry(QRect(630, 10, 31, 31))
        sizePolicy.setHeightForWidth(self.refresh_bt.sizePolicy().hasHeightForWidth())
        self.refresh_bt.setSizePolicy(sizePolicy)
        self.refresh_bt.setStyleSheet(u"QToolButton {\n"
"    background: transparent;       /* no fill */\n"
"    color: white;                  /* icon/text color */\n"
"    border: 1px solid #ffffff;     /* white border */\n"
"    border-radius: 15px;           /* make it round (half of width/height) */\n"
"    padding: 3px;                  /* space inside */\n"
"}\n"
"")
        icon7 = QIcon()
        icon7.addFile(u"src/worker_node_ui/resources/fbuttons/refresh.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.refresh_bt.setIcon(icon7)
        self.refresh_bt.setIconSize(QSize(35, 35))
        self.toggle_switch = QWidget(self.centralwidget)
        self.toggle_switch.setObjectName(u"toggle_switch")
        self.toggle_switch.setGeometry(QRect(1158, 47, 91, 21))
        self.toggle_switch.setStyleSheet(u"background: transparent;")
        self.workerM_label = QLabel(self.centralwidget)
        self.workerM_label.setObjectName(u"workerM_label")
        self.workerM_label.setGeometry(QRect(1150, 80, 81, 16))
        self.workerM_label.setFont(font2)
        self.workerM_label.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"")

        self.widget_7 = QWidget(self.centralwidget)
        self.widget_7.setVisible(True)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(130, 160, 16, 16))
        self.widget_7.setStyleSheet(u"border-radius: 4px;\n"
"background-color: #D6BDDC;")


        self.widget_8 = QWidget(self.centralwidget)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setGeometry(QRect(130, 180, 16, 16))
        self.widget_8.setStyleSheet(u"border-radius: 4px;\n"
"background-color: #49067C;")
        self.widget_8.setAttribute(Qt.WA_StyledBackground, True)

        self.widget_9 = QWidget(self.centralwidget)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setGeometry(QRect(420, 160, 16, 16))
        self.widget_9.setStyleSheet(u"border-radius: 4px;\n"
"background-color: #49067C;")
        self.widget_9.setAttribute(Qt.WA_StyledBackground, True)

        self.widget_10 = QWidget(self.centralwidget)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setGeometry(QRect(490, 160, 16, 16))
        self.widget_10.setStyleSheet(u"border-radius: 4px;\n"
"background-color: #151A20;")
        self.widget_10.setAttribute(Qt.WA_StyledBackground, True)

        self.widget_11 = QWidget(self.centralwidget)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setGeometry(QRect(700, 260, 31, 16))
        self.widget_11.setStyleSheet(u"border-radius: 8px;\n"
"background-color: #49067C;")
        self.widget_11.setAttribute(Qt.WA_StyledBackground, True)

        self.widget_12 = QWidget(self.centralwidget)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setGeometry(QRect(840, 260, 31, 16))
        self.widget_12.setStyleSheet(u"border-radius: 8px;\n"
"background-color: #D6BDDC;")
        self.widget_12.setAttribute(Qt.WA_StyledBackground, True)

        self.consumed_data = QLabel(self.centralwidget)
        self.consumed_data.setObjectName(u"consumed_data")
        self.consumed_data.setGeometry(QRect(740, 260, 91, 16))
        self.consumed_data.setFont(font2)
        self.consumed_data.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"")
        self.avail_space = QLabel(self.centralwidget)
        self.avail_space.setObjectName(u"avail_space")
        self.avail_space.setGeometry(QRect(880, 260, 91, 16))
        self.avail_space.setFont(font2)
        self.avail_space.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"")
        self.memo_used = QLabel(self.centralwidget)
        self.memo_used.setObjectName(u"memo_used")
        self.memo_used.setGeometry(QRect(440, 160, 31, 16))
        self.memo_used.setFont(font2)
        self.memo_used.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"")
        self.memo_total = QLabel(self.centralwidget)
        self.memo_total.setObjectName(u"memo_total")
        self.memo_total.setGeometry(QRect(510, 160, 31, 16))
        self.memo_total.setFont(font2)
        self.memo_total.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"")
        self.vm_id = QLabel(self.centralwidget)
        self.vm_id.setObjectName(u"vm_id")
        self.vm_id.setGeometry(QRect(150, 160, 91, 16))
        self.vm_id.setFont(font2)
        self.vm_id.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"")
        self.cpu_perce = QLabel(self.centralwidget)
        self.cpu_perce.setObjectName(u"cpu_perce")
        self.cpu_perce.setGeometry(QRect(150, 180, 91, 16))
        self.cpu_perce.setFont(font2)
        self.cpu_perce.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"")
        self.diskusage_label = QLabel(self.centralwidget)
        self.diskusage_label.setObjectName(u"diskusage_label")
        self.diskusage_label.setGeometry(QRect(700, 160, 211, 31))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(14)
        font6.setBold(True)
        self.diskusage_label.setFont(font6)
        self.diskusage_label.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"")
        self.report_bt = QPushButton(self.centralwidget)
        self.report_bt.setObjectName(u"report_bt")
        self.report_bt.setGeometry(QRect(420, 750, 101, 20))
        font7 = QFont()
        font7.setFamilies([u"Segoe UI"])
        font7.setPointSize(11)
        self.report_bt.setFont(font7)
        self.report_bt.setStyleSheet(u"QPushButton {\n"
"    background: transparent;\n"
"    border: none;\n"
"    color: #FFFFFF;  /* purple link color */\n"
"}\n"
"QPushButton:hover {\n"
"    color: #5B3ECC;\n"
"    cursor: pointer;\n"
"}\n"
"")
        self.report_bt2 = QToolButton(self.centralwidget)
        self.report_bt2.setObjectName(u"report_bt2")
        self.report_bt2.setGeometry(QRect(520, 750, 21, 21))
        sizePolicy.setHeightForWidth(self.report_bt2.sizePolicy().hasHeightForWidth())
        self.report_bt2.setSizePolicy(sizePolicy)
        self.report_bt2.setStyleSheet(u"background: transparent;")
        icon8 = QIcon()
        icon8.addFile(u"../../../../../Downloads/Arrow_Right_LG.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.report_bt2.setIcon(icon8)
        self.report_bt2.setIconSize(QSize(31, 41))
        welcome_dash.setCentralWidget(self.centralwidget)
        self.hist_con.raise_()
        self.usage_con.raise_()
        self.horizontalLayoutWidget.raise_()
        self.logo.raise_()
        self.welcome_label.raise_()
        self.cpu_usage.raise_()
        self.verticalLayoutWidget.raise_()
        self.settings_bt.raise_()
        self.rate_con.raise_()
        self.current_con.raise_()
        self.run_con.raise_()
        self.avg_con.raise_()
        self.exe_con.raise_()
        self.slots_con.raise_()
        self.memory_usage.raise_()
        self.cache_usage.raise_()
        self.earning_rate.raise_()
        self.current_earnings.raise_()
        self.avg_job.raise_()
        self.jobs_executed.raise_()
        self.running_jobs.raise_()
        self.jobs_slots.raise_()
        self.rate_chart.raise_()
        self.cpu_chart.raise_()
        self.mem_chart.raise_()
        self.cache_chart.raise_()
        self.rjobs_label.raise_()
        self.jslots_label.raise_()
        self.jexe_label.raise_()
        self.ajob_label.raise_()
        self.avgtp_label.raise_()
        self.exet_label.raise_()
        self.current_label.raise_()
        self.prof_button.raise_()
        self.notif_button.raise_()
        self.inc_label.raise_()
        self.inc_wid.raise_()
        self.currentp_label.raise_()
        self.rate_label.raise_()
        self.toggle_switch.raise_()
        self.workerM_label.raise_()
        self.widget_7.raise_()
        self.widget_8.raise_()
        self.widget_9.raise_()
        self.widget_10.raise_()
        self.widget_11.raise_()
        self.widget_12.raise_()
        self.consumed_data.raise_()
        self.avail_space.raise_()
        self.memo_used.raise_()
        self.memo_total.raise_()
        self.vm_id.raise_()
        self.cpu_perce.raise_()
        self.diskusage_label.raise_()
        self.report_bt.raise_()
        self.report_bt2.raise_()

        self.retranslateUi(welcome_dash)

        QMetaObject.connectSlotsByName(welcome_dash)
    # setupUi

    def retranslateUi(self, welcome_dash):
        welcome_dash.setWindowTitle(QCoreApplication.translate("welcome_dash", u"CrowdCloud", None))
        self.logo.setText("")
        self.welcome_label.setText(QCoreApplication.translate("welcome_dash", u"Hi,  Welcome Back", None))
        self.cpu_usage.setText(QCoreApplication.translate("welcome_dash", u"CPU Usage per VM", None))
        self.usage_con.setText("")
        self.dash_bt.setText("")
        self.sys_bt.setText("")
        self.job_bt.setText("")
        self.earning_bt.setText("")
        self.settings_bt.setText("")
        self.rate_con.setText("")
        self.current_con.setText("")
        self.run_con.setText("")
        self.avg_con.setText("")
        self.exe_con.setText("")
        self.slots_con.setText("")
        self.memory_usage.setText(QCoreApplication.translate("welcome_dash", u"Memory Usage per VM", None))
        self.cache_usage.setText(QCoreApplication.translate("welcome_dash", u"Cache Disk Usage", None))
        self.earning_rate.setText(QCoreApplication.translate("welcome_dash", u"Earning Rate", None))
        self.current_earnings.setText(QCoreApplication.translate("welcome_dash", u"Current Earnings", None))
        self.avg_job.setText(QCoreApplication.translate("welcome_dash", u"Average Job", None))
        self.jobs_executed.setText(QCoreApplication.translate("welcome_dash", u"Jobs Executed", None))
        self.running_jobs.setText(QCoreApplication.translate("welcome_dash", u"Running Jobs", None))
        self.jobs_slots.setText(QCoreApplication.translate("welcome_dash", u"Job Slots", None))
        self.rjobs_label.setText(QCoreApplication.translate("welcome_dash", u"12", None))
        self.jslots_label.setText(QCoreApplication.translate("welcome_dash", u"12", None))
        self.jexe_label.setText(QCoreApplication.translate("welcome_dash", u"544", None))
        self.ajob_label.setText(QCoreApplication.translate("welcome_dash", u"3/min", None))
        self.avgtp_label.setText(QCoreApplication.translate("welcome_dash", u"Avg Throughput: 2.5/min", None))
        self.exet_label.setText(QCoreApplication.translate("welcome_dash", u"Three Days", None))
        self.current_label.setText(QCoreApplication.translate("welcome_dash", u"PHP 890.93", None))
        self.prof_button.setText("")
        self.notif_button.setText("")
        self.inc_label.setText(QCoreApplication.translate("welcome_dash", u"-- --", None))
        self.currentp_label.setText(QCoreApplication.translate("welcome_dash", u"-- --", None))
        self.rate_label.setText(QCoreApplication.translate("welcome_dash", u"PHP 125/hr", None))
        ___qtablewidgetitem = self.hist_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("welcome_dash", u"User ID", None));
        ___qtablewidgetitem1 = self.hist_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("welcome_dash", u"Retained", None));
        ___qtablewidgetitem2 = self.hist_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("welcome_dash", u"Duration", None));
        ___qtablewidgetitem3 = self.hist_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("welcome_dash", u"Amount", None));
        self.job_history.setText(QCoreApplication.translate("welcome_dash", u"Job History", None))
        self.refresh_bt.setText("")
        self.workerM_label.setText(QCoreApplication.translate("welcome_dash", u"Worker Mode", None))
        self.consumed_data.setText(QCoreApplication.translate("welcome_dash", u"Consumed Data", None))
        self.avail_space.setText(QCoreApplication.translate("welcome_dash", u"Available Space", None))
        self.memo_used.setText(QCoreApplication.translate("welcome_dash", u"Used", None))
        self.memo_total.setText(QCoreApplication.translate("welcome_dash", u"Total", None))
        self.vm_id.setText(QCoreApplication.translate("welcome_dash", u"VM ID", None))
        self.cpu_perce.setText(QCoreApplication.translate("welcome_dash", u"CPU %", None))
        self.diskusage_label.setText(QCoreApplication.translate("welcome_dash", u"324/1000 MB", None))
        self.report_bt.setText(QCoreApplication.translate("welcome_dash", u"View Report", None))
        self.report_bt2.setText("")
    # retranslateUi

