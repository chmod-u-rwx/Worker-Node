from PySide6.QtWidgets import QToolButton, QFrame, QVBoxLayout, QLabel, QWidget
from PySide6.QtCore import QRect, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QColor

from src.worker_node_ui.components.header.notification_state_manager import NotificationManager

class NotificationHandler:
    def __init__(self, button: QToolButton, parent: QWidget):
        self.button = button
        self.parent = parent
        self.notifications = []
        self.bar_width = 180
        self.bar_height = 120
        self.is_expanded = False

        self.red_dot = QWidget(self.button)
        self.red_dot.setGeometry(QRect(30, 0, 12, 12))
        self.red_dot.setStyleSheet("background-color: red; border-radius: 6px;")
        self.red_dot.hide()

        self.notif_bar = QFrame(parent)
        self.notif_bar.setGeometry(QRect(button.x() - 140, button.y() + 50, self.bar_width, 0))
        self.notif_bar.setStyleSheet("background-color: #2C2C2C; border-radius: 8px;")
        self.notif_bar.setVisible(False)

        self.layout = QVBoxLayout(self.notif_bar)
        self.layout.setContentsMargins(8, 8, 8, 8)
        self.layout.setSpacing(4)

        self.anim = QPropertyAnimation(self.notif_bar, b"geometry")
        self.anim.setDuration(200)
        self.anim.setEasingCurve(QEasingCurve.Type.OutQuad)

        self.button.clicked.connect(self.toggle_notifications)

        NotificationManager.register_handler(self)

    def update_notifications(self, notifications: list[str], has_unread: bool):
        for label in self.notifications:
            self.layout.removeWidget(label)
            label.deleteLater()
        self.notifications.clear()

        for text in notifications:
            label = QLabel(text, self.notif_bar)
            label.setStyleSheet("color: white;")
            self.layout.addWidget(label)
            self.notifications.append(label)

        if has_unread and not self.is_expanded:
            self.red_dot.show()
        else:
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
        
        NotificationManager.mark_all_as_read()


    def collapse(self):
        start_rect = QRect(self.notif_bar.x(), self.notif_bar.y(), self.bar_width, self.bar_height)
        end_rect = QRect(self.notif_bar.x(), self.notif_bar.y(), self.bar_width, 0)
        self.anim.stop()
        self.anim.setStartValue(start_rect)
        self.anim.setEndValue(end_rect)
        self.anim.finished.connect(lambda: self.notif_bar.setVisible(False))
        self.anim.start()
        self.is_expanded = False
