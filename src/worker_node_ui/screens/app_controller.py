from PySide6.QtWidgets import QWidget
from src.worker_node_ui.screens.signup_create import SignupWindow
from src.worker_node_ui.screens.signup_tell import SignupTellWindow
from src.worker_node_ui.screens.signup_almost import SignupAlmostWindow
from src.worker_node_ui.screens.signup_fast import SignupToDashboardWindow

class AppController:
    def __init__(self):
        self.current_window: QWidget | None = None

    def _switch_window(self, window_class):
        if self.current_window is not None:
            self.current_window.close()
            
        self.current_window = window_class(self)
        self.current_window.show()

    def show_signup_create(self):
        self._switch_window(SignupWindow)

    def show_signup_tell(self):
        self._switch_window(SignupTellWindow)

    def show_signup_almost(self):
        self._switch_window(SignupAlmostWindow)

    def show_signup_fast(self):
        self._switch_window(SignupToDashboardWindow)
