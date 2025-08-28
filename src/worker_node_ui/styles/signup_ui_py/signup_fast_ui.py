from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize)
from PySide6.QtGui import (QFont, QPixmap)
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QPushButton, QWidget)

class Ui_signup_toDashboard(object):
    def setupUi(self, disk_question):
        if not disk_question.objectName():
            disk_question.setObjectName(u"disk_question")
        disk_question.resize(1440, 810)
        disk_question.setMinimumSize(QSize(1440, 810))
        disk_question.setMaximumSize(QSize(1440, 810))
        self.centralwidget = QWidget(disk_question)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMinimumSize(QSize(1440, 810))
        self.centralwidget.setMaximumSize(QSize(1440, 810))
        self.centralwidget.setStyleSheet("background-image: url('src/worker_node_ui/resources/images/signin_background.png');")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 2, 2))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(280, 320, 109, 88))
        self.logo.setAutoFillBackground(False)
        self.logo.setStyleSheet(u"background: transparent;")
        self.logo.setPixmap(QPixmap("src/worker_node_ui/resources/images/signup1logo.png"))
        self.get_started = QLabel(self.centralwidget)
        self.get_started.setObjectName(u"get_started")
        self.get_started.setGeometry(QRect(170, 410, 333, 88))
        font = QFont()
        font.setFamilies([u"Century Gothic"])
        font.setPointSize(28)
        font.setBold(True)
        self.get_started.setFont(font)
        self.get_started.setStyleSheet(u"background: transparent;\n"
"color: white;\n"
"\n"
"")
        self.fast_label = QLabel(self.centralwidget)
        self.fast_label.setObjectName(u"fast_label")
        self.fast_label.setGeometry(QRect(970, 290, 221, 31))
        font1 = QFont()
        font1.setFamilies([u"Century Gothic"])
        font1.setPointSize(26)
        font1.setBold(True)
        self.fast_label.setFont(font1)
        self.fast_label.setStyleSheet(u"background: transparent;\n"
"color: white;\n"
"\n"
"")
        self.dashboard_button = QPushButton(self.centralwidget)
        self.dashboard_button.setObjectName(u"dashboard_button")
        self.dashboard_button.setGeometry(QRect(870, 580, 421, 41))
        font2 = QFont()
        font2.setFamilies([u"Century Gothic"])
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setItalic(False)
        self.dashboard_button.setFont(font2)
        self.dashboard_button.setStyleSheet(u"QPushButton {\n"
"	font: bold 12pt \"Century Gothic\";\n"
"    background-color: #00031F;   /* button fill color */\n"
"    color: white;                /* text color */\n"
"    border: 1px solid #340561;   /* stroke/border */\n"
"    border-radius: 10px;         /* corner radius */\n"
"    padding: 6px 12px;           /* optional padding */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #6A0DBF;   /* hover color */\n"
"}\n"
"\n"
"")
        self.info_label = QLabel(self.centralwidget)
        self.info_label.setObjectName(u"info_label")
        self.info_label.setGeometry(QRect(870, 360, 411, 111))
        font3 = QFont()
        font3.setFamilies([u"Century Gothic"])
        font3.setPointSize(12)
        font3.setBold(False)
        self.info_label.setFont(font3)
        self.info_label.setStyleSheet(u"color: white;\n"
"background-color: transparent;\n"
"")
        self.info_label.setWordWrap(True)
        self.info_label_2 = QLabel(self.centralwidget)
        self.info_label_2.setObjectName(u"info_label_2")
        self.info_label_2.setGeometry(QRect(1000, 550, 161, 16))
        font4 = QFont()
        font4.setFamilies([u"Century Gothic"])
        font4.setPointSize(10)
        font4.setBold(False)
        self.info_label_2.setFont(font4)
        self.info_label_2.setStyleSheet(u"color: #a2a1a1;\n"
"background-color: transparent;\n"
"")
        self.info_label_2.setWordWrap(True)
        disk_question.setCentralWidget(self.centralwidget)

        self.retranslateUi(disk_question)

        QMetaObject.connectSlotsByName(disk_question)
    # setupUi

    def retranslateUi(self, disk_question):
        disk_question.setWindowTitle(QCoreApplication.translate("disk_question", u"CrowdCloud", None))
        self.logo.setText("")
        self.get_started.setText(QCoreApplication.translate("disk_question", u"Get Started with Us", None))
        self.fast_label.setText(QCoreApplication.translate("disk_question", u"That was fast", None))
        self.dashboard_button.setText(QCoreApplication.translate("disk_question", u"To Dashboard", None))
        self.info_label.setText(QCoreApplication.translate("disk_question", u"Thank you for signing up to CrowdCloud. To start earning please press the button below it will redirect you to your CrowdCloud Worker Node Dashboard", None))
        self.info_label_2.setText(QCoreApplication.translate("disk_question", u"Automatic redirect in 3s", None))
    # retranslateUi

