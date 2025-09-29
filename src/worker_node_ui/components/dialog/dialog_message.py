from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class CustomDialog(QDialog):
    def __init__(self, message, parent=None):
        super().__init__(parent)

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Dialog)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)


        self.central_widget = QWidget(self)
        self.central_widget.setStyleSheet("""
            QWidget {
                border-radius: 30px;
                background-image:url("src/worker_node_ui/resources/images/dialog.png");
                background-repeat: no-repeat;
                background-position: center;
                background-size: cover;
            }
        """)

        layout = QVBoxLayout(self.central_widget)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)

        label = QLabel(message)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setWordWrap(True)
        label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 14px;
                background: transparent;
            }
        """)
        layout.addWidget(label)

        close_btn = QPushButton("OK")
        close_btn.clicked.connect(self.close)
        close_btn.setStyleSheet("""
            QPushButton {
                background-color: #003f7f;
                color: white;
                font-size: 13px;
                padding: 8px 25px;
                border-radius: 10px;
                border: 1px solid white;
            }
            QPushButton:hover {
                background-color: #005fff;
            }
        """)
        layout.addWidget(close_btn, alignment=Qt.AlignmentFlag.AlignCenter)

        font = QFont("Segoe UI", 12)
        self.setFont(font)

        self.central_widget.setFixedSize(500, 180)
        self.resize(self.central_widget.size())

        self.center_on_parent(parent)

    def center_on_parent(self, parent):
        if parent is not None:
            parent_center = parent.frameGeometry().center()
            self_rect = self.frameGeometry()
            self_rect.moveCenter(parent_center)
            self.move(self_rect.topLeft())
        else:
            screen_center = self.screen().availableGeometry().center()
            self_rect = self.frameGeometry()
            self_rect.moveCenter(screen_center)
            self.move(self_rect.topLeft())

def show_custom_error(parent, message: str):
    dlg = CustomDialog(message, parent)
    dlg.exec()
