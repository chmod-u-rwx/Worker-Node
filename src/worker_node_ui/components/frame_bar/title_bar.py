from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton
from PySide6.QtCore import Qt


class TitleBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent_window = parent
        self.drag_pos = None

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setStyleSheet("background: transparent;")

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)
        

        layout.addStretch()  # push buttons to the right

        btn_style = """
            QPushButton {
                background: transparent;
                color: white;
                border: none;
                padding: 5px 10px;
            }
        """

        self.min_btn = QPushButton("—")
        self.min_btn.setStyleSheet(btn_style + "QPushButton:hover { background: #ffbd2e; }")
        self.min_btn.clicked.connect(self.parent_window.showMinimized)
        layout.addWidget(self.min_btn)

        self.fullscreen_btn = QPushButton("☐")
        self.fullscreen_btn.setStyleSheet(btn_style)
        self.fullscreen_btn.setEnabled(False)  # disabled look
        layout.addWidget(self.fullscreen_btn)

        self.close_btn = QPushButton("X")
        self.close_btn.setStyleSheet(btn_style + "QPushButton:hover { background: red; }")
        self.close_btn.clicked.connect(self.parent_window.close)
        layout.addWidget(self.close_btn)

        self.drag_pos = None

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton and self.drag_pos:
            if self.parent_window:
                self.parent_window.move(
                    self.parent_window.pos() + event.globalPosition().toPoint() - self.drag_pos
            )
        self.drag_pos = event.globalPosition().toPoint()
