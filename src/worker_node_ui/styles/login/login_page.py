from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class UiLoginPage(object):
    def setupUi(self, login_page):
        if not login_page.objectName():
            login_page.setObjectName(u"login_page")
        login_page.resize(1440, 810)
        login_page.setMinimumSize(QSize(1440, 810))
        login_page.setMaximumSize(QSize(1440, 810))
        self.bg_label = QLabel(login_page)
        self.bg_label.setPixmap(QPixmap("src/worker_node_ui/resources/images/login_bg.png"))
        self.bg_label.setScaledContents(True)  # scales image with window
        self.bg_label.setGeometry(0, 0, login_page.width(), login_page.height())
        self.bg_label.lower()  # send to back
        self.horizontalLayoutWidget = QWidget(login_page)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 2, 2))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.logo = QLabel(login_page)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(650, 130, 81, 61))
        self.logo.setAutoFillBackground(False)
        self.logo.setStyleSheet(u"background: transparent;")
        self.logo.setPixmap(QPixmap("src/worker_node_ui/resources/images/signup1logo.png"))
        self.logo.setScaledContents(True)
        self.welcome_label = QLabel(login_page)
        self.welcome_label.setObjectName(u"welcome_label")
        self.welcome_label.setGeometry(QRect(490, 230, 421, 31))
        font = QFont()
        font.setFamilies([u"Century Gothic"])
        font.setPointSize(26)
        font.setBold(True)
        self.welcome_label.setFont(font)
        self.welcome_label.setStyleSheet(u"background: transparent;\n"
"color: white;\n"
"\n"
"")
        self.login_button_2 = QPushButton(login_page)
        self.login_button_2.setObjectName(u"login_button_2")
        self.login_button_2.setGeometry(QRect(580, 580, 241, 41))
        font1 = QFont()
        font1.setFamilies([u"Century Gothic"])
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(False)
        self.login_button_2.setFont(font1)
        self.login_button_2.setStyleSheet(u"QPushButton {\n"
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
        self.username_label = QLabel(login_page)
        self.username_label.setObjectName(u"username_label")
        self.username_label.setGeometry(QRect(460, 310, 91, 31))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(14)
        font2.setBold(False)
        self.username_label.setFont(font2)
        self.username_label.setStyleSheet(u"color: white;\n"
"background-color: transparent;\n"
"")
        self.signup_button = QPushButton(login_page)
        self.signup_button.setObjectName(u"signup_button")
        self.signup_button.setGeometry(QRect(610, 730, 181, 20))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(9)
        self.signup_button.setFont(font3)
        self.signup_button.setStyleSheet(u"QPushButton {\n"
"    background: transparent;\n"
"    border: none;\n"
"    color: #FFFFFF;  /* purple link color */\n"
"}\n"
"QPushButton:hover {\n"
"    color: #5B3ECC;\n"
"}\n"
"")
        self.username_field = QLineEdit(login_page)
        self.username_field.setObjectName(u"username_field")
        self.username_field.setGeometry(QRect(460, 350, 481, 51))
        self.username_field.setStyleSheet(u"QLineEdit {\n"
"	background-color: transparent;\n"
"    border: 1px solid rgba(255, 255, 255, 0.3);\n"
"    border-radius: 10px;\n"
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
        self.login_container = QLabel(login_page)
        self.login_container.setObjectName(u"login_container")
        self.login_container.setGeometry(QRect(410, 100, 582, 614))
        self.login_container.setStyleSheet(u"QLabel {\n"
"	background-color: rgba(20, 20, 50, 10);\n"
"    border: 1px solid rgba(255, 255, 255, 0.3);\n"
"    border-radius: 50px;\n"
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
        self.password_label = QLabel(login_page)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setGeometry(QRect(460, 440, 91, 31))
        self.password_label.setFont(font2)
        self.password_label.setStyleSheet(u"color: white;\n"
"background-color: transparent;\n"
"")
        self.password_field = QLineEdit(login_page)
        self.password_field.setObjectName(u"password_field")
        self.password_field.setGeometry(QRect(460, 480, 481, 51))
        self.password_field.setStyleSheet(u"QLineEdit {\n"
"	background-color: transparent;\n"
"    border: 1px solid rgba(255, 255, 255, 0.3);\n"
"    border-radius: 10px;\n"
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
        self.login_container.raise_()
        self.horizontalLayoutWidget.raise_()
        self.logo.raise_()
        self.welcome_label.raise_()
        self.login_button_2.raise_()
        self.username_label.raise_()
        self.signup_button.raise_()
        self.username_field.raise_()
        self.password_label.raise_()
        self.password_field.raise_()

        self.retranslateUi(login_page)

        QMetaObject.connectSlotsByName(login_page)
    # setupUi

    def retranslateUi(self, login_page):
        login_page.setWindowTitle(QCoreApplication.translate("login_page", u"CrowdCloud", None))
        self.logo.setText("")
        self.welcome_label.setText(QCoreApplication.translate("login_page", u"Welcome to CrowdCloud", None))
        self.login_button_2.setText(QCoreApplication.translate("login_page", u"Log In", None))
        self.username_label.setText(QCoreApplication.translate("login_page", u"Username", None))
        self.signup_button.setText(QCoreApplication.translate("login_page", u"Dont have an account? Sign up", None))
        self.username_field.setText("")
        self.login_container.setText("")
        self.password_label.setText(QCoreApplication.translate("login_page", u"Password", None))
        self.password_field.setText("")
    # retranslateUi

