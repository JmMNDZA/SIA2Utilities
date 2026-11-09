import sys
import re
import importlib.util
from pathlib import Path

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QLineEdit
from PySide6.QtCore import Signal

# Load the Qt Designer interface.
try:
    from .UI.ui_signup_window import Ui_SignUpForm
except ImportError:
    from UI.ui_signup_window import Ui_SignUpForm


# ==========================================
# LOAD EXISTING DATABASE.PY
# ==========================================

CURRENT_DIRECTORY = Path(__file__).resolve().parent

database_locations = [
    CURRENT_DIRECTORY / "database.py",
    CURRENT_DIRECTORY / "UI" / "database.py",
    CURRENT_DIRECTORY.parent / "database.py",
    CURRENT_DIRECTORY.parent / "UI" / "database.py",
    CURRENT_DIRECTORY.parents[1] / "database.py",
]

UserDatabase = None

for database_file in database_locations:
    if database_file.is_file():
        spec = importlib.util.spec_from_file_location(
            "signup_database",
            database_file
        )

        if spec is None or spec.loader is None:
            continue

        database_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(database_module)

        UserDatabase = getattr(database_module, "UserDatabase", None)

        if UserDatabase is not None:
            break

if UserDatabase is None:
    searched_locations = "\n".join(str(path) for path in database_locations)
    raise FileNotFoundError(
        "Cannot find UserDatabase in database.py.\n\n"
        "Locations checked:\n" + searched_locations
    )


# ==========================================
# SIGN UP WINDOW
# ==========================================

class SignUpWindow(QWidget):

    login_requested = Signal()
    signup_successful = Signal(str)

    def __init__(self):
        super().__init__()

        self.database = UserDatabase()

        # Load and display the Qt Designer form.
        self.ui = Ui_SignUpForm()
        self.ui.setupUi(self)

        # Keep the same window size as the original GUI.
        self.setWindowTitle("SIA2 Utilities")
        self.setFixedSize(500, 650)

        # Make the Designer widgets available to the existing methods.
        self.username_input = self.ui.username_input
        self.email_input = self.ui.email_input
        self.password_input = self.ui.password_input
        self.confirm_password_input = self.ui.confirm_password_input
        self.show_password = self.ui.show_password

        self.signup_button = self.ui.signup_button
        self.google_button = self.ui.google_button
        self.login_button = self.ui.login_button

        # Connect GUI actions to the existing application functions.
        self.show_password.toggled.connect(
            self.toggle_password_visibility
        )
        self.signup_button.clicked.connect(
            self.register_account
        )
        self.login_button.clicked.connect(
            self.go_to_login
        )

    # ======================================
    # SHOW / HIDE PASSWORD
    # ======================================

    def toggle_password_visibility(self, checked):
        mode = (
            QLineEdit.EchoMode.Normal
            if checked
            else QLineEdit.EchoMode.Password
        )

        self.password_input.setEchoMode(mode)
        self.confirm_password_input.setEchoMode(mode)

    # ======================================
    # EMAIL VALIDATION
    # ======================================

    def validate_email(self, email):
        pattern = r"^[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,}$"
        return re.match(pattern, email) is not None

    # ======================================
    # INPUT VALIDATION
    # ======================================

    def validate_inputs(self):
        username = self.username_input.text().strip()
        email = self.email_input.text().strip()
        password = self.password_input.text()
        confirm_password = self.confirm_password_input.text()

        if not username or not email or not password or not confirm_password:
            QMessageBox.warning(
                self,
                "Missing Information",
                "Please complete all fields."
            )
            return False

        if len(username) < 3:
            QMessageBox.warning(
                self,
                "Invalid Username",
                "Username must contain at least 3 characters."
            )
            return False

        if not self.validate_email(email):
            QMessageBox.warning(
                self,
                "Invalid Email",
                "Please enter a valid email address."
            )
            return False

        if len(password) < 8:
            QMessageBox.warning(
                self,
                "Weak Password",
                "Password must contain at least 8 characters."
            )
            return False

        if password != confirm_password:
            QMessageBox.warning(
                self,
                "Password Mismatch",
                "Passwords do not match."
            )
            return False

        return True

    # ======================================
    # REGISTER ACCOUNT
    # ======================================

    def register_account(self):
        if not self.validate_inputs():
            return

        username = self.username_input.text().strip()
        email = self.email_input.text().strip()
        password = self.password_input.text()

        try:
            success, message = self.database.register_user(
                username,
                email,
                password
            )

            if success:
                QMessageBox.information(
                    self,
                    "Registration Successful",
                    message
                )

                self.signup_successful.emit(username)
                self.clear_fields()

            else:
                QMessageBox.warning(
                    self,
                    "Registration Failed",
                    message
                )

        except Exception as error:
            QMessageBox.critical(
                self,
                "Database Error",
                str(error)
            )

    # ======================================
    # CLEAR FIELDS
    # ======================================

    def clear_fields(self):
        self.username_input.clear()
        self.email_input.clear()
        self.password_input.clear()
        self.confirm_password_input.clear()
        self.show_password.setChecked(False)

    # ======================================
    # RETURN TO LOGIN
    # ======================================

    def go_to_login(self):
        self.login_requested.emit()
        self.close()


# ==========================================
# RUN APPLICATION
# ==========================================

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = SignUpWindow()
    window.show()

    sys.exit(app.exec())
