import sys
import ctypes
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from src.worker_node_ui.screens.app_controller import AppController


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("src/worker_node_ui/resources/images/desk_logo.png"))
    myappid = u"CrowdCloud.app"
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    controller = AppController()
    app.lastWindowClosed.connect(app.quit)
    sys.exit(app.exec())



    
