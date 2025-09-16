from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSlider, QWidget)

class UiSignupTell(object):
    def setupUi(self, signup_page2):
        if not signup_page2.objectName():
            signup_page2.setObjectName(u"signup_page2")
        signup_page2.resize(1440, 810)
        signup_page2.setMinimumSize(QSize(1440, 810))
        signup_page2.setMaximumSize(QSize(1440, 810))
        self.bg_label = QLabel(signup_page2)
        self.bg_label.setPixmap(QPixmap("src/worker_node_ui/resources/images/gen_dashboard.png"))
        self.bg_label.setScaledContents(True)  # scales image with window
        self.bg_label.setGeometry(0, 0, signup_page2.width(), signup_page2.height())
        self.bg_label.lower()  # send to back
        self.horizontalLayoutWidget = QWidget(signup_page2)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 2, 2))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.logo = QLabel(signup_page2)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(280, 320, 109, 88))
        self.logo.setAutoFillBackground(False)
        self.logo.setStyleSheet(u"background: transparent;")
        self.logo.setPixmap(QPixmap("src/worker_node_ui/resources/images/signup1logo.png"))
        self.get_started = QLabel(signup_page2)
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
        self.create_label = QLabel(signup_page2)
        self.create_label.setObjectName(u"create_label")
        self.create_label.setGeometry(QRect(910, 140, 601, 31))
        font1 = QFont()
        font1.setFamilies([u"Century Gothic"])
        font1.setPointSize(26)
        font1.setBold(True)
        self.create_label.setFont(font1)
        self.create_label.setStyleSheet(u"background: transparent;\n"
"color: white;\n"
"\n"
"")
        self.next1_button = QPushButton(signup_page2)
        self.next1_button.setObjectName(u"next1_button")
        self.next1_button.setGeometry(QRect(1080, 590, 211, 41))
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
        self.cpu_label = QLabel(signup_page2)
        self.cpu_label.setObjectName(u"cpu_label")
        self.cpu_label.setGeometry(QRect(810, 280, 341, 16))
        font3 = QFont()
        font3.setFamilies([u"Century Gothic"])
        font3.setPointSize(10)
        font3.setBold(False)
        self.cpu_label.setFont(font3)
        self.cpu_label.setStyleSheet(u"color: white;\n"
"background-color: transparent;\n"
"")
        self.create_label_2 = QLabel(signup_page2)
        self.create_label_2.setObjectName(u"create_label_2")
        self.create_label_2.setGeometry(QRect(980, 180, 171, 31))
        self.create_label_2.setFont(font1)
        self.create_label_2.setStyleSheet(u"background: transparent;\n"
"color: white;\n"
"\n"
"")
        self.cpu_slider = QSlider(signup_page2)
        self.cpu_slider.setObjectName(u"cpu_slider")
        self.cpu_slider.setGeometry(QRect(910, 330, 381, 21))
        self.cpu_slider.setStyleSheet(u"QSlider {\n"
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
        self.cpu_slider.setMaximum(100)
        self.cpu_slider.setValue(50)
        self.cpu_slider.setOrientation(Qt.Orientation.Horizontal)
        self.core_label = QLabel(signup_page2)
        self.core_label.setObjectName(u"core_label")
        self.core_label.setGeometry(QRect(810, 380, 341, 16))
        self.core_label.setFont(font3)
        self.core_label.setStyleSheet(u"color: white;\n"
"background-color: transparent;\n"
"")
        self.ram_label = QLabel(signup_page2)
        self.ram_label.setObjectName(u"ram_label")
        self.ram_label.setGeometry(QRect(810, 480, 341, 16))
        self.ram_label.setFont(font3)
        self.ram_label.setStyleSheet(u"color: white;\n"
"background-color: transparent;\n"
"")
        self.back_button = QPushButton(signup_page2)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setGeometry(QRect(840, 590, 221, 41))
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
        self.cpu_lineedit = QLineEdit(signup_page2)
        self.cpu_lineedit.setObjectName(u"cpu_lineedit")
        self.cpu_lineedit.setGeometry(QRect(830, 310, 51, 41))
        font4 = QFont()
        font4.setFamilies([u"Century Gothic"])
        self.cpu_lineedit.setFont(font4)
        self.cpu_lineedit.setStyleSheet(u"QLineEdit {\n"
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
        self.cpu_min_label = QLabel(signup_page2)
        self.cpu_min_label.setObjectName(u"cpu_min_label")
        self.cpu_min_label.setGeometry(QRect(910, 310, 16, 21))
        self.cpu_min_label.setStyleSheet(u"QLabel {\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    font-family: \"Century Gothic\";\n"
"    color: #ffffff;\n"
"    background-color: transparent;\n"
"}\n"
"")
        self.cpu_max_label = QLabel(signup_page2)
        self.cpu_max_label.setObjectName(u"cpu_max_label")
        self.cpu_max_label.setGeometry(QRect(1260, 310, 31, 21))
        self.cpu_max_label.setStyleSheet(u"QLabel {\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    font-family: \"Century Gothic\";\n"
"    color: #ffffff;\n"
"    background-color: transparent;\n"
"}\n"
"")
        self.info_label = QLabel(signup_page2)
        self.info_label.setObjectName(u"info_label")
        self.info_label.setGeometry(QRect(840, 650, 441, 16))
        self.info_label.setFont(font3)
        self.info_label.setStyleSheet(u"color: white;\n"
"background-color: transparent;\n"
"")
        self.cores_max_label = QLabel(signup_page2)
        self.cores_max_label.setObjectName(u"cores_max_label")
        self.cores_max_label.setGeometry(QRect(1280, 410, 16, 21))
        self.cores_max_label.setStyleSheet(u"QLabel {\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    font-family: \"Century Gothic\";\n"
"    color: #ffffff;\n"
"    background-color: transparent;\n"
"}\n"
"")
        self.cores_min_label = QLabel(signup_page2)
        self.cores_min_label.setObjectName(u"cores_min_label")
        self.cores_min_label.setGeometry(QRect(910, 410, 16, 21))
        self.cores_min_label.setStyleSheet(u"QLabel {\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    font-family: \"Century Gothic\";\n"
"    color: #ffffff;\n"
"    background-color: transparent;\n"
"}\n"
"")
        self.cores_slider = QSlider(signup_page2)
        self.cores_slider.setObjectName(u"cores_slider")
        self.cores_slider.setGeometry(QRect(910, 430, 381, 21))
        self.cores_slider.setStyleSheet(u"QSlider {\n"
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
        self.cores_slider.setMaximum(100)
        self.cores_slider.setValue(50)
        self.cores_slider.setOrientation(Qt.Orientation.Horizontal)
        self.cores_lineedit = QLineEdit(signup_page2)
        self.cores_lineedit.setObjectName(u"cores_lineedit")
        self.cores_lineedit.setGeometry(QRect(830, 410, 51, 41))
        self.cores_lineedit.setFont(font4)
        self.cores_lineedit.setStyleSheet(u"QLineEdit {\n"
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
        self.ram_min_label = QLabel(signup_page2)
        self.ram_min_label.setObjectName(u"ram_min_label")
        self.ram_min_label.setGeometry(QRect(910, 510, 31, 21))
        self.ram_min_label.setStyleSheet(u"QLabel {\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    font-family: \"Century Gothic\";\n"
"    color: #ffffff;\n"
"    background-color: transparent;\n"
"}\n"
"")
        self.ram_slider = QSlider(signup_page2)
        self.ram_slider.setObjectName(u"ram_slider")
        self.ram_slider.setGeometry(QRect(910, 530, 381, 21))
        self.ram_slider.setStyleSheet(u"QSlider {\n"
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
        self.ram_slider.setMaximum(100)
        self.ram_slider.setValue(50)
        self.ram_slider.setOrientation(Qt.Orientation.Horizontal)
        self.ram_lineedit = QLineEdit(signup_page2)
        self.ram_lineedit.setObjectName(u"ram_lineedit")
        self.ram_lineedit.setGeometry(QRect(820, 510, 81, 41))
        self.ram_lineedit.setFont(font4)
        self.ram_lineedit.setStyleSheet(u"QLineEdit {\n"
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
        self.ram_max_label = QLabel(signup_page2)
        self.ram_max_label.setObjectName(u"ram_max_label")
        self.ram_max_label.setGeometry(QRect(1230, 510, 61, 21))
        self.ram_max_label.setStyleSheet(u"QLabel {\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    font-family: \"Century Gothic\";\n"
"    color: #ffffff;\n"
"    background-color: transparent;\n"
"}\n"
"")

        self.retranslateUi(signup_page2)

        QMetaObject.connectSlotsByName(signup_page2)
    # setupUi

    def retranslateUi(self, signup_page2):
        signup_page2.setWindowTitle(QCoreApplication.translate("signup_page2", u"CrowdCloud", None))
        self.logo.setText("")
        self.get_started.setText(QCoreApplication.translate("signup_page2", u"Get Started with Us", None))
        self.create_label.setText(QCoreApplication.translate("signup_page2", u"Tell us a little more", None))
        self.next1_button.setText(QCoreApplication.translate("signup_page2", u"Next", None))
        self.cpu_label.setText(QCoreApplication.translate("signup_page2", u"How much CPU percentage would you want to use", None))
        self.create_label_2.setText(QCoreApplication.translate("signup_page2", u"about you", None))
        self.core_label.setText(QCoreApplication.translate("signup_page2", u"How many cores would you want to use", None))
        self.ram_label.setText(QCoreApplication.translate("signup_page2", u"How much RAM would you want to use", None))
        self.back_button.setText(QCoreApplication.translate("signup_page2", u"Back", None))
        self.cpu_lineedit.setText(QCoreApplication.translate("signup_page2", u"57%", None))
        self.cpu_min_label.setText(QCoreApplication.translate("signup_page2", u"0", None))
        self.cpu_max_label.setText(QCoreApplication.translate("signup_page2", u"100", None))
        self.info_label.setText(QCoreApplication.translate("signup_page2", u"The information you provide helps us provide you with better service", None))
        self.cores_max_label.setText(QCoreApplication.translate("signup_page2", u"8", None))
        self.cores_min_label.setText(QCoreApplication.translate("signup_page2", u"0", None))
        self.cores_lineedit.setText(QCoreApplication.translate("signup_page2", u"2", None))
        self.ram_min_label.setText(QCoreApplication.translate("signup_page2", u"0MB", None))
        self.ram_lineedit.setText(QCoreApplication.translate("signup_page2", u"1600MB", None))
        self.ram_max_label.setText(QCoreApplication.translate("signup_page2", u"1600MB", None))
    # retranslateUi

