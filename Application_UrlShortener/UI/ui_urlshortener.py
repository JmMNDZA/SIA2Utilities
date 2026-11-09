# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'urlshortener.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_w_UrlShortener(object):
    def setupUi(self, w_UrlShortener):
        if not w_UrlShortener.objectName():
            w_UrlShortener.setObjectName(u"w_UrlShortener")
        w_UrlShortener.resize(392, 238)
        self.gridLayout = QGridLayout(w_UrlShortener)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = QPushButton(w_UrlShortener)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 3, 1, 1, 2)

        self.pushButton_2 = QPushButton(w_UrlShortener)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 3, 0, 1, 1)

        self.groupBox = QGroupBox(w_UrlShortener)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineEdit)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.SpanningRole, self.label_2)

        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.SpanningRole, self.lineEdit_2)

        self.pushButton_3 = QPushButton(self.groupBox)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.SpanningRole, self.pushButton_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(3, QFormLayout.ItemRole.LabelRole, self.verticalSpacer)


        self.gridLayout.addWidget(self.groupBox, 2, 0, 1, 3)


        self.retranslateUi(w_UrlShortener)

        QMetaObject.connectSlotsByName(w_UrlShortener)
    # setupUi

    def retranslateUi(self, w_UrlShortener):
        w_UrlShortener.setWindowTitle(QCoreApplication.translate("w_UrlShortener", u"Url Shortener", None))
        self.pushButton.setText(QCoreApplication.translate("w_UrlShortener", u"Shorten URL", None))
        self.pushButton_2.setText(QCoreApplication.translate("w_UrlShortener", u"Home", None))
        self.groupBox.setTitle(QCoreApplication.translate("w_UrlShortener", u"SIA2Utilities URL Shortener", None))
        self.label.setText(QCoreApplication.translate("w_UrlShortener", u"Input URL", None))
        self.label_2.setText(QCoreApplication.translate("w_UrlShortener", u"Generated URL:", None))
        self.pushButton_3.setText(QCoreApplication.translate("w_UrlShortener", u"Copy", None))
    # retranslateUi

