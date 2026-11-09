import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from Application_FakeDataGenerator.UI.ui_fakedatagenerator import Ui_w_FakeDataGenerator

class FakeDataGenerator(qtw.QWidget, Ui_w_FakeDataGenerator ):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = FakeDataGenerator()
    window.show()

    sys.exit(app.exec())