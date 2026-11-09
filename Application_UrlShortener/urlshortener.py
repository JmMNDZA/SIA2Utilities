import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from Application_UrlShortener.UI.ui_urlshortener import Ui_w_UrlShortener


class UrlShortener(qtw.QWidget, Ui_w_UrlShortener):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = UrlShortener()
    window.show()

    sys.exit(app.exec())