from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGraphicsView, QHBoxLayout, QHeaderView,
    QLabel, QSizePolicy, QTableWidget, QTableWidgetItem,
    QToolButton, QVBoxLayout, QWidget)

class UiInformationUsage(object):
    def setupUi(self, information_usage):
        if not information_usage.objectName():
            information_usage.setObjectName(u"information_usage")
        information_usage.resize(1440, 810)
        information_usage.setMinimumSize(QSize(1440, 810))
        information_usage.setMaximumSize(QSize(1440, 810))
        self.bg_label = QLabel(information_usage)
        self.bg_label.setPixmap(QPixmap("src/worker_node_ui/resources/images/usage_bg.png"))
        self.bg_label.setScaledContents(True)
        self.bg_label.setGeometry(0, 0, information_usage.width(), information_usage.height())
        self.bg_label.lower()
        self.horizontalLayoutWidget = QWidget(information_usage)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 2, 2))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.logo = QLabel(information_usage)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(30, 40, 52, 41))
        self.logo.setAutoFillBackground(False)
        self.logo.setStyleSheet(u"background: transparent;")
        self.logo.setPixmap(QPixmap("src/worker_node_ui/resources/images/signup1logo.png"))
        self.logo.setScaledContents(True)
        font = QFont()
        font.setFamilies([u"Century Gothic"])
        font.setPointSize(22)
        font.setBold(True)
        self.cpu_usage = QLabel(information_usage)
        self.cpu_usage.setObjectName(u"cpu_usage")
        self.cpu_usage.setGeometry(QRect(530, 120, 141, 31))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(11)
        font1.setBold(False)
        self.cpu_usage.setFont(font1)
        self.cpu_usage.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.usage_con = QLabel(information_usage)
        self.usage_con.setObjectName(u"usage_con")
        self.usage_con.setGeometry(QRect(500, 110, 903, 341))
        self.usage_con.setStyleSheet(u"QLabel {\n"
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
"}\n"
"")
        self.verticalLayoutWidget = QWidget(information_usage)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 110, 43, 301))
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

        self.settings_bt = QToolButton(information_usage)
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
        self.trend_con = QLabel(information_usage)
        self.trend_con.setObjectName(u"trend_con")
        self.trend_con.setGeometry(QRect(100, 110, 381, 681))
        self.trend_con.setStyleSheet(u"QLabel {\n"
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
"}\n"
"")
        self.memory_usage = QLabel(information_usage)
        self.memory_usage.setObjectName(u"memory_usage")
        self.memory_usage.setGeometry(QRect(820, 120, 171, 31))
        self.memory_usage.setFont(font1)
        self.memory_usage.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.cache_usage = QLabel(information_usage)
        self.cache_usage.setObjectName(u"cache_usage")
        self.cache_usage.setGeometry(QRect(1090, 120, 141, 31))
        self.cache_usage.setFont(font1)
        self.cache_usage.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"")
        self.trend_over24hr = QLabel(information_usage)
        self.trend_over24hr.setObjectName(u"trend_over24hr")
        self.trend_over24hr.setGeometry(QRect(120, 120, 121, 31))
        self.trend_over24hr.setFont(font1)
        self.trend_over24hr.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"")
        self.trend_chart = QGraphicsView(information_usage)
        self.trend_chart.setObjectName(u"trend_chart")
        self.trend_chart.setGeometry(QRect(120, 170, 341, 211))
        self.trend_chart.setStyleSheet(u"background: transparent;")
        self.cpu_chart = QWidget(information_usage)
        self.cpu_chart.setObjectName(u"cpu_chart")
        self.cpu_chart.setGeometry(QRect(550, 210, 191, 191))
        self.cpu_chart.setStyleSheet(u"background: transparent;\n"
"")
        self.mem_chart = QWidget(information_usage)
        self.mem_chart.setObjectName(u"mem_chart")
        self.mem_chart.setGeometry(QRect(840, 210, 191, 191))
        self.mem_chart.setStyleSheet(u"background: transparent;\n"
"")
        self.cache_chart = QWidget(information_usage)
        self.cache_chart.setObjectName(u"cache_chart")
        self.cache_chart.setGeometry(QRect(1100, 210, 251, 31))
        self.cache_chart.setStyleSheet(u"background: transparent;\n"
"")
        self.prof_button = QToolButton(information_usage)
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
        self.notif_button = QToolButton(information_usage)
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
        self.toggle_switch = QWidget(information_usage)
        self.toggle_switch.setObjectName(u"toggle_switch")
        self.toggle_switch.setGeometry(QRect(1145, 45, 91, 21))
        self.toggle_switch.setStyleSheet(u"background: transparent;")
        self.workerM_label = QLabel(information_usage)
        self.workerM_label.setObjectName(u"workerM_label")
        self.workerM_label.setGeometry(QRect(1150, 80, 81, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(9)
        font2.setBold(False)
        self.workerM_label.setFont(font2)
        self.workerM_label.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.consumed_data = QLabel(information_usage)
        self.consumed_data.setObjectName(u"consumed_data")
        self.consumed_data.setGeometry(QRect(1140, 260, 91, 16))
        self.consumed_data.setFont(font2)
        self.consumed_data.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.avail_space = QLabel(information_usage)
        self.avail_space.setObjectName(u"avail_space")
        self.avail_space.setGeometry(QRect(1280, 260, 91, 16))
        self.avail_space.setFont(font2)
        self.avail_space.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.memo_used = QLabel(information_usage)
        self.memo_used.setObjectName(u"memo_used")
        self.memo_used.setGeometry(QRect(840, 160, 31, 16))
        self.memo_used.setFont(font2)
        self.memo_used.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"")
        self.memo_total = QLabel(information_usage)
        self.memo_total.setObjectName(u"memo_total")
        self.memo_total.setGeometry(QRect(910, 160, 31, 16))
        self.memo_total.setFont(font2)
        self.memo_total.setStyleSheet(u"color: white;\n"
"background-color: transparent;\n"
"")
        self.vm_id = QLabel(information_usage)
        self.vm_id.setObjectName(u"vm_id")
        self.vm_id.setGeometry(QRect(550, 160, 91, 16))
        self.vm_id.setFont(font2)
        self.vm_id.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.cpu_perce = QLabel(information_usage)
        self.cpu_perce.setObjectName(u"cpu_perce")
        self.cpu_perce.setGeometry(QRect(550, 180, 91, 16))
        self.cpu_perce.setFont(font2)
        self.cpu_perce.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.diskusage_label = QLabel(information_usage)
        self.diskusage_label.setObjectName(u"diskusage_label")
        self.diskusage_label.setGeometry(QRect(1100, 160, 211, 31))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(14)
        font3.setBold(True)
        self.diskusage_label.setFont(font3)
        self.diskusage_label.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.history_table = QTableWidget(information_usage)
        if (self.history_table.columnCount() < 6):
            self.history_table.setColumnCount(6)
        font4 = QFont()
        font4.setFamilies([u"Century Gothic"])
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font4);
        self.history_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.history_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.history_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.history_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.history_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.history_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.history_table.setObjectName(u"history_table")
        self.history_table.setGeometry(QRect(500, 470, 901, 321))
        self.history_table.setStyleSheet(u"/* All header sections */\n"
"QHeaderView::section {\n"
"    background-color: rgba(20,20,50,0.6); \n"
"    color: white;\n"
"    border: none;\n"
"    padding: 6px;\n"
"    font-weight: bold;\n"
"    border-radius: 0px;  /* reset, avoid pill-shape for all */\n"
"}\n"
"\n"
"/* First column (round only left corner) */\n"
"QHeaderView::section:first {\n"
"    border-top-left-radius: 35px;\n"
"}\n"
"\n"
"/* Last column (round only right corner) */\n"
"QHeaderView::section:last {\n"
"    border-top-right-radius: 35px;\n"
"}\n"
"")
        self.history_table.horizontalHeader().setDefaultSectionSize(155)
        self.history_table.horizontalHeader().setStretchLastSection(True)
        self.daily_consump = QLabel(information_usage)
        self.daily_consump.setObjectName(u"daily_consump")
        self.daily_consump.setGeometry(QRect(120, 400, 121, 16))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(10)
        font5.setBold(False)
        self.daily_consump.setFont(font5)
        self.daily_consump.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.memcon_label = QLabel(information_usage)
        self.memcon_label.setObjectName(u"memcon_label")
        self.memcon_label.setGeometry(QRect(120, 420, 181, 16))
        self.memcon_label.setFont(font5)
        self.memcon_label.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.cputime_label = QLabel(information_usage)
        self.cputime_label.setObjectName(u"cputime_label")
        self.cputime_label.setGeometry(QRect(120, 440, 171, 16))
        self.cputime_label.setFont(font5)
        self.cputime_label.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.cachecon_label = QLabel(information_usage)
        self.cachecon_label.setObjectName(u"cachecon_label")
        self.cachecon_label.setGeometry(QRect(120, 460, 181, 16))
        self.cachecon_label.setFont(font5)
        self.cachecon_label.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"")
        self.icon_1 = QLabel(information_usage)
        self.icon_1.setObjectName(u"icon_1")
        self.icon_1.setGeometry(QRect(530, 160, 16, 16))
        self.icon_1.setStyleSheet(u"border-radius: 4px;\n"
"background-color: #D6BDDC;")
        self.icon_2 = QLabel(information_usage)
        self.icon_2.setObjectName(u"icon_2")
        self.icon_2.setGeometry(QRect(530, 180, 16, 16))
        self.icon_2.setStyleSheet(u"border-radius: 4px;\n"
"background-color: #49067C;")
        self.icon_3 = QLabel(information_usage)
        self.icon_3.setObjectName(u"icon_3")
        self.icon_3.setGeometry(QRect(820, 160, 16, 16))
        self.icon_3.setStyleSheet(u"border-radius: 4px;\n"
"background-color: #49067C;")
        self.icon_4 = QLabel(information_usage)
        self.icon_4.setObjectName(u"icon_4")
        self.icon_4.setGeometry(QRect(890, 160, 16, 16))
        self.icon_4.setStyleSheet(u"border-radius: 4px;\n"
"background-color: #151A20;")
        self.icon_5 = QLabel(information_usage)
        self.icon_5.setObjectName(u"icon_5")
        self.icon_5.setGeometry(QRect(1100, 260, 31, 16))
        self.icon_5.setStyleSheet(u"border-radius: 8px;\n"
"background-color: #49067C;")
        self.icon_6 = QLabel(information_usage)
        self.icon_6.setObjectName(u"icon_6")
        self.icon_6.setGeometry(QRect(1240, 260, 31, 16))
        self.icon_6.setStyleSheet(u"border-radius: 8px;\n"
"background-color: #D6BDDC;")
        self.usage_con.raise_()
        self.horizontalLayoutWidget.raise_()
        self.logo.raise_()
        self.cpu_usage.raise_()
        self.verticalLayoutWidget.raise_()
        self.settings_bt.raise_()
        self.trend_con.raise_()
        self.memory_usage.raise_()
        self.cache_usage.raise_()
        self.trend_over24hr.raise_()
        self.trend_chart.raise_()
        self.cpu_chart.raise_()
        self.mem_chart.raise_()
        self.cache_chart.raise_()
        self.prof_button.raise_()
        self.notif_button.raise_()
        self.toggle_switch.raise_()
        self.workerM_label.raise_()
        self.consumed_data.raise_()
        self.avail_space.raise_()
        self.memo_used.raise_()
        self.memo_total.raise_()
        self.vm_id.raise_()
        self.cpu_perce.raise_()
        self.diskusage_label.raise_()
        self.history_table.raise_()
        self.daily_consump.raise_()
        self.memcon_label.raise_()
        self.cputime_label.raise_()
        self.cachecon_label.raise_()
        self.icon_1.raise_()
        self.icon_2.raise_()
        self.icon_3.raise_()
        self.icon_4.raise_()
        self.icon_5.raise_()
        self.icon_6.raise_()

        self.retranslateUi(information_usage)

        QMetaObject.connectSlotsByName(information_usage)
    # setupUi

    def retranslateUi(self, information_usage):
        information_usage.setWindowTitle(QCoreApplication.translate("information_usage", u"CrowdCloud", None))
        self.logo.setText("")
        self.cpu_usage.setText(QCoreApplication.translate("information_usage", u"CPU Usage per VM", None))
        self.usage_con.setText("")
        self.dash_bt.setText("")
        self.sys_bt.setText("")
        self.job_bt.setText("")
        self.earning_bt.setText("")
        self.settings_bt.setText("")
        self.trend_con.setText("")
        self.memory_usage.setText(QCoreApplication.translate("information_usage", u"Memory Usage per VM", None))
        self.cache_usage.setText(QCoreApplication.translate("information_usage", u"Cache Disk Usage", None))
        self.trend_over24hr.setText(QCoreApplication.translate("information_usage", u"Trend over 24hr", None))
        self.prof_button.setText("")
        self.notif_button.setText("")
        self.workerM_label.setText(QCoreApplication.translate("information_usage", u"Worker Mode", None))
        self.consumed_data.setText(QCoreApplication.translate("information_usage", u"Consumed Data", None))
        self.avail_space.setText(QCoreApplication.translate("information_usage", u"Available Space", None))
        self.memo_used.setText(QCoreApplication.translate("information_usage", u"Used", None))
        self.memo_total.setText(QCoreApplication.translate("information_usage", u"Total", None))
        self.vm_id.setText(QCoreApplication.translate("information_usage", u"VM ID", None))
        self.cpu_perce.setText(QCoreApplication.translate("information_usage", u"CPU %", None))
        self.diskusage_label.setText(QCoreApplication.translate("information_usage", u"324/1000 MB", None))
        ___qtablewidgetitem = self.history_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("information_usage", u"VM Name", None)); #type: ignore
        ___qtablewidgetitem1 = self.history_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("information_usage", u"CPU Avg %", None)); #type: ignore
        ___qtablewidgetitem2 = self.history_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("information_usage", u"CPU Peak %", None)); #type: ignore
        ___qtablewidgetitem3 = self.history_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("information_usage", u"Memory Used/ Total (MB)", None)); #type: ignore
        ___qtablewidgetitem4 = self.history_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("information_usage", u"Cache Used/ Total (MB)", None)); #type: ignore
        ___qtablewidgetitem5 = self.history_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("information_usage", u"Status", None)); #type: ignore
        self.daily_consump.setText(QCoreApplication.translate("information_usage", u"Daily Consumption", None))
        self.memcon_label.setText(QCoreApplication.translate("information_usage", u"Memory Consumed: +512 MB", None))
        self.cputime_label.setText(QCoreApplication.translate("information_usage", u"CPU Time Used: 14.3 hours", None))
        self.cachecon_label.setText(QCoreApplication.translate("information_usage", u"Cache Consumed: +2048 MB", None))
        self.icon_1.setText("")
        self.icon_2.setText("")
        self.icon_3.setText("")
        self.icon_4.setText("")
        self.icon_5.setText("")
        self.icon_6.setText("")
    # retranslateUi

