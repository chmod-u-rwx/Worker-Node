from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QSizePolicy, QTableView, QToolButton, QVBoxLayout,
    QWidget)

class UiInformationEarnings(object):
    def setupUi(self, information_earnings):
        if not information_earnings.objectName():
            information_earnings.setObjectName(u"information_earnings")
        information_earnings.resize(1440, 810)
        information_earnings.setMinimumSize(QSize(1440, 810))
        information_earnings.setMaximumSize(QSize(1440, 810))
        self.bg_label = QLabel(information_earnings)
        self.bg_label.setPixmap(QPixmap("src/worker_node_ui/resources/images/earn_bg.png"))
        self.bg_label.setScaledContents(True)  # scales image with window
        self.bg_label.setGeometry(0, 0, information_earnings.width(), information_earnings.height())
        self.bg_label.lower()  # send to back
        self.horizontalLayoutWidget = QWidget(information_earnings)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 2, 2))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.logo = QLabel(information_earnings)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(20, 60, 52, 41))
        self.logo.setAutoFillBackground(False)
        self.logo.setStyleSheet(u"background: transparent;")
        self.logo.setPixmap(QPixmap("src/worker_node_ui/resources/images/signup1logo.png"))
        self.logo.setScaledContents(True)
        font = QFont()
        font.setFamilies([u"Century Gothic"])
        font.setPointSize(22)
        font.setBold(True)
        self.earning_rate = QLabel(information_earnings)
        self.earning_rate.setObjectName(u"earning_rate")
        self.earning_rate.setGeometry(QRect(490, 140, 141, 31))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(11)
        font1.setBold(False)
        self.earning_rate.setFont(font1)
        self.earning_rate.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.earning_con = QLabel(information_earnings)
        self.earning_con.setObjectName(u"earning_con")
        self.earning_con.setGeometry(QRect(470, 130, 291, 320))
        self.earning_con.setStyleSheet(u"QLabel {\n"
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
        self.verticalLayoutWidget = QWidget(information_earnings)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 130, 43, 301))
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

        self.settings_bt = QToolButton(information_earnings)
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
        self.balance_con = QLabel(information_earnings)
        self.balance_con.setObjectName(u"balance_con")
        self.balance_con.setGeometry(QRect(100, 130, 351, 319))
        self.balance_con.setStyleSheet(u"QLabel {\n"
"	background-color: #200447;\n"
"    border: 2px solid #340561;\n"
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
        self.balance_details = QLabel(information_earnings)
        self.balance_details.setObjectName(u"balance_details")
        self.balance_details.setGeometry(QRect(120, 140, 121, 31))
        self.balance_details.setFont(font1)
        self.balance_details.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.eline_chart = QWidget(information_earnings)
        self.eline_chart.setObjectName(u"eline_chart")
        self.eline_chart.setGeometry(QRect(490, 230, 251, 131))
        self.eline_chart.setStyleSheet(u"background: transparent;\n"
"")
        self.prof_button = QToolButton(information_earnings)
        self.prof_button.setObjectName(u"prof_button")
        self.prof_button.setGeometry(QRect(1310, 60, 51, 50))
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
        self.notif_button = QToolButton(information_earnings)
        self.notif_button.setObjectName(u"notif_button")
        self.notif_button.setGeometry(QRect(1240, 60, 51, 50))
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
        self.toggle_switch = QWidget(information_earnings)
        self.toggle_switch.setObjectName(u"toggle_switch")
        self.toggle_switch.setGeometry(QRect(1135, 65, 91, 21))
        self.toggle_switch.setStyleSheet(u"background: transparent;\n"
"")
        self.workerM_label = QLabel(information_earnings)
        self.workerM_label.setObjectName(u"workerM_label")
        self.workerM_label.setGeometry(QRect(1140, 100, 81, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(9)
        font2.setBold(False)
        self.workerM_label.setFont(font2)
        self.workerM_label.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.ppayouts_label = QLabel(information_earnings)
        self.ppayouts_label.setObjectName(u"ppayouts_label")
        self.ppayouts_label.setGeometry(QRect(800, 280, 131, 16))
        self.ppayouts_label.setFont(font2)
        self.ppayouts_label.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.etoday_label = QLabel(information_earnings)
        self.etoday_label.setObjectName(u"etoday_label")
        self.etoday_label.setGeometry(QRect(800, 260, 131, 16))
        self.etoday_label.setFont(font2)
        self.etoday_label.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.acc_number = QLabel(information_earnings)
        self.acc_number.setObjectName(u"acc_number")
        self.acc_number.setGeometry(QRect(120, 380, 121, 16))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        self.acc_number.setFont(font3)
        self.acc_number.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.accnum_label = QLabel(information_earnings)
        self.accnum_label.setObjectName(u"accnum_label")
        self.accnum_label.setGeometry(QRect(120, 400, 181, 16))
        self.accnum_label.setFont(font3)
        self.accnum_label.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.current_con = QLabel(information_earnings)
        self.current_con.setObjectName(u"current_con")
        self.current_con.setGeometry(QRect(780, 130, 291, 320))
        self.current_con.setStyleSheet(u"QLabel {\n"
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
        self.trans_con = QLabel(information_earnings)
        self.trans_con.setObjectName(u"trans_con")
        self.trans_con.setGeometry(QRect(100, 470, 351, 321))
        self.trans_con.setStyleSheet(u"QLabel {\n"
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
        self.revenue_con = QLabel(information_earnings)
        self.revenue_con.setObjectName(u"revenue_con")
        self.revenue_con.setGeometry(QRect(470, 470, 601, 321))
        self.revenue_con.setStyleSheet(u"QLabel {\n"
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
        self.tvp_con = QLabel(information_earnings)
        self.tvp_con.setObjectName(u"tvp_con")
        self.tvp_con.setGeometry(QRect(1090, 130, 311, 661))
        self.tvp_con.setStyleSheet(u"QLabel {\n"
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
        self.amount_label = QLabel(information_earnings)
        self.amount_label.setObjectName(u"amount_label")
        self.amount_label.setGeometry(QRect(120, 190, 251, 31))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(24)
        font4.setBold(True)
        self.amount_label.setFont(font4)
        self.amount_label.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.inc_wid = QWidget(information_earnings)
        self.inc_wid.setObjectName(u"inc_wid")
        self.inc_wid.setGeometry(QRect(800, 230, 21, 21))
        self.inc_wid.setStyleSheet(u"background: transparent;\n"
"")
        self.inc_label = QLabel(information_earnings)
        self.inc_label.setObjectName(u"inc_label")
        self.inc_label.setGeometry(QRect(840, 220, 31, 31))
        self.inc_label.setFont(font1)
        self.inc_label.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.currentp_label = QLabel(information_earnings)
        self.currentp_label.setObjectName(u"currentp_label")
        self.currentp_label.setGeometry(QRect(900, 220, 61, 31))
        self.currentp_label.setFont(font1)
        self.currentp_label.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.earning_label = QLabel(information_earnings)
        self.earning_label.setObjectName(u"earning_label")
        self.earning_label.setGeometry(QRect(490, 180, 191, 31))
        self.earning_label.setFont(font4)
        self.earning_label.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.avgearning_label = QLabel(information_earnings)
        self.avgearning_label.setObjectName(u"avgearning_label")
        self.avgearning_label.setGeometry(QRect(490, 380, 151, 16))
        self.avgearning_label.setFont(font3)
        self.avgearning_label.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.wavg_label = QLabel(information_earnings)
        self.wavg_label.setObjectName(u"wavg_label")
        self.wavg_label.setGeometry(QRect(490, 400, 151, 16))
        self.wavg_label.setFont(font3)
        self.wavg_label.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.current_earning = QLabel(information_earnings)
        self.current_earning.setObjectName(u"current_earning")
        self.current_earning.setGeometry(QRect(800, 140, 141, 31))
        self.current_earning.setFont(font1)
        self.current_earning.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.cearning_label = QLabel(information_earnings)
        self.cearning_label.setObjectName(u"cearning_label")
        self.cearning_label.setGeometry(QRect(800, 180, 191, 31))
        self.cearning_label.setFont(font4)
        self.cearning_label.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.current_chart = QWidget(information_earnings)
        self.current_chart.setObjectName(u"current_chart")
        self.current_chart.setGeometry(QRect(800, 310, 251, 121))
        self.current_chart.setStyleSheet(u"background: transparent;\n"
"")
        self.transactions = QLabel(information_earnings)
        self.transactions.setObjectName(u"transactions")
        self.transactions.setGeometry(QRect(120, 480, 121, 31))
        self.transactions.setFont(font1)
        self.transactions.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"\n"
"")
        self.revenue = QLabel(information_earnings)
        self.revenue.setObjectName(u"revenue")
        self.revenue.setGeometry(QRect(500, 480, 121, 31))
        self.revenue.setFont(font1)
        self.revenue.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.totalv_performance = QLabel(information_earnings)
        self.totalv_performance.setObjectName(u"totalv_performance")
        self.totalv_performance.setGeometry(QRect(1170, 140, 161, 31))
        self.totalv_performance.setFont(font1)
        self.totalv_performance.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.tvp_chart = QWidget(information_earnings)
        self.tvp_chart.setObjectName(u"tvp_chart")
        self.tvp_chart.setGeometry(QRect(1140, 190, 224, 224))
        self.tvp_chart.setStyleSheet(u"background: transparent;\n"
"")
        self.tjexe_label = QLabel(information_earnings)
        self.tjexe_label.setObjectName(u"tjexe_label")
        self.tjexe_label.setGeometry(QRect(1180, 430, 151, 16))
        self.tjexe_label.setFont(font3)
        self.tjexe_label.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.tearning_label = QLabel(information_earnings)
        self.tearning_label.setObjectName(u"tearning_label")
        self.tearning_label.setGeometry(QRect(1190, 450, 141, 16))
        self.tearning_label.setFont(font3)
        self.tearning_label.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.ajsrate_label = QLabel(information_earnings)
        self.ajsrate_label.setObjectName(u"ajsrate_label")
        self.ajsrate_label.setGeometry(QRect(1160, 470, 191, 16))
        self.ajsrate_label.setFont(font3)
        self.ajsrate_label.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.revenue_chart = QWidget(information_earnings)
        self.revenue_chart.setObjectName(u"revenue_chart")
        self.revenue_chart.setGeometry(QRect(500, 580, 541, 181))
        self.revenue_chart.setStyleSheet(u"background: transparent;\n"
"")
        self.trevenue_label = QLabel(information_earnings)
        self.trevenue_label.setObjectName(u"trevenue_label")
        self.trevenue_label.setGeometry(QRect(510, 520, 151, 16))
        self.trevenue_label.setFont(font3)
        self.trevenue_label.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.yrevenue_label = QLabel(information_earnings)
        self.yrevenue_label.setObjectName(u"yrevenue_label")
        self.yrevenue_label.setGeometry(QRect(510, 540, 171, 16))
        self.yrevenue_label.setFont(font3)
        self.yrevenue_label.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.rweek_label = QLabel(information_earnings)
        self.rweek_label.setObjectName(u"rweek_label")
        self.rweek_label.setGeometry(QRect(730, 510, 161, 16))
        self.rweek_label.setFont(font3)
        self.rweek_label.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.rlweek_label = QLabel(information_earnings)
        self.rlweek_label.setObjectName(u"rlweek_label")
        self.rlweek_label.setGeometry(QRect(730, 530, 161, 16))
        self.rlweek_label.setFont(font3)
        self.rlweek_label.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.lrevenue_label = QLabel(information_earnings)
        self.lrevenue_label.setObjectName(u"lrevenue_label")
        self.lrevenue_label.setGeometry(QRect(730, 550, 171, 16))
        self.lrevenue_label.setFont(font3)
        self.lrevenue_label.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"\n"
"")
        self.trans_tablev = QTableView(information_earnings)
        self.trans_tablev.setObjectName(u"trans_tablev")
        self.trans_tablev.setGeometry(QRect(120, 520, 311, 251))
        self.trans_tablev.setStyleSheet(u"QTableView {\n"
"    background: transparent;\n"
"    border: 1px solid #ffffff;\n"
"    border-radius: 20px;   /* adjust radius to your liking */\n"
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
        self.current_con.raise_()
        self.trans_con.raise_()
        self.earning_con.raise_()
        self.horizontalLayoutWidget.raise_()
        self.logo.raise_()
        self.earning_rate.raise_()
        self.verticalLayoutWidget.raise_()
        self.settings_bt.raise_()
        self.balance_con.raise_()
        self.balance_details.raise_()
        self.eline_chart.raise_()
        self.prof_button.raise_()
        self.notif_button.raise_()
        self.toggle_switch.raise_()
        self.workerM_label.raise_()
        self.ppayouts_label.raise_()
        self.etoday_label.raise_()
        self.acc_number.raise_()
        self.accnum_label.raise_()
        self.revenue_con.raise_()
        self.tvp_con.raise_()
        self.amount_label.raise_()
        self.inc_wid.raise_()
        self.inc_label.raise_()
        self.currentp_label.raise_()
        self.earning_label.raise_()
        self.avgearning_label.raise_()
        self.wavg_label.raise_()
        self.current_earning.raise_()
        self.cearning_label.raise_()
        self.current_chart.raise_()
        self.transactions.raise_()
        self.revenue.raise_()
        self.totalv_performance.raise_()
        self.tvp_chart.raise_()
        self.tjexe_label.raise_()
        self.tearning_label.raise_()
        self.ajsrate_label.raise_()
        self.revenue_chart.raise_()
        self.trevenue_label.raise_()
        self.yrevenue_label.raise_()
        self.rweek_label.raise_()
        self.rlweek_label.raise_()
        self.lrevenue_label.raise_()
        self.trans_tablev.raise_()

        self.retranslateUi(information_earnings)

        QMetaObject.connectSlotsByName(information_earnings)
    # setupUi

    def retranslateUi(self, information_earnings):
        information_earnings.setWindowTitle(QCoreApplication.translate("information_earnings", u"CrowdCloud", None))
        self.logo.setText("")
        self.earning_rate.setText(QCoreApplication.translate("information_earnings", u"Earning Rate", None))
        self.earning_con.setText("")
        self.dash_bt.setText("")
        self.sys_bt.setText("")
        self.job_bt.setText("")
        self.earning_bt.setText("")
        self.settings_bt.setText("")
        self.balance_con.setText("")
        self.balance_details.setText(QCoreApplication.translate("information_earnings", u"Balance Details", None))
        self.prof_button.setText("")
        self.notif_button.setText("")
        self.workerM_label.setText(QCoreApplication.translate("information_earnings", u"Worker Mode", None))
        self.ppayouts_label.setText(QCoreApplication.translate("information_earnings", u"Pending payouts: 650.25", None))
        self.etoday_label.setText(QCoreApplication.translate("information_earnings", u"Earning Today: 450.00", None))
        self.acc_number.setText(QCoreApplication.translate("information_earnings", u"Account Number", None))
        self.accnum_label.setText(QCoreApplication.translate("information_earnings", u"014815685355014815685355", None))
        self.current_con.setText("")
        self.trans_con.setText("")
        self.revenue_con.setText("")
        self.tvp_con.setText("")
        self.amount_label.setText(QCoreApplication.translate("information_earnings", u"PHP 30,000.25", None))
        self.inc_label.setText(QCoreApplication.translate("information_earnings", u"-- --", None))
        self.currentp_label.setText(QCoreApplication.translate("information_earnings", u"-- --", None))
        self.earning_label.setText(QCoreApplication.translate("information_earnings", u"PHP 125/hr", None))
        self.avgearning_label.setText(QCoreApplication.translate("information_earnings", u"Average Earning: 50/hr", None))
        self.wavg_label.setText(QCoreApplication.translate("information_earnings", u"Weekly Average: 110/hr", None))
        self.current_earning.setText(QCoreApplication.translate("information_earnings", u"Current Earnings", None))
        self.cearning_label.setText(QCoreApplication.translate("information_earnings", u"PHP 890.93", None))
        self.transactions.setText(QCoreApplication.translate("information_earnings", u"Transactions", None))
        self.revenue.setText(QCoreApplication.translate("information_earnings", u"Revenue", None))
        self.totalv_performance.setText(QCoreApplication.translate("information_earnings", u"Total View Performance", None))
        self.tjexe_label.setText(QCoreApplication.translate("information_earnings", u"Total Jobs Executed: 1234", None))
        self.tearning_label.setText(QCoreApplication.translate("information_earnings", u"Total Earnings: 512.456", None))
        self.ajsrate_label.setText(QCoreApplication.translate("information_earnings", u"Average Job Success Rate: 88%", None))
        self.trevenue_label.setText(QCoreApplication.translate("information_earnings", u"Today's revenue: 700.00", None))
        self.yrevenue_label.setText(QCoreApplication.translate("information_earnings", u"Yesterday's revenue: 675.24", None))
        self.rweek_label.setText(QCoreApplication.translate("information_earnings", u"Revenue this week: 1123.75", None))
        self.rlweek_label.setText(QCoreApplication.translate("information_earnings", u"Revenue last week: 7400.89", None))
        self.lrevenue_label.setText(QCoreApplication.translate("information_earnings", u"Lifetime revenue: 11,345.56", None))
    # retranslateUi

