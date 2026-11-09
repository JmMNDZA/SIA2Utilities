# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fakedatagenerator.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QWidget)

class Ui_w_FakeDataGenerator(object):
    def setupUi(self, w_FakeDataGenerator):
        if not w_FakeDataGenerator.objectName():
            w_FakeDataGenerator.setObjectName(u"w_FakeDataGenerator")
        w_FakeDataGenerator.resize(458, 493)
        self.gridLayout = QGridLayout(w_FakeDataGenerator)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(w_FakeDataGenerator)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.groupBox)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_2.addWidget(self.pushButton_4, 2, 1, 1, 1)

        self.scrollArea = QScrollArea(self.groupBox)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 400, 374))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lineEdit_4 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_3.addWidget(self.lineEdit_4, 8, 0, 1, 2)

        self.label = QLabel(self.scrollAreaWidgetContents_3)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 2, 0, 1, 1)

        self.comboBox_8 = QComboBox(self.scrollAreaWidgetContents_3)
        self.comboBox_8.setObjectName(u"comboBox_8")

        self.gridLayout_3.addWidget(self.comboBox_8, 12, 2, 1, 1)

        self.lineEdit_3 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_3.addWidget(self.lineEdit_3, 7, 0, 1, 2)

        self.comboBox_7 = QComboBox(self.scrollAreaWidgetContents_3)
        self.comboBox_7.setObjectName(u"comboBox_7")

        self.gridLayout_3.addWidget(self.comboBox_7, 11, 2, 1, 1)

        self.lineEdit_10 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.gridLayout_3.addWidget(self.lineEdit_10, 14, 0, 1, 2)

        self.comboBox_9 = QComboBox(self.scrollAreaWidgetContents_3)
        self.comboBox_9.setObjectName(u"comboBox_9")

        self.gridLayout_3.addWidget(self.comboBox_9, 13, 2, 1, 1)

        self.lineEdit = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_3.addWidget(self.lineEdit, 5, 0, 1, 2)

        self.comboBox_5 = QComboBox(self.scrollAreaWidgetContents_3)
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.gridLayout_3.addWidget(self.comboBox_5, 9, 2, 1, 1)

        self.comboBox_3 = QComboBox(self.scrollAreaWidgetContents_3)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.gridLayout_3.addWidget(self.comboBox_3, 7, 2, 1, 1)

        self.lineEdit_8 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout_3.addWidget(self.lineEdit_8, 12, 0, 1, 2)

        self.lineEdit_6 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_3.addWidget(self.lineEdit_6, 10, 0, 1, 2)

        self.lineEdit_7 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout_3.addWidget(self.lineEdit_7, 11, 0, 1, 2)

        self.comboBox_10 = QComboBox(self.scrollAreaWidgetContents_3)
        self.comboBox_10.setObjectName(u"comboBox_10")

        self.gridLayout_3.addWidget(self.comboBox_10, 14, 2, 1, 1)

        self.comboBox_6 = QComboBox(self.scrollAreaWidgetContents_3)
        self.comboBox_6.setObjectName(u"comboBox_6")

        self.gridLayout_3.addWidget(self.comboBox_6, 10, 2, 1, 1)

        self.comboBox_4 = QComboBox(self.scrollAreaWidgetContents_3)
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.gridLayout_3.addWidget(self.comboBox_4, 8, 2, 1, 1)

        self.comboBox = QComboBox(self.scrollAreaWidgetContents_3)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_3.addWidget(self.comboBox, 5, 2, 1, 1)

        self.lineEdit_9 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout_3.addWidget(self.lineEdit_9, 13, 0, 1, 2)

        self.label_2 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 2, 2, 1, 1)

        self.lineEdit_2 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_3.addWidget(self.lineEdit_2, 6, 0, 1, 2)

        self.lineEdit_5 = QLineEdit(self.scrollAreaWidgetContents_3)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_3.addWidget(self.lineEdit_5, 9, 0, 1, 2)

        self.comboBox_2 = QComboBox(self.scrollAreaWidgetContents_3)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_3.addWidget(self.comboBox_2, 6, 2, 1, 1)

        self.pushButton_3 = QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_3.addWidget(self.pushButton_3, 1, 0, 1, 2)

        self.pushButton_2 = QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_3.addWidget(self.pushButton_2, 1, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout_3.addItem(self.verticalSpacer, 3, 0, 1, 3)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 2, 1, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 0, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 1, 0, 1, 2)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)


        self.retranslateUi(w_FakeDataGenerator)

        QMetaObject.connectSlotsByName(w_FakeDataGenerator)
    # setupUi

    def retranslateUi(self, w_FakeDataGenerator):
        w_FakeDataGenerator.setWindowTitle(QCoreApplication.translate("w_FakeDataGenerator", u"SIA2Utilities Fake Data Generator", None))
        self.groupBox.setTitle(QCoreApplication.translate("w_FakeDataGenerator", u"Fake Data Generator", None))
        self.pushButton.setText(QCoreApplication.translate("w_FakeDataGenerator", u"Save as..", None))
        self.pushButton_4.setText(QCoreApplication.translate("w_FakeDataGenerator", u"Home", None))
        self.label.setText(QCoreApplication.translate("w_FakeDataGenerator", u"Field", None))
        self.comboBox_5.setCurrentText("")
        self.label_2.setText(QCoreApplication.translate("w_FakeDataGenerator", u"Type", None))
        self.pushButton_3.setText(QCoreApplication.translate("w_FakeDataGenerator", u"Generate Fake Data", None))
        self.pushButton_2.setText(QCoreApplication.translate("w_FakeDataGenerator", u"View", None))
    # retranslateUi

