# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_home_window.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_w_home(object):
    def setupUi(self, w_home):
        if not w_home.objectName():
            w_home.setObjectName(u"w_home")
        w_home.resize(543, 456)
        self.gridLayout = QGridLayout(w_home)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_4 = QPushButton(w_home)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.pushButton_4, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.label = QLabel(w_home)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.groupBox = QGroupBox(w_home)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.groupBox)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 2)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_3, 2, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 2)


        self.gridLayout.addWidget(self.groupBox, 2, 0, 1, 3)


        self.retranslateUi(w_home)

        QMetaObject.connectSlotsByName(w_home)
    # setupUi

    def retranslateUi(self, w_home):
        w_home.setWindowTitle(QCoreApplication.translate("w_home", u"SIA2Utilities Home", None))
        self.pushButton_4.setText(QCoreApplication.translate("w_home", u"Sign Out", None))
        self.label.setText(QCoreApplication.translate("w_home", u"Profile Name", None))
        self.groupBox.setTitle(QCoreApplication.translate("w_home", u"Home", None))
        self.label_2.setText(QCoreApplication.translate("w_home", u"Mendoza, John Michael", None))
        self.pushButton.setText(QCoreApplication.translate("w_home", u"URL Shortener", None))
        self.pushButton_2.setText(QCoreApplication.translate("w_home", u"SMS / Email", None))
        self.pushButton_3.setText(QCoreApplication.translate("w_home", u"Fake Data Generator", None))
        self.label_3.setText(QCoreApplication.translate("w_home", u"Bonifacio, Jurys Jacob", None))
        self.label_4.setText(QCoreApplication.translate("w_home", u"Made by", None))
    # retranslateUi

