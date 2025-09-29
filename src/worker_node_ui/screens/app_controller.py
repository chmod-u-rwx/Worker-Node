import requests
from PySide6 import QtCore
from src.worker_node_ui.components.dialog.dialog_message import show_custom_error
from src.worker_node_ui.components.helper.session_helper import add_local_fields
from src.worker_node_ui.components.helper.storage_helper import save_session, load_session

from src.worker_node_ui.components.dialog.registration_stack import RegistrationStack
from src.worker_node_ui.components.dialog.dashboard_stack import DashboardStack
from src.worker_node_ui.components.dialog.setting_dialog import SettingsDialog


class AppController:
    BASE_URL = "http://127.0.0.1:8000"

    def __init__(self):
        self.current_user = load_session() or {}
        self.current_email = self.current_user.get("email") if self.current_user else None

        self.registration_stack: RegistrationStack | None = None
        self.dashboard_stack: DashboardStack | None = None
        self.settings_dialog: SettingsDialog | None = None

        self.user_resources = {}

        if self.current_user:
            self.show_dashboard("maindash")
        else:
            self.show_signup()

    def show_login(self):
        if self.dashboard_stack:
            self.dashboard_stack.hide()

        if self.registration_stack is None:
            self.registration_stack = RegistrationStack(self)
        self.registration_stack.show_page("login")
        self.registration_stack.show()
        self.registration_stack.raise_()
        self.registration_stack.activateWindow()

    def show_signup(self, page: str = "signup1"):
        if self.dashboard_stack:
            self.dashboard_stack.hide()

        if self.registration_stack is None:
            self.registration_stack = RegistrationStack(self)
        self.registration_stack.show_page(page)
        self.registration_stack.show()
        self.registration_stack.raise_()
        self.registration_stack.activateWindow()

    def show_dashboard(self, page: str = "maindash"):
        if self.registration_stack:
            self.registration_stack.hide()

        if self.dashboard_stack is None:
            self.dashboard_stack = DashboardStack(self)
        else:
            username = self.current_user.get("username", "") #type:ignore
            email = self.current_user.get("email", "") #type:ignore
            if "maindash" in self.dashboard_stack.pages:
                self.dashboard_stack.pages["maindash"].update_user_info(username, email)

        self.dashboard_stack.show_page(page)
        self.dashboard_stack.show()
        self.dashboard_stack.raise_()
        self.dashboard_stack.activateWindow()

    def show_settings(self, page: str = "main"):
        if self.dashboard_stack is None:
            return

        if self.settings_dialog is None:
            self.settings_dialog = SettingsDialog(self, parent=self.dashboard_stack)

        self.settings_dialog.show_page(page)
        self.settings_dialog.show()
        self.settings_dialog.raise_()
        self.settings_dialog.activateWindow()

    def logout_user(self):
        if self.settings_dialog:
            self.settings_dialog.close()
            self.settings_dialog = None

        if self.dashboard_stack:
            self.dashboard_stack.hide()

        self.current_user = None
        self.current_email = None
        save_session({})

        self.show_login()

    def signup_user(self, user_data):
        try:
            response = requests.post(f"{self.BASE_URL}/users/signup", json=user_data)
            if response.ok:
                api_user = add_local_fields(response.json())
                self.current_user = api_user
                self.current_email = api_user.get("email")
                save_session(api_user)
            else:
                self._handle_api_error(response, "Signup failed")
        except requests.exceptions.RequestException as e:
            show_custom_error(None, f"Connection Error: {str(e)}")

    def login_user(self, credentials):
        try:
            response = requests.post(f"{self.BASE_URL}/users/login", json=credentials)
            if response.ok:
                api_user = add_local_fields(response.json())
                self.current_user = api_user
                self.current_email = api_user.get("email")
                save_session(api_user)
                self.show_dashboard("maindash")
                return True
            else:
                self._handle_api_error(response, "Login failed")
                return False
        except requests.exceptions.RequestException as e:
            show_custom_error(None, f"Connection Error: {str(e)}")
            return False

    def _handle_api_error(self, response, default_message):
        error_message = default_message
        try:
            error_json = response.json()
            if isinstance(error_json, dict) and "detail" in error_json:
                if isinstance(error_json["detail"], str):
                    error_message = error_json["detail"]
                elif isinstance(error_json["detail"], list):
                    error_message = "; ".join(
                        item.get("msg", str(item)) for item in error_json["detail"]
                    )
        except Exception:
            error_message = response.text
        show_custom_error(None, f"{error_message}")
