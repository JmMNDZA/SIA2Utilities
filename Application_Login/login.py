import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from Application_Login.UI.ui_login_window import Ui_W_LoginForm

class LoginForm(qtw.QWidget, Ui_W_LoginForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = LoginForm()
    window.show()

    sys.exit(app.exec())