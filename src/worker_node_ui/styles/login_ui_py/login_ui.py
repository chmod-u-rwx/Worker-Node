# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize)
from PySide6.QtGui import (QFont, QPixmap)
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QLineEdit, QMainWindow, QPushButton, QWidget)

class Ui_login(object):
    def setupUi(self, login_page: QMainWindow):
        if not login_page.objectName():
            login_page.setObjectName(u"login_page")
        login_page.resize(1440, 810)
        login_page.setMinimumSize(QSize(1440, 810))
        login_page.setMaximumSize(QSize(1440, 810))
        self.centralwidget = QWidget(login_page)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMinimumSize(QSize(1440, 810))
        self.centralwidget.setMaximumSize(QSize(1440, 810))
        self.centralwidget.setStyleSheet("background-image: url('src/worker_node_ui/resources/images/login_bg.png');")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 2, 2))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(650, 130, 81, 63))
        self.logo.setAutoFillBackground(False)
        self.logo.setScaledContents(True)
        self.logo.setStyleSheet(u"background: transparent;")
        self.logo.setPixmap(QPixmap("src/worker_node_ui/resources/images/signup1logo.png"))
        self.welcome_label = QLabel(self.centralwidget)
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
        self.login_button_2 = QPushButton(self.centralwidget)
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
        self.username_label = QLabel(self.centralwidget)
        self.username_label.setObjectName(u"username_label")
        self.username_label.setGeometry(QRect(460, 310, 91, 31))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(14)
        font2.setBold(False)
        self.username_label.setFont(font2)
        self.username_label.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"")
        self.signup_button = QPushButton(self.centralwidget)
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
"    cursor: pointer;\n"
"}\n"
"")
        self.username_field = QLineEdit(self.centralwidget)
        self.username_field.setObjectName(u"username_field")
        self.username_field.setGeometry(QRect(460, 350, 481, 51))
        self.username_field.setStyleSheet(u"QLineEdit {\n"
"	background: transparent;\n"
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
        self.login_container = QLabel(self.centralwidget)
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
        self.password_label = QLabel(self.centralwidget)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setGeometry(QRect(460, 440, 91, 31))
        self.password_label.setFont(font2)
        self.password_label.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"")
        self.password_field = QLineEdit(self.centralwidget)
        self.password_field.setObjectName(u"password_field")
        self.password_field.setGeometry(QRect(460, 480, 481, 51))
        self.password_field.setStyleSheet(u"QLineEdit {\n"
"	background: transparent;\n"
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
        login_page.setCentralWidget(self.centralwidget)
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

