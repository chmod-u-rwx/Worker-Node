from PySide6.QtWidgets import QCheckBox, QTableWidgetItem
from PySide6.QtCore import QSize, Qt, QRectF, Property, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QPainter, QPen, QBrush, QColor

from src.worker_node_ui.components.header.toggle_state_manager import ToggleStateManager


class ToggleSwitch(QCheckBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setChecked(ToggleStateManager.get_state())
        self.labels = []
        self.table = None
        self.charts = []
        self.update_func = None

        self._backup_labels = {}
        self._backup_table = []

        self.setFixedSize(60, 34)
        self._checked = ToggleStateManager.get_state()
        self._handle_position = 1.0 if self._checked else 0.0
        self._border_color = QColor("#ffffff")
        self._bg_color_checked = QColor("#4CAF50")
        self._bg_color_unchecked = QColor("#F44336")

        self._animation = QPropertyAnimation(self, b"handle_position")
        self._animation.setDuration(200)
        self._animation.setEasingCurve(QEasingCurve.Type.InOutCubic)

        self.stateChanged.connect(self.on_changed)

        ToggleStateManager.register_listener(self.sync_state)

    def set_widgets(self, labels=None, table=None, charts=None, update_func=None):
        if labels:
            self.labels = labels
        if table:
            self.table = table
        if charts:
            self.charts = charts
        self.update_func = update_func
        self._backup_current_state()

    def _backup_current_state(self):
        self._backup_labels = {label: label.text() for label in self.labels}
        if self.table:
            self._backup_table = [
                [self.table.item(r, c).text() if self.table.item(r, c) else ""
                 for c in range(self.table.columnCount())]
                for r in range(self.table.rowCount())
            ]

    def sync_state(self, value: bool):
        if self._checked != value:
            self.setChecked(value)

    def on_changed(self, state):
        self._checked = bool(state)

        ToggleStateManager.set_state(self._checked)

        self._animation.stop()
        self._animation.setStartValue(0.0 if not self._checked else 1.0)
        self._animation.setEndValue(1.0 if self._checked else 0.0)
        self._animation.start()

        if self._checked:
            for label in self.labels:
                if label in self._backup_labels:
                    label.setText(self._backup_labels[label])
            if self.table:
                self.table.clearContents()
                self.table.setRowCount(len(self._backup_table))
                for r, row_data in enumerate(self._backup_table):
                    for c, value in enumerate(row_data):
                        self.table.setItem(r, c, QTableWidgetItem(value))
            for chart in self.charts:
                chart.show()
        else:
            self._backup_current_state()
            for label in self.labels:
                label.setText("--")
            if self.table:
                self.table.clearContents()
                self.table.setRowCount(0)
            for chart in self.charts:
                chart.hide()

    def get_handle_position(self):
        return self._handle_position

    def set_handle_position(self, pos):
        self._handle_position = pos
        self.update()

    handle_position = Property(float, get_handle_position, set_handle_position)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        rect = self.rect()

        track_color = self._bg_color_checked if self._checked else self._bg_color_unchecked
        painter.setPen(QPen(self._border_color, 1))
        painter.setBrush(QBrush(track_color))
        painter.drawRoundedRect(rect.adjusted(1, 1, -1, -1), rect.height()/2, rect.height()/2)

        margin = 2
        diameter = rect.height() - 2 * margin
        x = margin + (rect.width() - diameter - 2 * margin) * self._handle_position
        y = margin
        painter.setBrush(QBrush(QColor("#ffffff")))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawEllipse(QRectF(x, y, diameter, diameter))

    def sizeHint(self):
        return QSize(60, 34)
