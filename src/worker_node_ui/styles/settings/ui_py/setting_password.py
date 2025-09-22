
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class UiPasswordSetting(object):
    def setupUi(self, password_set):
        if not password_set.objectName():
            password_set.setObjectName(u"password_set")
        password_set.resize(1031, 569)
        password_set.setStyleSheet(u"background-color: #00031f\n"
"")
        self.passet_con = QLabel(password_set)
        self.passet_con.setObjectName(u"passet_con")
        self.passet_con.setGeometry(QRect(30, 20, 961, 521))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        self.passet_con.setFont(font)
        self.passet_con.setStyleSheet(u"QLabel {\n"
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
"}\n"
"")
        self.cancel_bt = QPushButton(password_set)
        self.cancel_bt.setObjectName(u"cancel_bt")
        self.cancel_bt.setGeometry(QRect(810, 500, 161, 28))
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
        self.old_pass = QLabel(password_set)
        self.old_pass.setObjectName(u"old_pass")
        self.old_pass.setGeometry(QRect(80, 70, 111, 31))
        self.old_pass.setFont(font)
        self.old_pass.setStyleSheet(u"\n"
"	background-color: rgba(20, 20, 50, 10);\n"
"    color: white;\n"
"	border: transparent;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 13px;\n"
"\n"
"\n"
"")
        self.opass_label = QLineEdit(password_set)
        self.opass_label.setObjectName(u"opass_label")
        self.opass_label.setGeometry(QRect(80, 100, 286, 34))
        self.opass_label.setStyleSheet(u"QLineEdit {\n"
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
        self.new_pass = QLabel(password_set)
        self.new_pass.setObjectName(u"new_pass")
        self.new_pass.setGeometry(QRect(80, 140, 111, 31))
        self.new_pass.setFont(font)
        self.new_pass.setStyleSheet(u"\n"
"	background-color: rgba(20, 20, 50, 10);\n"
"    color: white;\n"
"	border: transparent;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 13px;\n"
"\n"
"\n"
"")
        self.npass_label = QLineEdit(password_set)
        self.npass_label.setObjectName(u"npass_label")
        self.npass_label.setGeometry(QRect(80, 170, 286, 34))
        self.npass_label.setStyleSheet(u"QLineEdit {\n"
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
        self.conf_pass = QLabel(password_set)
        self.conf_pass.setObjectName(u"conf_pass")
        self.conf_pass.setGeometry(QRect(80, 210, 151, 31))
        self.conf_pass.setFont(font)
        self.conf_pass.setStyleSheet(u"\n"
"	background-color: rgba(20, 20, 50, 10);\n"
"    color: white;\n"
"	border: transparent;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 13px;\n"
"\n"
"\n"
"")
        self.cnew_pass = QLineEdit(password_set)
        self.cnew_pass.setObjectName(u"cnew_pass")
        self.cnew_pass.setGeometry(QRect(80, 240, 286, 34))
        self.cnew_pass.setStyleSheet(u"QLineEdit {\n"
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
        self.schanges_bt = QPushButton(password_set)
        self.schanges_bt.setObjectName(u"schanges_bt")
        self.schanges_bt.setGeometry(QRect(810, 470, 161, 28))
        self.schanges_bt.setStyleSheet(u"QPushButton {\n"
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

        self.retranslateUi(password_set)

        QMetaObject.connectSlotsByName(password_set)
    # setupUi

    def retranslateUi(self, password_set):
        password_set.setWindowTitle(QCoreApplication.translate("password_set", u"Form", None))
        self.passet_con.setText("")
        self.cancel_bt.setText(QCoreApplication.translate("password_set", u"Cancel", None))
        self.old_pass.setText(QCoreApplication.translate("password_set", u"Old Password", None))
        self.opass_label.setText("")
        self.new_pass.setText(QCoreApplication.translate("password_set", u"New Password", None))
        self.npass_label.setText("")
        self.conf_pass.setText(QCoreApplication.translate("password_set", u"Confirm New Password", None))
        self.cnew_pass.setText("")
        self.schanges_bt.setText(QCoreApplication.translate("password_set", u"Save Changes", None))
    # retranslateUi

