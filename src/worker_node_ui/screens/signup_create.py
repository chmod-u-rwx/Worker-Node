from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QLabel, QLineEdit
from src.worker_node_ui.styles.signup_ui_py.signup_create_ui import Ui_signup_create
import re

class SignupWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.ui = Ui_signup_create()
        self.ui.setupUi(self)

        self.setWindowIcon(QtGui.QIcon("src/worker_node_ui/resources/images/desk_logo"".png"))

        self.setup_floating_labels()
        self.add_password_toggle(self.ui.password_field)
        self.add_password_toggle(self.ui.confpass_field)
        self.setup_logic()

    def setup_floating_labels(self):
        self.add_floating_label(self.ui.email_field, self.ui.email_label)
        self.add_floating_label(self.ui.username_field, self.ui.username)
        self.add_floating_label(self.ui.password_field, self.ui.password)
        self.add_floating_label(self.ui.confpass_field, self.ui.confpass)

    def add_floating_label(self, line_edit: QLineEdit, label: QLabel):
        original_pos = label.pos()
        float_pos = QtCore.QPoint(label.x(), original_pos.y() - 20)

        anim = QtCore.QPropertyAnimation(label, b"pos", self)
        anim.setDuration(150)
        anim.setEasingCurve(QtCore.QEasingCurve.Type.InOutQuad)

        bg_color = "#00031F"

        def float_up():
            anim.stop()
            anim.setStartValue(label.pos())
            anim.setEndValue(float_pos)
            anim.start()
            label.setStyleSheet(f"""color: #7D5FFF; background: {bg_color}; padding: 0 4px;""")
            label.adjustSize()

        def float_down():
            if not line_edit.text():
                anim.stop()
                anim.setStartValue(label.pos())
                anim.setEndValue(original_pos)
                anim.start()
                label.setStyleSheet("color: white; background: transparent;")

        original_focus_in = line_edit.focusInEvent
        def new_focus_in(event):
            float_up()
            original_focus_in(event)

        original_focus_out = line_edit.focusOutEvent
        def new_focus_out(event):
            if not line_edit.text():
                float_down()
            original_focus_out(event)

        line_edit.focusInEvent = new_focus_in
        line_edit.focusOutEvent = new_focus_out
        line_edit.textChanged.connect(lambda text: float_up() if text else float_down())

    def add_password_toggle(self, line_edit):
        toggle_btn = QtWidgets.QToolButton(line_edit)
        toggle_btn.setIcon(QtGui.QIcon.fromTheme("view-hidden"))
        toggle_btn.setCheckable(True)
        toggle_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        frame_width = line_edit.style().pixelMetric(QtWidgets.QStyle.PixelMetric.PM_DefaultFrameWidth)
        toggle_btn.setStyleSheet("QToolButton { border: none; padding: 0px; }")
        toggle_btn.setFixedSize(20, 20)
        toggle_btn.move(
            line_edit.rect().right() - toggle_btn.width() - frame_width,
            (line_edit.height() - toggle_btn.height()) // 2,
        )

        toggle_btn.clicked.connect(lambda: self.toggle_password(toggle_btn, line_edit))

        line_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        line_edit.setTextMargins(0, 0, toggle_btn.width() + frame_width, 0)

    def toggle_password(self, button, line_edit):
        if button.isChecked():
            button.setIcon(QtGui.QIcon.fromTheme("view-visible"))
            line_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        else:
            button.setIcon(QtGui.QIcon.fromTheme("view-hidden"))
            line_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
    
    def validate_email(self, email):
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(pattern, email) is not None

    def setup_logic(self):
        self.ui.next_button.clicked.connect(self.handle_next)
        self.ui.login_button.clicked.connect(self.handle_login)

    def handle_next(self):
        email = self.ui.email_field.text().strip()
        username = self.ui.username_field.text().strip()
        password = self.ui.password_field.text()
        confpass = self.ui.confpass_field.text()

        if not email or not username or not password or not confpass:
            QtWidgets.QMessageBox.warning(self, "Error", "All fields are required!")
            return

        if not self.validate_email(email):
            QtWidgets.QMessageBox.warning(self, "Error", "Invalid email address!")
            return

        if password != confpass:
            QtWidgets.QMessageBox.warning(self, "Error", "Passwords do not match!")
            return

        self.close()
        self.controller.show_signup_tell()

    def handle_login(self):
        self.controller.show_login()
