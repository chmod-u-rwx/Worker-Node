# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_settings.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Editdash(object):
    def setupUi(self, edit_dash):
        if not edit_dash.objectName():
            edit_dash.setObjectName(u"edit_dash")
        edit_dash.resize(1031, 569)
        edit_dash.setStyleSheet(u"background-color: #00031f\n"
"")
        self.settings_2 = QLabel(edit_dash)
        self.settings_2.setObjectName(u"settings_2")
        self.settings_2.setGeometry(QRect(50, 30, 151, 41))
        font = QFont()
        font.setFamilies([u"Century Gothic"])
        font.setPointSize(26)
        font.setBold(True)
        self.settings_2.setFont(font)
        self.settings_2.setStyleSheet(u"background: transparent;\n"
"color: white;\n"
"\n"
"")
        self.rallocation_bt = QPushButton(edit_dash)
        self.rallocation_bt.setObjectName(u"rallocation_bt")
        self.rallocation_bt.setGeometry(QRect(40, 90, 221, 31))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(14)
        self.rallocation_bt.setFont(font1)
        self.rallocation_bt.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid transparent;\n"
"    border-radius: 12px;\n"
"    background: transparent;\n"
"    color: white;\n"
"    padding: 6px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 1px solid #ffffff; \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 1px solid #ffffff;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"../../../../../Downloads/resource_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.rallocation_bt.setIcon(icon)
        self.eprofile_bt = QPushButton(edit_dash)
        self.eprofile_bt.setObjectName(u"eprofile_bt")
        self.eprofile_bt.setGeometry(QRect(40, 130, 151, 31))
        self.eprofile_bt.setFont(font1)
        self.eprofile_bt.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid transparent;\n"
"    border-radius: 12px;\n"
"    background: transparent;\n"
"    color: white;\n"
"    padding: 6px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 1px solid #ffffff;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 1px solid #ffffff; \n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"../../../../../Downloads/eprofile.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.eprofile_bt.setIcon(icon1)
        self.set_con = QLabel(edit_dash)
        self.set_con.setObjectName(u"set_con")
        self.set_con.setGeometry(QRect(280, 30, 721, 511))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        self.set_con.setFont(font2)
        self.set_con.setStyleSheet(u"QLabel {\n"
"	background-color: rgba(20, 20, 50, 10);\n"
"    border: 1px solid rgba(255, 255, 255, 0.3);\n"
"    border-radius: 20px;\n"
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
        self.cancel_bt = QPushButton(edit_dash)
        self.cancel_bt.setObjectName(u"cancel_bt")
        self.cancel_bt.setGeometry(QRect(820, 500, 161, 28))
        self.cancel_bt.setStyleSheet(u"QPushButton {\n"
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
        self.logout_bt = QPushButton(edit_dash)
        self.logout_bt.setObjectName(u"logout_bt")
        self.logout_bt.setGeometry(QRect(50, 520, 81, 20))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(9)
        self.logout_bt.setFont(font3)
        self.logout_bt.setStyleSheet(u"QPushButton {\n"
"    background: transparent;\n"
"    border: none;\n"
"    color: #FF3B30;  /* purple link color */\n"
"}\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"src/worker_node_ui/resources/fbuttons/logout.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.logout_bt.setIcon(icon2)
        self.jdate_gbox = QGroupBox(edit_dash)
        self.jdate_gbox.setObjectName(u"jdate_gbox")
        self.jdate_gbox.setGeometry(QRect(330, 80, 281, 61))
        self.jdate_gbox.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"border: 1px solid #a2a1a1;\n"
"border-radius: 12px;\n"
"")
        self.jdate_label = QLabel(self.jdate_gbox)
        self.jdate_label.setObjectName(u"jdate_label")
        self.jdate_label.setGeometry(QRect(0, 10, 261, 51))
        self.jdate_label.setStyleSheet(u"\n"
"	background-color: rgba(20, 20, 50, 10);\n"
"    padding: 8px;\n"
"    color: white;\n"
"	border: transparent;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 13px;\n"
"\n"
"\n"
"")
        self.uname_gbox = QGroupBox(edit_dash)
        self.uname_gbox.setObjectName(u"uname_gbox")
        self.uname_gbox.setGeometry(QRect(640, 80, 301, 61))
        self.uname_gbox.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"border: 1px solid #a2a1a1;\n"
"border-radius: 12px;\n"
"")
        self.uname_label = QLabel(self.uname_gbox)
        self.uname_label.setObjectName(u"uname_label")
        self.uname_label.setGeometry(QRect(0, 10, 259, 51))
        self.uname_label.setStyleSheet(u"\n"
"	background-color: rgba(20, 20, 50, 10);\n"
"    padding: 8px;\n"
"    color: white;\n"
"	border: transparent;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 13px;\n"
"\n"
"\n"
"")
        self.wid_gbox = QGroupBox(edit_dash)
        self.wid_gbox.setObjectName(u"wid_gbox")
        self.wid_gbox.setGeometry(QRect(330, 160, 401, 61))
        self.wid_gbox.setStyleSheet(u"color: white;\n"
"background: transparent;\n"
"border: 1px solid #a2a1a1;\n"
"border-radius: 12px;\n"
"")
        self.wid_label = QLabel(self.wid_gbox)
        self.wid_label.setObjectName(u"wid_label")
        self.wid_label.setGeometry(QRect(0, 10, 261, 51))
        self.wid_label.setStyleSheet(u"\n"
"	background-color: rgba(20, 20, 50, 10);\n"
"    padding: 8px;\n"
"    color: white;\n"
"	border: transparent;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 13px;\n"
"\n"
"\n"
"")
        self.chpass_bt = QPushButton(edit_dash)
        self.chpass_bt.setObjectName(u"chpass_bt")
        self.chpass_bt.setGeometry(QRect(750, 160, 131, 21))
        self.chpass_bt.setStyleSheet(u"QPushButton {\n"
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
        self.set_con.raise_()
        self.settings_2.raise_()
        self.rallocation_bt.raise_()
        self.eprofile_bt.raise_()
        self.cancel_bt.raise_()
        self.logout_bt.raise_()
        self.jdate_gbox.raise_()
        self.uname_gbox.raise_()
        self.wid_gbox.raise_()
        self.chpass_bt.raise_()

        self.retranslateUi(edit_dash)

        QMetaObject.connectSlotsByName(edit_dash)
    # setupUi

    def retranslateUi(self, edit_dash):
        edit_dash.setWindowTitle(QCoreApplication.translate("edit_dash", u"Form", None))
        self.settings_2.setText(QCoreApplication.translate("edit_dash", u"Settings", None))
        self.rallocation_bt.setText(QCoreApplication.translate("edit_dash", u"Resource Allocation", None))
        self.eprofile_bt.setText(QCoreApplication.translate("edit_dash", u"Edit Profile", None))
        self.set_con.setText("")
        self.cancel_bt.setText(QCoreApplication.translate("edit_dash", u"Cancel", None))
        self.logout_bt.setText(QCoreApplication.translate("edit_dash", u"Log out", None))
        self.jdate_gbox.setTitle(QCoreApplication.translate("edit_dash", u"Join Date", None))
        self.jdate_label.setText(QCoreApplication.translate("edit_dash", u"09/01/2025", None))
        self.uname_gbox.setTitle(QCoreApplication.translate("edit_dash", u"Username", None))
        self.uname_label.setText(QCoreApplication.translate("edit_dash", u"YEYPASKONA", None))
        self.wid_gbox.setTitle(QCoreApplication.translate("edit_dash", u"Worker Identification", None))
        self.wid_label.setText(QCoreApplication.translate("edit_dash", u"15fb957b-03a9-4f10-9404-0882cc5264f5", None))
        self.chpass_bt.setText(QCoreApplication.translate("edit_dash", u"Change Password", None))
    # retranslateUi

