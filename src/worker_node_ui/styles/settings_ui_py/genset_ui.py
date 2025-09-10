# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gen_setting.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSlider, QWidget)

class Ui_Gensettings(object):
    def setupUi(self, gen_settings):
        if not gen_settings.objectName():
            gen_settings.setObjectName(u"gen_settings")
        gen_settings.resize(1031, 569)
        gen_settings.setStyleSheet(u"background-color: #00031f\n"
"")
        self.settings_2 = QLabel(gen_settings)
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
        self.cache_path = QLabel(gen_settings)
        self.cache_path.setObjectName(u"cache_path")
        self.cache_path.setGeometry(QRect(300, 40, 121, 31))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(11)
        font1.setBold(False)
        self.cache_path.setFont(font1)
        self.cache_path.setStyleSheet(u"color: white;\n"
"background-color: transparent;\n"
"")
        self.rallocation_bt = QPushButton(gen_settings)
        self.rallocation_bt.setObjectName(u"rallocation_bt")
        self.rallocation_bt.setGeometry(QRect(40, 90, 221, 31))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(14)
        self.rallocation_bt.setFont(font2)
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
        self.eprofile_bt = QPushButton(gen_settings)
        self.eprofile_bt.setObjectName(u"eprofile_bt")
        self.eprofile_bt.setGeometry(QRect(40, 130, 151, 31))
        self.eprofile_bt.setFont(font2)
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
        self.set_con = QLabel(gen_settings)
        self.set_con.setObjectName(u"set_con")
        self.set_con.setGeometry(QRect(280, 30, 721, 511))
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
        self.cpu_lineedit = QLineEdit(gen_settings)
        self.cpu_lineedit.setObjectName(u"cpu_lineedit")
        self.cpu_lineedit.setGeometry(QRect(310, 170, 71, 41))
        font3 = QFont()
        font3.setFamilies([u"Century Gothic"])
        self.cpu_lineedit.setFont(font3)
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
        self.conf_cpu = QLabel(gen_settings)
        self.conf_cpu.setObjectName(u"conf_cpu")
        self.conf_cpu.setGeometry(QRect(300, 140, 341, 16))
        font4 = QFont()
        font4.setFamilies([u"Century Gothic"])
        font4.setPointSize(10)
        font4.setBold(False)
        self.conf_cpu.setFont(font4)
        self.conf_cpu.setStyleSheet(u"color: white;\n"
"background-color: transparent;\n"
"")
        self.cpu_min_label = QLabel(gen_settings)
        self.cpu_min_label.setObjectName(u"cpu_min_label")
        self.cpu_min_label.setGeometry(QRect(400, 170, 16, 21))
        self.cpu_min_label.setStyleSheet(u"QLabel {\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    font-family: \"Century Gothic\";\n"
"    color: #ffffff;\n"
"    background-color: transparent;\n"
"}\n"
"")
        self.cpu_slider = QSlider(gen_settings)
        self.cpu_slider.setObjectName(u"cpu_slider")
        self.cpu_slider.setGeometry(QRect(400, 190, 381, 21))
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
        self.cpu_slider.setOrientation(Qt.Horizontal)
        self.cpu_max_label = QLabel(gen_settings)
        self.cpu_max_label.setObjectName(u"cpu_max_label")
        self.cpu_max_label.setGeometry(QRect(750, 170, 31, 21))
        self.cpu_max_label.setStyleSheet(u"QLabel {\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    font-family: \"Century Gothic\";\n"
"    color: #ffffff;\n"
"    background-color: transparent;\n"
"}\n"
"")
        self.cache_lineedit = QLineEdit(gen_settings)
        self.cache_lineedit.setObjectName(u"cache_lineedit")
        self.cache_lineedit.setGeometry(QRect(320, 80, 481, 41))
        self.cache_lineedit.setStyleSheet(u"QLineEdit {\n"
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
"    box-shadow: 0px 0px 8px #7D5FFF;\n"
"}\n"
"")
        self.schanges_bt = QPushButton(gen_settings)
        self.schanges_bt.setObjectName(u"schanges_bt")
        self.schanges_bt.setGeometry(QRect(830, 470, 151, 28))
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
        self.conf_cores = QLabel(gen_settings)
        self.conf_cores.setObjectName(u"conf_cores")
        self.conf_cores.setGeometry(QRect(300, 230, 341, 16))
        self.conf_cores.setFont(font4)
        self.conf_cores.setStyleSheet(u"color: white;\n"
"background-color: transparent;\n"
"")
        self.core_min_label = QLabel(gen_settings)
        self.core_min_label.setObjectName(u"core_min_label")
        self.core_min_label.setGeometry(QRect(400, 260, 16, 21))
        self.core_min_label.setStyleSheet(u"QLabel {\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    font-family: \"Century Gothic\";\n"
"    color: #ffffff;\n"
"    background-color: transparent;\n"
"}\n"
"")
        self.core_max_label_ = QLabel(gen_settings)
        self.core_max_label_.setObjectName(u"core_max_label_")
        self.core_max_label_.setGeometry(QRect(750, 260, 31, 21))
        self.core_max_label_.setStyleSheet(u"QLabel {\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    font-family: \"Century Gothic\";\n"
"    color: #ffffff;\n"
"    background-color: transparent;\n"
"}\n"
"")
        self.core_lineedit = QLineEdit(gen_settings)
        self.core_lineedit.setObjectName(u"core_lineedit")
        self.core_lineedit.setGeometry(QRect(310, 260, 71, 41))
        self.core_lineedit.setFont(font3)
        self.core_lineedit.setStyleSheet(u"QLineEdit {\n"
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
        self.cores_slider = QSlider(gen_settings)
        self.cores_slider.setObjectName(u"cores_slider")
        self.cores_slider.setGeometry(QRect(400, 280, 381, 21))
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
        self.cores_slider.setOrientation(Qt.Horizontal)
        self.ram_slider = QSlider(gen_settings)
        self.ram_slider.setObjectName(u"ram_slider")
        self.ram_slider.setGeometry(QRect(400, 370, 381, 21))
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
        self.ram_slider.setOrientation(Qt.Horizontal)
        self.ram_min_label = QLabel(gen_settings)
        self.ram_min_label.setObjectName(u"ram_min_label")
        self.ram_min_label.setGeometry(QRect(400, 350, 16, 21))
        self.ram_min_label.setStyleSheet(u"QLabel {\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    font-family: \"Century Gothic\";\n"
"    color: #ffffff;\n"
"    background-color: transparent;\n"
"}\n"
"")
        self.ram_max_label = QLabel(gen_settings)
        self.ram_max_label.setObjectName(u"ram_max_label")
        self.ram_max_label.setGeometry(QRect(750, 350, 31, 21))
        self.ram_max_label.setStyleSheet(u"QLabel {\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    font-family: \"Century Gothic\";\n"
"    color: #ffffff;\n"
"    background-color: transparent;\n"
"}\n"
"")
        self.conf_ram = QLabel(gen_settings)
        self.conf_ram.setObjectName(u"conf_ram")
        self.conf_ram.setGeometry(QRect(300, 320, 341, 16))
        self.conf_ram.setFont(font4)
        self.conf_ram.setStyleSheet(u"color: white;\n"
"background-color: transparent;\n"
"")
        self.ram_lineedit = QLineEdit(gen_settings)
        self.ram_lineedit.setObjectName(u"ram_lineedit")
        self.ram_lineedit.setGeometry(QRect(310, 350, 71, 41))
        self.ram_lineedit.setFont(font3)
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
        self.cache_slider = QSlider(gen_settings)
        self.cache_slider.setObjectName(u"cache_slider")
        self.cache_slider.setGeometry(QRect(400, 460, 381, 21))
        self.cache_slider.setStyleSheet(u"QSlider {\n"
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
        self.cache_slider.setMaximum(100)
        self.cache_slider.setValue(50)
        self.cache_slider.setOrientation(Qt.Horizontal)
        self.cache_min_label = QLabel(gen_settings)
        self.cache_min_label.setObjectName(u"cache_min_label")
        self.cache_min_label.setGeometry(QRect(400, 440, 16, 21))
        self.cache_min_label.setStyleSheet(u"QLabel {\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    font-family: \"Century Gothic\";\n"
"    color: #ffffff;\n"
"    background-color: transparent;\n"
"}\n"
"")
        self.cache_max_label = QLabel(gen_settings)
        self.cache_max_label.setObjectName(u"cache_max_label")
        self.cache_max_label.setGeometry(QRect(750, 440, 31, 21))
        self.cache_max_label.setStyleSheet(u"QLabel {\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    font-family: \"Century Gothic\";\n"
"    color: #ffffff;\n"
"    background-color: transparent;\n"
"}\n"
"")
        self.conf_cache = QLabel(gen_settings)
        self.conf_cache.setObjectName(u"conf_cache")
        self.conf_cache.setGeometry(QRect(300, 410, 341, 16))
        self.conf_cache.setFont(font4)
        self.conf_cache.setStyleSheet(u"color: white;\n"
"background-color: transparent;\n"
"")
        self.cache_lineedit_2 = QLineEdit(gen_settings)
        self.cache_lineedit_2.setObjectName(u"cache_lineedit_2")
        self.cache_lineedit_2.setGeometry(QRect(310, 440, 71, 41))
        self.cache_lineedit_2.setFont(font3)
        self.cache_lineedit_2.setStyleSheet(u"QLineEdit {\n"
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
        self.cancel_bt = QPushButton(gen_settings)
        self.cancel_bt.setObjectName(u"cancel_bt")
        self.cancel_bt.setGeometry(QRect(830, 500, 151, 28))
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
        self.logout_bt = QPushButton(gen_settings)
        self.logout_bt.setObjectName(u"logout_bt")
        self.logout_bt.setGeometry(QRect(50, 520, 81, 20))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(9)
        self.logout_bt.setFont(font5)
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
        self.clearc_bt = QPushButton(gen_settings)
        self.clearc_bt.setObjectName(u"clearc_bt")
        self.clearc_bt.setGeometry(QRect(520, 410, 111, 21))
        self.clearc_bt.setStyleSheet(u"QPushButton {\n"
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
        self.clearc_bt_2 = QPushButton(gen_settings)
        self.clearc_bt_2.setObjectName(u"clearc_bt_2")
        self.clearc_bt_2.setGeometry(QRect(380, 45, 81, 20))
        self.clearc_bt_2.setStyleSheet(u"QPushButton {\n"
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
        self.cache_path.raise_()
        self.rallocation_bt.raise_()
        self.eprofile_bt.raise_()
        self.cpu_lineedit.raise_()
        self.conf_cpu.raise_()
        self.cpu_min_label.raise_()
        self.cpu_slider.raise_()
        self.cpu_max_label.raise_()
        self.cache_lineedit.raise_()
        self.schanges_bt.raise_()
        self.conf_cores.raise_()
        self.core_min_label.raise_()
        self.core_max_label_.raise_()
        self.core_lineedit.raise_()
        self.cores_slider.raise_()
        self.ram_slider.raise_()
        self.ram_min_label.raise_()
        self.ram_max_label.raise_()
        self.conf_ram.raise_()
        self.ram_lineedit.raise_()
        self.cache_slider.raise_()
        self.cache_min_label.raise_()
        self.cache_max_label.raise_()
        self.conf_cache.raise_()
        self.cache_lineedit_2.raise_()
        self.cancel_bt.raise_()
        self.logout_bt.raise_()
        self.clearc_bt.raise_()
        self.clearc_bt_2.raise_()

        self.retranslateUi(gen_settings)

        QMetaObject.connectSlotsByName(gen_settings)
    # setupUi

    def retranslateUi(self, gen_settings):
        gen_settings.setWindowTitle(QCoreApplication.translate("gen_settings", u"Form", None))
        self.settings_2.setText(QCoreApplication.translate("gen_settings", u"Settings", None))
        self.cache_path.setText(QCoreApplication.translate("gen_settings", u"Cache Path", None))
        self.rallocation_bt.setText(QCoreApplication.translate("gen_settings", u"Resource Allocation", None))
        self.eprofile_bt.setText(QCoreApplication.translate("gen_settings", u"Edit Profile", None))
        self.set_con.setText("")
        self.cpu_lineedit.setText(QCoreApplication.translate("gen_settings", u"57%", None))
        self.conf_cpu.setText(QCoreApplication.translate("gen_settings", u"Configure CPU utilization limit", None))
        self.cpu_min_label.setText(QCoreApplication.translate("gen_settings", u"0", None))
        self.cpu_max_label.setText(QCoreApplication.translate("gen_settings", u"100", None))
        self.cache_lineedit.setInputMask("")
        self.cache_lineedit.setText("")
        self.cache_lineedit.setPlaceholderText(QCoreApplication.translate("gen_settings", u"/tmp/crowdcloud", None))
        self.schanges_bt.setText(QCoreApplication.translate("gen_settings", u"Save changes", None))
        self.conf_cores.setText(QCoreApplication.translate("gen_settings", u"Configure cores utilization limit", None))
        self.core_min_label.setText(QCoreApplication.translate("gen_settings", u"0", None))
        self.core_max_label_.setText(QCoreApplication.translate("gen_settings", u"100", None))
        self.core_lineedit.setText(QCoreApplication.translate("gen_settings", u"3", None))
        self.ram_min_label.setText(QCoreApplication.translate("gen_settings", u"0", None))
        self.ram_max_label.setText(QCoreApplication.translate("gen_settings", u"100", None))
        self.conf_ram.setText(QCoreApplication.translate("gen_settings", u"Configure RAM utilization limit", None))
        self.ram_lineedit.setText(QCoreApplication.translate("gen_settings", u"57%", None))
        self.cache_min_label.setText(QCoreApplication.translate("gen_settings", u"0", None))
        self.cache_max_label.setText(QCoreApplication.translate("gen_settings", u"100", None))
        self.conf_cache.setText(QCoreApplication.translate("gen_settings", u"Configure cache utilization limit", None))
        self.cache_lineedit_2.setText(QCoreApplication.translate("gen_settings", u"57%", None))
        self.cancel_bt.setText(QCoreApplication.translate("gen_settings", u"Cancel", None))
        self.logout_bt.setText(QCoreApplication.translate("gen_settings", u"Log out", None))
        self.clearc_bt.setText(QCoreApplication.translate("gen_settings", u"Clear cache", None))
        self.clearc_bt_2.setText(QCoreApplication.translate("gen_settings", u"Browse", None))
    # retranslateUi

