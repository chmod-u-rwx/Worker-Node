from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

class UiSignupLast(object):
    def setupUi(self, signup_page4):
        if not signup_page4.objectName():
            signup_page4.setObjectName(u"signup_page4")
        signup_page4.resize(1440, 810)
        signup_page4.setMinimumSize(QSize(1440, 810))
        signup_page4.setMaximumSize(QSize(1440, 810))
        self.bg_label = QLabel(signup_page4)
        self.bg_label.setPixmap(QPixmap("src/worker_node_ui/resources/images/gen_dashboard.png"))
        self.bg_label.setScaledContents(True)  # scales image with window
        self.bg_label.setGeometry(0, 0, signup_page4.width(), signup_page4.height())
        self.bg_label.lower()  # send to back
        self.horizontalLayoutWidget = QWidget(signup_page4)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 2, 2))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.logo = QLabel(signup_page4)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(280, 320, 109, 88))
        self.logo.setAutoFillBackground(False)
        self.logo.setStyleSheet(u"background: transparent;")
        self.logo.setPixmap(QPixmap("src/worker_node_ui/resources/images/signup1logo.png"))
        self.get_started = QLabel(signup_page4)
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
        self.fast_label = QLabel(signup_page4)
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
        self.dashboard_button = QPushButton(signup_page4)
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
        self.info_label = QLabel(signup_page4)
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
        self.info_label_2 = QLabel(signup_page4)
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

        self.retranslateUi(signup_page4)

        QMetaObject.connectSlotsByName(signup_page4)
    # setupUi

    def retranslateUi(self, signup_page4):
        signup_page4.setWindowTitle(QCoreApplication.translate("signup_page4", u"CrowdCloud", None))
        self.logo.setText("")
        self.get_started.setText(QCoreApplication.translate("signup_page4", u"Get Started with Us", None))
        self.fast_label.setText(QCoreApplication.translate("signup_page4", u"That was fast", None))
        self.dashboard_button.setText(QCoreApplication.translate("signup_page4", u"To Dashboard", None))
        self.info_label.setText(QCoreApplication.translate("signup_page4", u"Thank you for signing up to CrowdCloud. To start earning please press the button below it will redirect you to your CrowdCloud Worker Node Dashboard", None))
        self.info_label_2.setText(QCoreApplication.translate("signup_page4", u"Automatic redirect in 3s", None))
    # retranslateUi

