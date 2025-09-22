from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class UiSignupCreate(object):
    def setupUi(self, signup_page1):
        if not signup_page1.objectName():
            signup_page1.setObjectName(u"signup_page1")
        signup_page1.resize(1440, 810)
        signup_page1.setMinimumSize(QSize(1440, 810))
        signup_page1.setMaximumSize(QSize(1440, 810))
        self.bg_label = QLabel(signup_page1)
        self.bg_label.setPixmap(QPixmap("src/worker_node_ui/resources/images/gen_dashboard.png"))
        self.bg_label.setScaledContents(True)  # scales image with window
        self.bg_label.setGeometry(0, 0, signup_page1.width(), signup_page1.height())
        self.bg_label.lower()  # send to back
        self.horizontalLayoutWidget = QWidget(signup_page1)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 2, 2))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.logo = QLabel(signup_page1)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(280, 320, 109, 88))
        self.logo.setAutoFillBackground(False)
        self.logo.setStyleSheet(u"background: transparent;")
        self.logo.setPixmap(QPixmap("src/worker_node_ui/resources/images/signup1logo.png"))
        self.get_started = QLabel(signup_page1)
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
        self.create_label = QLabel(signup_page1)
        self.create_label.setObjectName(u"create_label")
        self.create_label.setGeometry(QRect(900, 180, 281, 31))
        font1 = QFont()
        font1.setFamilies([u"Century Gothic"])
        font1.setPointSize(26)
        font1.setBold(True)
        self.create_label.setFont(font1)
        self.create_label.setStyleSheet(u"background: transparent;\n"
"color: white;\n"
"\n"
"")
        self.enter_personal_label = QLabel(signup_page1)
        self.enter_personal_label.setObjectName(u"enter_personal_label")
        self.enter_personal_label.setGeometry(QRect(880, 220, 301, 21))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(12)
        font2.setBold(False)
        self.enter_personal_label.setFont(font2)
        self.enter_personal_label.setStyleSheet(u"background: transparent;\n"
"color: white;\n"
"\n"
"")
        self.email_field = QLineEdit(signup_page1)
        self.email_field.setObjectName(u"email_field")
        self.email_field.setGeometry(QRect(810, 300, 451, 41))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        self.email_field.setFont(font3)
        self.email_field.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgba(20, 20, 50, 10);\n"
"    border: 1px solid rgba(255, 255, 255, 0.3);\n"
"    border-radius: 10px;\n"
"    padding: 8px;\n"
"    color: white;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #7D5FFF; \n"
"}\n"
"")
        self.username_field = QLineEdit(signup_page1)
        self.username_field.setObjectName(u"username_field")
        self.username_field.setGeometry(QRect(810, 370, 451, 41))
        self.username_field.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgba(20, 20, 50, 10);\n"
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
        self.password_field = QLineEdit(signup_page1)
        self.password_field.setObjectName(u"password_field")
        self.password_field.setGeometry(QRect(810, 440, 451, 41))
        self.password_field.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgba(20, 20, 50, 10);\n"
"    border: 1px solid rgba(255, 255, 255, 0.3);\n"
"    border-radius: 10px;\n"
"    padding: 8px;\n"
"    color: white; \n"
"    font-family: \"Segoe UI\"; \n"
"    font-size: 13px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #7D5FFF;\n"
"}\n"
"")
        self.confpass_field = QLineEdit(signup_page1)
        self.confpass_field.setObjectName(u"confpass_field")
        self.confpass_field.setGeometry(QRect(810, 510, 451, 41))
        self.confpass_field.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgba(20, 20, 50, 10);\n"
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
        self.next_button = QPushButton(signup_page1)
        self.next_button.setObjectName(u"next_button")
        self.next_button.setGeometry(QRect(810, 580, 451, 41))
        font4 = QFont()
        font4.setFamilies([u"Century Gothic"])
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setItalic(False)
        self.next_button.setFont(font4)
        self.next_button.setStyleSheet(u"QPushButton {\n"
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
        self.login_button = QPushButton(signup_page1)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setGeometry(QRect(950, 640, 181, 20))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(9)
        self.login_button.setFont(font5)
        self.login_button.setStyleSheet(u"QPushButton {\n"
"    background: transparent;\n"
"    border: none;\n"
"    color: #FFFFFF;  /* purple link color */\n"
"}\n"
"QPushButton:hover {\n"
"    color: #5B3ECC;\n"
"}\n"
"")
        self.email_label = QLabel(signup_page1)
        self.email_label.setObjectName(u"email_label")
        self.email_label.setGeometry(QRect(820, 310, 91, 16))
        self.email_label.setFont(font5)
        self.email_label.setStyleSheet(u"color: white;\n"
"background-color: transparent;")
        self.username = QLabel(signup_page1)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(820, 380, 91, 16))
        self.username.setFont(font5)
        self.username.setStyleSheet(u"color: white;\n"
"background-color: transparent;")
        self.password = QLabel(signup_page1)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(820, 450, 91, 16))
        self.password.setFont(font5)
        self.password.setStyleSheet(u"color: white;\n"
"background-color: transparent;")
        self.confpass = QLabel(signup_page1)
        self.confpass.setObjectName(u"confpass")
        self.confpass.setGeometry(QRect(820, 520, 111, 16))
        self.confpass.setFont(font5)
        self.confpass.setStyleSheet(u"color: white;\n"
"background-color: transparent;")

        self.retranslateUi(signup_page1)

        QMetaObject.connectSlotsByName(signup_page1)
    # setupUi

    def retranslateUi(self, signup_page1):
        signup_page1.setWindowTitle(QCoreApplication.translate("signup_page1", u"CrowdCloud", None))
        self.logo.setText("")
        self.get_started.setText(QCoreApplication.translate("signup_page1", u"Get Started with Us", None))
        self.create_label.setText(QCoreApplication.translate("signup_page1", u"Create Account", None))
        self.enter_personal_label.setText(QCoreApplication.translate("signup_page1", u"Enter your personal information to sign up", None))
        self.email_field.setText("")
        self.username_field.setText("")
        self.password_field.setText("")
        self.confpass_field.setText("")
        self.next_button.setText(QCoreApplication.translate("signup_page1", u"Next", None))
        self.login_button.setText(QCoreApplication.translate("signup_page1", u"Already have an account? Log In", None))
        self.email_label.setText(QCoreApplication.translate("signup_page1", u"Email Address", None))
        self.username.setText(QCoreApplication.translate("signup_page1", u"Username", None))
        self.password.setText(QCoreApplication.translate("signup_page1", u"Password", None))
        self.confpass.setText(QCoreApplication.translate("signup_page1", u"Confirm Password", None))
    # retranslateUi

