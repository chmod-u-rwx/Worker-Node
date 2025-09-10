from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QObject, Signal

from src.worker_node_ui.screens.signup_create import SignupWindow
from src.worker_node_ui.screens.signup_tell import SignupTellWindow
from src.worker_node_ui.screens.signup_almost import SignupAlmostWindow
from src.worker_node_ui.screens.signup_fast import SignupToDashboardWindow
from src.worker_node_ui.screens.login import LoginWindow
from src.worker_node_ui.screens.gen_dashboard import MainDashboard
from src.worker_node_ui.screens.info_usage import UsageDashboard
from src.worker_node_ui.screens.info_job import JobDashboard
from src.worker_node_ui.screens.info_earning import EarnDashboard
from src.worker_node_ui.screens.gen_settings import General_Setting
from src.worker_node_ui.screens.edit_settings import Edit_Settings
from src.worker_node_ui.screens.pass_settings import Pass_Settings

"""this controller is for routing between screens, globale states and signal
    between component"""

class AppController(QObject):
    user_updated = Signal()

    def __init__(self):
        super().__init__()
        self.current_window: QWidget | None = None
        self.current_user: str | None = None
        self.current_email: str | None = None
        self.user_resources = {}

# windows/screens
    def _switch_window(self, window_class, *args, **kwargs):
        if self.current_window is not None:
            self.current_window.close()
        self.current_window = window_class(self, *args, **kwargs)
        self.current_window.show()

    def show_signup_create(self):
        self._switch_window(SignupWindow)

    def show_signup_tell(self):
        self._switch_window(SignupTellWindow)

    def show_signup_almost(self):
        self._switch_window(SignupAlmostWindow)

    def show_signup_fast(self):
        self._switch_window(SignupToDashboardWindow)

    def show_login(self):
        self._switch_window(LoginWindow)

    def show_gendashboard(self, username: str | None = None, email: str | None = None):
        if username is None:
            username = self.current_user
        if email is None:
            email = self.current_email
        self._switch_window(MainDashboard, username, email)

    def show_info_usage(self, username: str | None = None, email: str | None = None):
        if username is None:
            username = self.current_user
        if email is None:
            email = self.current_email
        self._switch_window(UsageDashboard, username, email)

    def show_info_job(self, username: str | None = None, email: str | None = None):
        if username is None:
            username = self.current_user
        if email is None:
            email = self.current_email
        self._switch_window(JobDashboard, username, email)

    def show_info_earning(self, username: str | None = None, email: str | None = None):
        if username is None:
            username = self.current_user
        if email is None:
            email = self.current_email
        self._switch_window(EarnDashboard, username, email)
    
# Passing the data to different screens

    def set_user(self, username: str, email: str):
        self.current_user = username
        self.current_email = email
        self.user_updated.emit()

    def save_user_resources(self, data: dict):
        if data:
            self.user_resources.update(data)

    def get_user_resources(self) -> dict | None:
        return self.user_resources
    
# Settings functionalities

    def show_gen_settings(self):
        if not hasattr(self, 'gen_settings') or self.gen_settings is None:
            self.gen_settings = General_Setting(self, parent=self.current_window)
        self.gen_settings.show()
        self._center_widget(self.gen_settings, self.current_window)
        self.gen_settings.raise_()

    def show_edit_settings(self, parent=None):
        self.edit_settings = Edit_Settings(
            controller=self,
            username=self.current_user or "User",
            parent=parent
        )
        self.edit_settings.show()
        if parent:
            self._center_widget(self.edit_settings, parent)
        self.edit_settings.raise_()

    def show_pass_settings(self, parent=None):
        self.pass_settings = Pass_Settings(
            controller=self,
            parent=parent
        )
        self.pass_settings.show()
        if parent:
            self._center_widget(self.pass_settings, parent)
        self.pass_settings.raise_()

    def _center_widget(self, widget, parent):
        parent_rect = parent.geometry()
        widget_rect = widget.rect()
        new_x = parent_rect.center().x() - widget_rect.width() // 2
        new_y = parent_rect.center().y() - widget_rect.height() // 2
        widget.move(new_x, new_y)
