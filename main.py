import sys

from PySide6 import QtWidgets as qtw

from Application_FakeDataGenerator.fakedatagenerator import FakeDataGenerator
from Application_Home.home import Home
from Application_Login.login import LoginForm
from Application_SignUp.signup import SignUpWindow
from Application_UrlShortener.urlshortener import UrlShortener


class Application:
    def __init__(self):
        self.login_window = LoginForm()
        self.signup_window = SignUpWindow()
        self.home_window = Home()
        self.url_shortener_window = UrlShortener()
        self.fake_data_window = FakeDataGenerator()
        self.windows = (
            self.login_window,
            self.signup_window,
            self.home_window,
            self.url_shortener_window,
            self.fake_data_window,
        )

        self.login_window.pushButton.clicked.connect(
            lambda: self.show_window(self.signup_window)
        )
        self.login_window.pb_Cancel.clicked.connect(
            lambda: self.show_window(self.home_window)
        )
        self.signup_window.login_requested.connect(
            lambda: self.show_window(self.login_window)
        )
        self.signup_window.signup_successful.connect(
            lambda _username: self.show_window(self.login_window)
        )
        self.home_window.pushButton.clicked.connect(
            lambda: self.show_window(self.url_shortener_window)
        )
        self.home_window.pushButton_3.clicked.connect(
            lambda: self.show_window(self.fake_data_window)
        )
        self.home_window.pushButton_4.clicked.connect(
            lambda: self.show_window(self.login_window)
        )
        self.url_shortener_window.pushButton_2.clicked.connect(
            lambda: self.show_window(self.home_window)
        )
        self.fake_data_window.pushButton_4.clicked.connect(
            lambda: self.show_window(self.home_window)
        )

    def show_window(self, window):
        for current_window in self.windows:
            current_window.hide()

        window.show()


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    application = Application()
    application.show_window(application.login_window)
    sys.exit(app.exec())