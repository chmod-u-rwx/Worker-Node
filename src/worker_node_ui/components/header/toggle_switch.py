from PySide6.QtWidgets import QCheckBox, QVBoxLayout, QTableWidgetItem
from PySide6.QtCore import QSize, Qt, QRectF, Slot, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QPainter, QPen, QBrush, QColor

class ToggleSwitch(QCheckBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setChecked(True)
        self.labels = []
        self.table = None
        self.charts = []
        self.update_func = None

        self._backup_labels = {}
        self._backup_table = []

        self.stateChanged.connect(self.on_changed)

        self.setFixedSize(60, 34)  
        self._checked = True
        self.stateChanged.connect(self.start_transition)
        self._border_color = QColor("#ffffff")
        self._bg_color = QColor(50, 50, 50, 100)

    def set_widgets(self, labels=None, table=None, charts=None, update_func=None):
        if labels:
            self.labels = labels
        if table:
            self.table = table
        if charts:
            self.charts = charts
        self.update_func = update_func

        # Backup initial data
        self._backup_current_state()

    def _backup_current_state(self):
        # Backup labels
        self._backup_labels = {label: label.text() for label in self.labels}
        # Backup table
        if self.table:
            self._backup_table = [
                [self.table.item(row, col).text() if self.table.item(row, col) else ""
                 for col in range(self.table.columnCount())]
                for row in range(self.table.rowCount())
            ]

    @Slot()
    def on_changed(self, state):
        if state == Qt.CheckState.Checked:
            # Restore labels
            for label in self.labels:
                if label in self._backup_labels:
                    label.setText(self._backup_labels[label])
            # Restore table
            if self.table:
                self.table.clearContents()
                self.table.setRowCount(len(self._backup_table))
                for r, row_data in enumerate(self._backup_table):
                    for c, value in enumerate(row_data):
                        self.table.setItem(r, c, QTableWidgetItem(value))
            # Show charts
            for chart in self.charts:
                chart.show()
        else:
            # Backup current state before clearing
            self._backup_current_state()
            # Hide/clear everything
            for label in self.labels:
                label.setText("--")
            if self.table:
                self.table.clearContents()
                self.table.setRowCount(0)
            for chart in self.charts:
                chart.hide()


# toggle appearance
    def start_transition(self, state):
        self._checked = bool(state)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        rect = self.rect()

        # Draw track
        painter.setPen(QPen(self._border_color, 1))
        painter.setBrush(QBrush(self._bg_color))
        painter.drawRoundedRect(rect.adjusted(1, 1, -1, -1),
                                rect.height() / 2, rect.height() / 2)

        # Handle
        margin = 2
        circle_diameter = rect.height() - 2 * margin
        y = (rect.height() - circle_diameter) / 2  # center vertically
        x = rect.width() - circle_diameter - margin if self._checked else margin
        circle_color = QColor("#4CAF50") if self._checked else QColor("#F44336")

        painter.setBrush(QBrush(circle_color))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawEllipse(QRectF(x, y, circle_diameter, circle_diameter))

    def sizeHint(self):
        return QSize(60, 34)  # match the fixed size

