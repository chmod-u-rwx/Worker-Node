from PySide6.QtWidgets import QWidget, QStackedWidget, QVBoxLayout
from PySide6.QtCore import Signal
from PySide6.QtCore import Qt

from src.worker_node_ui.screens.login_page import LoginWindow

from src.worker_node_ui.screens.signup_page1 import SignupWindow1
from src.worker_node_ui.screens.signup_page2 import SignupWindow2
from src.worker_node_ui.screens.signup_page3 import SignupWindow3
from src.worker_node_ui.screens.signup_page4 import SignupWindow4

from src.worker_node_ui.screens.dashboard_page import MainDashboard
from src.worker_node_ui.screens.information_usage import UsageWindow
from src.worker_node_ui.screens.information_jobs import JobWindow
from src.worker_node_ui.screens.information_earnings import EarnWindow

from src.worker_node_ui.screens.setting_main import MainSetting
from src.worker_node_ui.screens.setting_password import PasswordSetting
from src.worker_node_ui.screens.setting_profile import ProfileSetting



class AppController:
    # manage which window to show

    def __init__(self):
        self.current_user = None
        self.current_email = None
        self.user_resource = {}

        self.signup_create = SignupWindow1(self)
        self.signup_tell = SignupWindow2(self)
        self.signup_almost = SignupWindow3(self)
        self.signup_fast = SignupWindow4(self)
        self.login = LoginWindow(self)

        self.show_signup_widget1()

    def hide_all(self):
        for app in [
            self.signup_create,
            self.signup_tell,
            self.signup_almost,
            self.signup_fast,
            self.login,
            getattr(self, 'dashboard', None),
            getattr(self, 'earningdashboard', None),
            getattr(self, 'jobdashboard', None),
            getattr(self, 'usagedashboard', None),
            getattr(self, 'mainsetting', None),
            getattr(self, 'passwordsetting', None),
            getattr(self, 'profilesetting', None),
        ]:
            if app:
                app.hide()


    def show_signup_widget1(self):
        self.hide_all()
        self.signup_create.show()

    def show_signup_widget2(self):
        self.hide_all()
        self.signup_tell.show()

    def show_signup_widget3(self):
        self.hide_all()
        self.signup_almost.show()

    def show_signup_widget4(self):
        self.hide_all()
        self.signup_fast.show()

    def show_login(self):
        self.hide_all()
        self.login.show()

    def show_dashboard(self, username=None, email=None):
        if not getattr(self, 'dashboard', None):
            self.dashboard = MainDashboard(self, username=username or "", email=email or "")
        if username and email:
            self.dashboard.update_user_info(username, email)

        self.hide_all()
        self.dashboard.show()
    
    def show_earning_dashboard(self, username=None, email=None):
        if not getattr(self, 'earningdashboard', None):
            self.earningdashboard = EarnWindow(self, username=username or "", email=email or "")
        if username and email:
            self.earningdashboard.update_user_info(username, email)

        self.hide_all()
        self.earningdashboard.show()

    def show_job_dashboard(self, username=None, email=None):
        if not getattr(self, 'jobdashboard', None):
            self.jobdashboard = JobWindow(self, username=username or "", email=email or "")
        if username and email:
            self.jobdashboard.update_user_info(username, email)

        self.hide_all()
        self.jobdashboard.show()

    def show_usage_dashboard(self, username=None, email=None):
        if not getattr(self, 'usagedashboard', None):
            self.usagedashboard = UsageWindow(self, username=username or "", email=email or "")
        if username and email:
            self.usagedashboard.update_user_info(username, email)

        self.hide_all()
        self.usagedashboard.show()


    def show_main_settings(self):
        if not getattr(self, 'mainsetting', None):
            self.main_settings = MainSetting(self)

        self.main_settings.show()
        self.main_settings.raise_()

    def show_password_settings(self):
        if not getattr(self, 'passwordsetting', None):
            self.password_settings = PasswordSetting(self)

        self.password_settings.show()
        self.password_settings.raise_()

    def show_profile_settings(self):
        if not getattr(self, 'profilesetting', None):
            self.profile_settings = ProfileSetting(self)

        self.profile_settings.show()
        self.profile_settings.raise_()



    