from PySide6.QtWidgets import QToolButton
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize

class ProfileButton:
    def __init__(self, button: QToolButton, controller):
        self.button = button
        self.controller = controller

        self.button.setStyleSheet("""
            QToolButton {
                background: transparent;
                color: white;
                border: 1px solid #ffffff;
                border-radius: 25px;
                padding: 3px;
            }
            QToolButton:hover {
                background-color: #49067c;
            }
        """)
        self.button.setIcon(QIcon("src/worker_node_ui/resources/fbuttons/Profile.png"))
        self.button.setIconSize(QSize(35, 35))
        self.update_tooltip()  # safe now

    def update_tooltip(self):
        username = self.controller.current_user or "Not set"
        email = self.controller.current_email or "Not set"
        tooltip_text = f"""
        <b>Username:</b> {username}<br>
        <b>Email:</b> {email}
        """
        self.button.setToolTip(tooltip_text)
