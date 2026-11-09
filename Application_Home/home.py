import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from Application_Home.UI.ui_ui_home_window import Ui_w_home


class Home(qtw.QWidget, Ui_w_home):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = Home()
    window.show()

    sys.exit(app.exec())