import re
from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QVBoxLayout
from PySide6.QtCore import Qt

from src.worker_node_ui.styles.signup.ui_py.signup_page1 import UiSignupCreate
from src.worker_node_ui.components.frame_bar.title_bar import TitleBar


class SignupWindow1(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Window)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.resize(1440, 810)

        screen_geometry = QtWidgets.QApplication.primaryScreen().geometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.move(x, y)

        self.ui = UiSignupCreate()
        self.ui.setupUi(self)

        self.title_bar = TitleBar(self)
        container_layout = QVBoxLayout(self)
        container_layout.setContentsMargins(0, 0, 0, 0)
        container_layout.setSpacing(0)
        container_layout.addWidget(self.title_bar, 0, Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight)

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
            label.setStyleSheet(f"color: #7D5FFF; background: {bg_color}; padding: 0 4px;")
            label.adjustSize()

        def float_down():
            if not line_edit.text():
                anim.stop()
                anim.setStartValue(label.pos())
                anim.setEndValue(original_pos)
                anim.start()
                label.setStyleSheet("color: white; background: transparent;")

        original_focus_in = line_edit.focusInEvent
        original_focus_out = line_edit.focusOutEvent

        def new_focus_in(event):
            float_up()
            original_focus_in(event)

        def new_focus_out(event):
            if not line_edit.text():
                float_down()
            original_focus_out(event)

        line_edit.focusInEvent = new_focus_in
        line_edit.focusOutEvent = new_focus_out
        line_edit.textChanged.connect(lambda text: float_up() if text else float_down())

    def add_password_toggle(self, line_edit):
        toggle_btn = QtWidgets.QToolButton(line_edit)
        toggle_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))

        btn_size = 20
        toggle_btn.setFixedSize(btn_size, btn_size)
        toggle_btn.setStyleSheet("QToolButton { border: none; padding: 0px; }")

        frame_width = line_edit.style().pixelMetric(QtWidgets.QStyle.PixelMetric.PM_DefaultFrameWidth)
        toggle_btn.move(
            line_edit.rect().right() - btn_size - frame_width,
            (line_edit.height() - btn_size) // 2,
        )

        eye_icon = QtGui.QIcon(
            QtGui.QPixmap("src/worker_node_ui/resources/fbuttons/eye-512.png").scaled(
                btn_size, btn_size, QtCore.Qt.AspectRatioMode.KeepAspectRatio, QtCore.Qt.TransformationMode.SmoothTransformation 
            )
        )
        toggle_btn.setIcon(eye_icon)
        toggle_btn.setIconSize(QtCore.QSize(btn_size, btn_size))

        toggle_btn.clicked.connect(lambda: self.show_password_temporarily(line_edit))
        line_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        line_edit.setTextMargins(0, 0, btn_size + frame_width, 0)

    def show_password_temporarily(self, line_edit):
        line_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)

        QtCore.QTimer.singleShot(1500, lambda: line_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password))

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

        if len(password) < 8:
            QtWidgets.QMessageBox.warning(self, "Error", "Password must be at least 8 characters long!")
            return

        if password != confpass:
            QtWidgets.QMessageBox.warning(self, "Error", "Passwords do not match!")
            return

        self.controller.current_user = username
        self.controller.current_email = email
        print(f"[DEBUG] Stored in controller: user={username}, email={email}")

        self.hide()
        self.controller.show_signup_widget2()

    def handle_login(self):
        self.hide()
        self.controller.show_login()
