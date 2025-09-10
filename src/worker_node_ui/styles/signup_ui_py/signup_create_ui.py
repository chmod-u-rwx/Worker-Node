from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize
from PySide6.QtGui import QFont, QPixmap
from PySide6 import QtGui, QtCore
from PySide6.QtWidgets import QLabel, QLineEdit, QPushButton, QWidget, QMainWindow

class Ui_signup_create(object):
    def setupUi(self, signup_create: QMainWindow):
        if not signup_create.objectName():
            signup_create.setObjectName("signup_create")
        signup_create.resize(1440, 810)
        signup_create.setMinimumSize(QSize(1440, 810))
        signup_create.setMaximumSize(QSize(1440, 810))

        # Central Widget
        self.centralwidget = QWidget(signup_create)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setMinimumSize(QSize(1440, 810))
        self.centralwidget.setMaximumSize(QSize(1440, 810))
        self.centralwidget.setStyleSheet(
            "background-image: url('src/worker_node_ui/resources/images/signin_background.png');"
        )

        # Logo
        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName("logo")
        self.logo.setGeometry(QRect(280, 320, 109, 88))
        self.logo.setStyleSheet("background: transparent;")
        self.logo.setPixmap(QPixmap("src/worker_node_ui/resources/images/signup1logo.png"))

        # Get Started Label
        self.get_started = QLabel(self.centralwidget)
        self.get_started.setObjectName("get_started")
        self.get_started.setGeometry(QRect(170, 410, 333, 88))
        font = QFont()
        font.setFamilies(["Century Gothic"])
        font.setPointSize(28)
        font.setBold(True)
        self.get_started.setFont(font)
        self.get_started.setStyleSheet("background: transparent; color: white;")

        # Create Account Label
        self.create_label = QLabel(self.centralwidget)
        self.create_label.setObjectName("create_label")
        self.create_label.setGeometry(QRect(900, 180, 281, 31))
        font1 = QFont()
        font1.setFamilies(["Century Gothic"])
        font1.setPointSize(26)
        font1.setBold(True)
        self.create_label.setFont(font1)
        self.create_label.setStyleSheet("background: transparent; color: white;")

        # Enter Personal Info Label
        self.enter_personal_label = QLabel(self.centralwidget)
        self.enter_personal_label.setObjectName("enter_personal_label")
        self.enter_personal_label.setGeometry(QRect(880, 220, 301, 21))
        font2 = QFont()
        font2.setFamilies(["Segoe UI"])
        font2.setPointSize(12)
        self.enter_personal_label.setFont(font2)
        self.enter_personal_label.setStyleSheet("background: transparent; color: white;")

        # --- Reusable LineEdit style ---
        lineedit_style = """
            QLineEdit {
                background-color: rgba(20, 20, 50, 0.4);   /* transparent dark bg */
                border: 1px solid rgba(255, 255, 255, 0.6);
                border-radius: 10px;
                padding: 8px;
                color: white;                              /* text always white */
                font-family: "Segoe UI";
                font-size: 13px;
            }
            QLineEdit:focus {
                border: 1px solid #7D5FFF;                 /* purple border on focus */
                background-color: rgba(40, 40, 70, 0.8);   /* slightly brighter */
                color: white;                              /* keep text white */
            }
        """

        # Input Fields
        self.email_field = QLineEdit(self.centralwidget)
        self.email_field.setObjectName("email_field")
        self.email_field.setGeometry(QRect(810, 300, 451, 41))
        self.email_field.setFont(QFont("Segoe UI", 9))
        self.email_field.setStyleSheet("QLineEdit { border: 1px solid white; background: #00031F; color: white; padding: 8px; border-radius: 10px; }")

        self.username_field = QLineEdit(self.centralwidget)
        self.username_field.setObjectName("username_field")
        self.username_field.setGeometry(QRect(810, 370, 451, 41))
        self.username_field.setStyleSheet(lineedit_style)

        self.password_field = QLineEdit(self.centralwidget)
        self.password_field.setObjectName("password_field")
        self.password_field.setGeometry(QRect(810, 440, 451, 41))
        self.password_field.setEchoMode(QLineEdit.EchoMode.Password) 
        self.password_field.setStyleSheet(lineedit_style)

        self.confpass_field = QLineEdit(self.centralwidget)
        self.confpass_field.setObjectName("confpass_field")
        self.confpass_field.setGeometry(QRect(810, 510, 451, 41))
        self.confpass_field.setEchoMode(QLineEdit.EchoMode.Password)
        self.confpass_field.setStyleSheet(lineedit_style)

        # Buttons
        self.next_button = QPushButton(self.centralwidget)
        self.next_button.setObjectName("next_button")
        self.next_button.setGeometry(QRect(810, 580, 451, 41))
        self.next_button.setFont(QFont("Century Gothic", 12, QFont.Bold)) #type:ignore
        self.next_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor)) #type:ignore
        self.next_button.setStyleSheet("""QPushButton {background-color: #7D5FFF; color: white; border: 2px solid #7D5FFF; border-radius: 10px; padding: 8px 16px;}
            QPushButton:hover {
                background-color: #9B7FFF;
                border: 2px solid #9B7FFF;
            }
            QPushButton:pressed {
                background-color: #4A1FB8;
                border: 2px solid #4A1FB8;
            }
        """)

        self.login_button = QPushButton(self.centralwidget)
        self.login_button.setObjectName("login_button")
        self.login_button.setGeometry(QRect(950, 640, 181, 20))
        self.login_button.setFont(QFont("Segoe UI", 9))
        self.login_button.setStyleSheet("""
            QPushButton {
                background: transparent;
                border: none;
                color: #FFFFFF;
            }
            QPushButton:hover {
                color: #5B3ECC;
            }
        """)

        # Labels for input fields
        font5 = QFont("Segoe UI", 9)
        self.email_label = QLabel(self.centralwidget)
        self.email_label.setObjectName("email_label")
        self.email_label.setGeometry(QRect(820, 310, 78, 16))
        self.email_label.setFont(font5)
        self.email_label.setStyleSheet("color: white; background-color: transparent;")

        self.username = QLabel(self.centralwidget)
        self.username.setObjectName("username")
        self.username.setGeometry(QRect(820, 380, 58, 16))
        self.username.setFont(font5)
        self.username.setStyleSheet("color: white; background-color: transparent;")

        self.password = QLabel(self.centralwidget)
        self.password.setObjectName("password")
        self.password.setGeometry(QRect(820, 450, 54, 16))
        self.password.setFont(font5)
        self.password.setStyleSheet("color: white; background-color: transparent;")

        self.confpass = QLabel(self.centralwidget)
        self.confpass.setObjectName("confpass")
        self.confpass.setGeometry(QRect(820, 520, 100, 16))
        self.confpass.setFont(font5)
        self.confpass.setStyleSheet("color: white; background-color: transparent;")

        signup_create.setCentralWidget(self.centralwidget)

        self.retranslateUi(signup_create)
        QMetaObject.connectSlotsByName(signup_create)

    def retranslateUi(self, signup_create: QWidget):
        signup_create.setWindowTitle(QCoreApplication.translate("signup_create", "CrowdCloud", None))
        self.logo.setText("")
        self.get_started.setText(QCoreApplication.translate("signup_create", "Get Started with Us", None))
        self.create_label.setText(QCoreApplication.translate("signup_create", "Create Account", None))
        self.enter_personal_label.setText(QCoreApplication.translate("signup_create", "Enter your personal information to sign up", None))
        self.email_field.setText("")
        self.username_field.setText("")
        self.password_field.setText("")
        self.confpass_field.setText("")
        self.next_button.setText(QCoreApplication.translate("signup_create", "Next", None))
        self.login_button.setText(QCoreApplication.translate("signup_create", "Already have an account? Log In", None))
        self.email_label.setText(QCoreApplication.translate("signup_create", "Email Address", None))
        self.username.setText(QCoreApplication.translate("signup_create", "Username", None))
        self.password.setText(QCoreApplication.translate("signup_create", "Password", None))
        self.confpass.setText(QCoreApplication.translate("signup_create", "Confirm Password", None))
