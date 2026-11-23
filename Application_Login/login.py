
import sys

from PySide6 import QtWidgets as qtw
from PySide6 import QtCore as qtc

from Application_Login.UI.ui_login_window import Ui_W_LoginForm
from Application_Database.database import UserDatabase


class LoginForm(qtw.QWidget, Ui_W_LoginForm):

    # Signal emitted only after successful authentication
    login_successful = qtc.Signal(str)

    def __init__(self):
        super().__init__()

        self.setupUi(self)

        # Initialize shared database
        self.database = UserDatabase()

        # Hide password by default
        self.le_Password.setEchoMode(
            qtw.QLineEdit.EchoMode.Password
        )

        # Connect Login button
        self.pb_Cancel.clicked.connect(self.login)

        # Connect password visibility checkbox
        self.checkBox.toggled.connect(self.toggle_password)

    # ==========================================
    # SHOW / HIDE PASSWORD
    # ==========================================

    def toggle_password(self, checked):

        if checked:
            self.le_Password.setEchoMode(
                qtw.QLineEdit.EchoMode.Normal
            )
        else:
            self.le_Password.setEchoMode(
                qtw.QLineEdit.EchoMode.Password
            )

    # ==========================================
    # LOGIN AUTHENTICATION
    # ==========================================

    def login(self):

        username = self.le_UserID.text().strip()
        password = self.le_Password.text()

        # Check empty fields
        if not username or not password:

            qtw.QMessageBox.warning(
                self,
                "Missing Information",
                "Please enter your username and password."
            )

            return

        try:

            # Verify account using SQLite
            success, message = self.database.login_user(
                username,
                password
            )

            if not success:

                qtw.QMessageBox.warning(
                    self,
                    "Login Failed",
                    message
                )

                self.label_Message.setText(message)

                # Stop here. Do not navigate to Homepage.
                return

            # Only successful authentication reaches this section
            qtw.QMessageBox.information(
                self,
                "Login Successful",
                message
            )

            self.label_Message.setText(message)

            # Notify main.py that authentication succeeded
            self.login_successful.emit(username)

        except Exception as error:

            qtw.QMessageBox.critical(
                self,
                "Database Error",
                str(error)
            )

            return


# ==========================================
# RUN APPLICATION
# ==========================================

if __name__ == "__main__":

    app = qtw.QApplication(sys.argv)

    window = LoginForm()
    window.show()

    sys.exit(app.exec())
