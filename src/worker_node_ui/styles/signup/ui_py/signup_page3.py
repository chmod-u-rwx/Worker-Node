from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSlider, QWidget)

class UiSignupAlmost(object):
    def setupUi(self, signup_page3):
        if not signup_page3.objectName():
            signup_page3.setObjectName(u"signup_page3")
        signup_page3.resize(1440, 810)
        signup_page3.setMinimumSize(QSize(1440, 810))
        signup_page3.setMaximumSize(QSize(1440, 810))
        self.bg_label = QLabel(signup_page3)
        self.bg_label.setPixmap(QPixmap("src/worker_node_ui/resources/images/gen_dashboard.png"))
        self.bg_label.setScaledContents(True)  # scales image with window
        self.bg_label.setGeometry(0, 0, signup_page3.width(), signup_page3.height())
        self.bg_label.lower()  # send to back
        self.horizontalLayoutWidget = QWidget(signup_page3)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 2, 2))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.logo = QLabel(signup_page3)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(280, 320, 109, 88))
        self.logo.setAutoFillBackground(False)
        self.logo.setStyleSheet(u"background: transparent;")
        self.logo.setPixmap(QPixmap("src/worker_node_ui/resources/images/signup1logo.png"))
        self.get_started = QLabel(signup_page3)
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
        self.almost_label = QLabel(signup_page3)
        self.almost_label.setObjectName(u"almost_label")
        self.almost_label.setGeometry(QRect(970, 170, 221, 31))
        font1 = QFont()
        font1.setFamilies([u"Century Gothic"])
        font1.setPointSize(26)
        font1.setBold(True)
        self.almost_label.setFont(font1)
        self.almost_label.setStyleSheet(u"background: transparent;\n"
"color: white;\n"
"\n"
"")
        self.next1_button = QPushButton(signup_page3)
        self.next1_button.setObjectName(u"next1_button")
        self.next1_button.setGeometry(QRect(1060, 590, 231, 41))
        font2 = QFont()
        font2.setFamilies([u"Century Gothic"])
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setItalic(False)
        self.next1_button.setFont(font2)
        self.next1_button.setStyleSheet(u"QPushButton {\n"
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
        self.cache_label = QLabel(signup_page3)
        self.cache_label.setObjectName(u"cache_label")
        self.cache_label.setGeometry(QRect(810, 280, 341, 16))
        font3 = QFont()
        font3.setFamilies([u"Century Gothic"])
        font3.setPointSize(10)
        font3.setBold(False)
        self.cache_label.setFont(font3)
        self.cache_label.setStyleSheet(u"color: white;\n"
"background-color: transparent;\n"
"")
        self.core_label = QLabel(signup_page3)
        self.core_label.setObjectName(u"core_label")
        self.core_label.setGeometry(QRect(810, 380, 381, 16))
        self.core_label.setFont(font3)
        self.core_label.setStyleSheet(u"color: white;\n"
"background-color: transparent;\n"
"")
        self.back_button = QPushButton(signup_page3)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setGeometry(QRect(810, 590, 241, 41))
        self.back_button.setFont(font2)
        self.back_button.setStyleSheet(u"QPushButton {\n"
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
        self.info_label = QLabel(signup_page3)
        self.info_label.setObjectName(u"info_label")
        self.info_label.setGeometry(QRect(870, 650, 371, 16))
        self.info_label.setFont(font3)
        self.info_label.setStyleSheet(u"color: white;\n"
"background-color: transparent;\n"
"")
        self.cores_max_label = QLabel(signup_page3)
        self.cores_max_label.setObjectName(u"cores_max_label")
        self.cores_max_label.setGeometry(QRect(1235, 410, 61, 21))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cores_max_label.sizePolicy().hasHeightForWidth())
        self.cores_max_label.setSizePolicy(sizePolicy)
        self.cores_max_label.setStyleSheet(u"QLabel {\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    font-family: \"Century Gothic\";\n"
"    color: #ffffff;\n"
"    background-color: transparent;\n"
"}\n"
"")
        self.cores_min_label = QLabel(signup_page3)
        self.cores_min_label.setObjectName(u"cores_min_label")
        self.cores_min_label.setGeometry(QRect(910, 410, 41, 21))
        sizePolicy.setHeightForWidth(self.cores_min_label.sizePolicy().hasHeightForWidth())
        self.cores_min_label.setSizePolicy(sizePolicy)
        self.cores_min_label.setStyleSheet(u"QLabel {\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    font-family: \"Century Gothic\";\n"
"    color: #ffffff;\n"
"    background-color: transparent;\n"
"}\n"
"")
        self.disk_slider = QSlider(signup_page3)
        self.disk_slider.setObjectName(u"disk_slider")
        self.disk_slider.setGeometry(QRect(910, 430, 381, 21))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(3)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.disk_slider.sizePolicy().hasHeightForWidth())
        self.disk_slider.setSizePolicy(sizePolicy1)
        self.disk_slider.setStyleSheet(u"QSlider {\n"
"    background: transparent;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"    height: 8px;\n"
"    background: #D9D9D9;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: #9C7DFF;   /* Violet filled part */\n"
"    border: 1px solid #777777;\n"
"    height: 8px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: #D9D9D9;   /* Unfilled part */\n"
"    border: 1px solid #777777;\n"
"    height: 8px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    border: 1px solid #5a2a83;\n"
"    width: 18px;\n"
"    border-radius: 9px;\n"
"	margin: -5px 0px;  \n"
"    background: qradialgradient(\n"
"        cx: 0.5, cy: 0.5, radius: 0.8,\n"
"        fx: 0.5, fy: 0.5,\n"
"        stop: 0 #9C7DFF,        /* Purple center */\n"
"        stop: 0.6 #9C7DFF,\n"
"        stop: 1 transparent     /* Fade to transparent */\n"
"    );\n"
"}\n"
"")
        self.disk_slider.setMaximum(100)
        self.disk_slider.setValue(50)
        self.disk_slider.setOrientation(Qt.Orientation.Horizontal)
        self.disk_line = QLineEdit(signup_page3)
        self.disk_line.setObjectName(u"disk_line")
        self.disk_line.setGeometry(QRect(810, 410, 91, 41))
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.disk_line.sizePolicy().hasHeightForWidth())
        self.disk_line.setSizePolicy(sizePolicy2)
        font4 = QFont()
        font4.setFamilies([u"Century Gothic"])
        self.disk_line.setFont(font4)
        self.disk_line.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #ffffff;   /* thickness + color */\n"
"    border-radius: 12px;         /* rounded corners */\n"
"    padding: 6px;\n"
"    font-size: 14px;\n"
"	font-family: \"Century Gothic\";\n"
"	color: #ffffff;\n"
"	background-color: transparent;\n"
"	qproperty-alignment: 'AlignCenter';\n"
"}\n"
"")
        self.reco_label = QLabel(signup_page3)
        self.reco_label.setObjectName(u"reco_label")
        self.reco_label.setGeometry(QRect(910, 450, 191, 16))
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.reco_label.sizePolicy().hasHeightForWidth())
        self.reco_label.setSizePolicy(sizePolicy3)
        self.reco_label.setFont(font3)
        self.reco_label.setStyleSheet(u"color: #a2a1a1;\n"
"background-color: transparent;\n"
"\n"
"")
        self.cache_line = QLineEdit(signup_page3)
        self.cache_line.setObjectName(u"cache_line")
        self.cache_line.setGeometry(QRect(810, 310, 481, 41))
        self.cache_line.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgba(20, 20, 50, 10);\n"
"    border: 1px solid rgba(255, 255, 255, 0.3);\n"
"    border-radius: 7px;\n"
"    padding: 8px;\n"
"    color: white;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #7D5FFF;\n"
"}\n"
"")
        self.pushButton = QPushButton(signup_page3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(900, 280, 91, 21))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	font: bold pt \"Century Gothic\";\n"
"    background-color: #00031F;   /* button fill color */\n"
"    color: white;                /* text color */\n"
"    border: 1px solid #340561;   /* stroke/border */\n"
"    border-radius: 10px;         /* corner radius */   \n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #6A0DBF;   /* hover color */\n"
"}\n"
"")

        self.retranslateUi(signup_page3)

        QMetaObject.connectSlotsByName(signup_page3)
    # setupUi

    def retranslateUi(self, signup_page3):
        signup_page3.setWindowTitle(QCoreApplication.translate("signup_page3", u"CrowdCloud", None))
        self.logo.setText("")
        self.get_started.setText(QCoreApplication.translate("signup_page3", u"Get Started with Us", None))
        self.almost_label.setText(QCoreApplication.translate("signup_page3", u"Almost There", None))
        self.next1_button.setText(QCoreApplication.translate("signup_page3", u"Next", None))
        self.cache_label.setText(QCoreApplication.translate("signup_page3", u"Cache Path", None))
        self.core_label.setText(QCoreApplication.translate("signup_page3", u"How much disk usage would you like to allocate as cache", None))
        self.back_button.setText(QCoreApplication.translate("signup_page3", u"Back", None))
        self.info_label.setText(QCoreApplication.translate("signup_page3", u"You could always change these later in the setting page", None))
        self.cores_max_label.setText(QCoreApplication.translate("signup_page3", u"1600MB", None))
        self.cores_min_label.setText(QCoreApplication.translate("signup_page3", u"0 MB", None))
        self.disk_line.setText(QCoreApplication.translate("signup_page3", u"2", None))
        self.reco_label.setText(QCoreApplication.translate("signup_page3", u"recommended: 500 - 2000MB", None))
        self.cache_line.setInputMask("")
        self.cache_line.setText("")
        self.cache_line.setPlaceholderText(QCoreApplication.translate("signup_page3", u"/tmp/crowdcloud", None))
        self.pushButton.setText(QCoreApplication.translate("signup_page3", u"Browse", None))
    # retranslateUi

