from PySide6.QtWidgets import QToolButton, QFrame, QVBoxLayout, QLabel, QWidget
from PySide6.QtCore import QRect, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QColor


class NotificationHandler:
    def __init__(self, button: QToolButton, parent: QWidget):
        self.button = button
        self.parent = parent
        self.notifications = []
        self.bar_width = 200
        self.bar_height = 150
        self.is_expanded = False

        # --- Red dot indicator ---
        self.red_dot = QWidget(self.button)
        self.red_dot.setGeometry(QRect(30, 0, 12, 12))
        self.red_dot.setStyleSheet("background-color: red; border-radius: 6px;")
        self.red_dot.hide()

        # --- Notification bar ---
        self.notif_bar = QFrame(parent)
        self.notif_bar.setGeometry(QRect(button.x() - 150, button.y() + 60, self.bar_width, 0))
        self.notif_bar.setStyleSheet("background-color: #2C2C2C; border-radius: 8px;")
        self.notif_bar.setVisible(False)

        self.layout = QVBoxLayout(self.notif_bar)
        self.layout.setContentsMargins(10, 10, 10, 10)
        self.layout.setSpacing(5)

        # --- Animation ---
        self.anim = QPropertyAnimation(self.notif_bar, b"geometry")
        self.anim.setDuration(200)
        self.anim.setEasingCurve(QEasingCurve.Type.OutQuad)

        # --- Connect button ---
        self.button.clicked.connect(self.toggle_notifications)

    def add_notification(self, text: str):
        label = QLabel(text, self.notif_bar)
        label.setStyleSheet("color: white;")
        self.layout.addWidget(label)
        self.notifications.append(label)
        self.red_dot.show()

    def clear_notifications(self):
        for label in self.notifications:
            self.layout.removeWidget(label)
            label.deleteLater()
        self.notifications.clear()
        self.red_dot.hide()

    def toggle_notifications(self):
        if self.is_expanded:
            self.collapse()
        else:
            self.expand()

    def expand(self):
        self.notif_bar.setVisible(True)
        start_rect = QRect(self.notif_bar.x(), self.notif_bar.y(), self.bar_width, 0)
        end_rect = QRect(self.notif_bar.x(), self.notif_bar.y(), self.bar_width, self.bar_height)
        self.anim.stop()
        self.anim.setStartValue(start_rect)
        self.anim.setEndValue(end_rect)
        self.anim.start()
        self.is_expanded = True
        self.red_dot.hide()

    def collapse(self):
        start_rect = QRect(self.notif_bar.x(), self.notif_bar.y(), self.bar_width, self.bar_height)
        end_rect = QRect(self.notif_bar.x(), self.notif_bar.y(), self.bar_width, 0)
        self.anim.stop()
        self.anim.setStartValue(start_rect)
        self.anim.setEndValue(end_rect)
        self.anim.finished.connect(lambda: self.notif_bar.setVisible(False))
        self.anim.start()
        self.is_expanded = False
