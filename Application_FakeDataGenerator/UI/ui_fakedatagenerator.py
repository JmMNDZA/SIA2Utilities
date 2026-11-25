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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QLabel, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

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
        self.pushButton_3 = QPushButton(self.groupBox)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_2.addWidget(self.pushButton_3, 4, 0, 1, 2)

        self.scrollArea = QScrollArea(self.groupBox)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 408, 371))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.scrollAreaWidgetContents_3)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.checkBox = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_2.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout_2.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout_2.addWidget(self.checkBox_3)

        self.checkBox_4 = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.verticalLayout_2.addWidget(self.checkBox_4)

        self.checkBox_5 = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.verticalLayout_2.addWidget(self.checkBox_5)

        self.checkBox_6 = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.verticalLayout_2.addWidget(self.checkBox_6)

        self.checkBox_9 = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_9.setObjectName(u"checkBox_9")

        self.verticalLayout_2.addWidget(self.checkBox_9)

        self.checkBox_7 = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.verticalLayout_2.addWidget(self.checkBox_7)

        self.checkBox_8 = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_8.setObjectName(u"checkBox_8")

        self.verticalLayout_2.addWidget(self.checkBox_8)

        self.checkBox_10 = QCheckBox(self.scrollAreaWidgetContents_3)
        self.checkBox_10.setObjectName(u"checkBox_10")

        self.verticalLayout_2.addWidget(self.checkBox_10)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.label_3 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.spinBox = QSpinBox(self.scrollAreaWidgetContents_3)
        self.spinBox.setObjectName(u"spinBox")

        self.verticalLayout_2.addWidget(self.spinBox)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 2)

        self.pushButton_4 = QPushButton(w_FakeDataGenerator)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.pushButton_4, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 1)


        self.retranslateUi(w_FakeDataGenerator)

        QMetaObject.connectSlotsByName(w_FakeDataGenerator)
    # setupUi

    def retranslateUi(self, w_FakeDataGenerator):
        w_FakeDataGenerator.setWindowTitle(QCoreApplication.translate("w_FakeDataGenerator", u"SIA2Utilities Fake Data Generator", None))
        self.groupBox.setTitle(QCoreApplication.translate("w_FakeDataGenerator", u"Fake Data Generator", None))
        self.pushButton_3.setText(QCoreApplication.translate("w_FakeDataGenerator", u"Generate Data", None))
        self.label.setText(QCoreApplication.translate("w_FakeDataGenerator", u"Choose fields", None))
        self.checkBox.setText(QCoreApplication.translate("w_FakeDataGenerator", u"id", None))
        self.checkBox_2.setText(QCoreApplication.translate("w_FakeDataGenerator", u"first_name", None))
        self.checkBox_3.setText(QCoreApplication.translate("w_FakeDataGenerator", u"last_name", None))
        self.checkBox_4.setText(QCoreApplication.translate("w_FakeDataGenerator", u"age", None))
        self.checkBox_5.setText(QCoreApplication.translate("w_FakeDataGenerator", u"gender", None))
        self.checkBox_6.setText(QCoreApplication.translate("w_FakeDataGenerator", u"email", None))
        self.checkBox_9.setText(QCoreApplication.translate("w_FakeDataGenerator", u"job", None))
        self.checkBox_7.setText(QCoreApplication.translate("w_FakeDataGenerator", u"race", None))
        self.checkBox_8.setText(QCoreApplication.translate("w_FakeDataGenerator", u"language", None))
        self.checkBox_10.setText(QCoreApplication.translate("w_FakeDataGenerator", u"city", None))
        self.label_3.setText(QCoreApplication.translate("w_FakeDataGenerator", u"Rows", None))
        self.pushButton_4.setText(QCoreApplication.translate("w_FakeDataGenerator", u"Home", None))
    # retranslateUi

