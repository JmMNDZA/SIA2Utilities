# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_window.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)
import Icons_rc

class Ui_W_LoginForm(object):
    def setupUi(self, W_LoginForm):
        if not W_LoginForm.objectName():
            W_LoginForm.setObjectName(u"W_LoginForm")
        W_LoginForm.resize(398, 431)
        font = QFont()
        font.setPointSize(12)
        W_LoginForm.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Main/utilities.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        W_LoginForm.setWindowIcon(icon)
        self.gridLayout = QGridLayout(W_LoginForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = QPushButton(W_LoginForm)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 13, 1, 1, 2)

        self.groupBox = QGroupBox(W_LoginForm)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.le_UserID = QLineEdit(self.groupBox)
        self.le_UserID.setObjectName(u"le_UserID")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.SpanningRole, self.le_UserID)

        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.checkBox)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.label_3)

        self.le_Password = QLineEdit(self.groupBox)
        self.le_Password.setObjectName(u"le_Password")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.SpanningRole, self.le_Password)


        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 3)

        self.pb_Ok = QPushButton(W_LoginForm)
        self.pb_Ok.setObjectName(u"pb_Ok")

        self.gridLayout.addWidget(self.pb_Ok, 6, 0, 1, 3)

        self.label_4 = QLabel(W_LoginForm)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 13, 0, 1, 1)

        self.label_Message = QLabel(W_LoginForm)
        self.label_Message.setObjectName(u"label_Message")
        font1 = QFont()
        font1.setPointSize(8)
        self.label_Message.setFont(font1)
        self.label_Message.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_Message, 4, 0, 1, 3)

        self.pb_Cancel = QPushButton(W_LoginForm)
        self.pb_Cancel.setObjectName(u"pb_Cancel")

        self.gridLayout.addWidget(self.pb_Cancel, 3, 0, 1, 3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer_2, 7, 0, 1, 3)


        self.retranslateUi(W_LoginForm)

        QMetaObject.connectSlotsByName(W_LoginForm)
    # setupUi

    def retranslateUi(self, W_LoginForm):
        W_LoginForm.setWindowTitle(QCoreApplication.translate("W_LoginForm", u"SIA2 Utilities", None))
        self.pushButton.setText(QCoreApplication.translate("W_LoginForm", u"Sign up", None))
        self.groupBox.setTitle(QCoreApplication.translate("W_LoginForm", u"Welcome", None))
        self.label.setText(QCoreApplication.translate("W_LoginForm", u"Username", None))
        self.label_2.setText(QCoreApplication.translate("W_LoginForm", u"Password", None))
        self.checkBox.setText(QCoreApplication.translate("W_LoginForm", u"Remember me", None))
        self.label_3.setText(QCoreApplication.translate("W_LoginForm", u"Forgot Password?", None))
        self.pb_Ok.setText(QCoreApplication.translate("W_LoginForm", u"Google", None))
        self.label_4.setText(QCoreApplication.translate("W_LoginForm", u"Already have an account?", None))
        self.label_Message.setText(QCoreApplication.translate("W_LoginForm", u"or Sign In with", None))
        self.pb_Cancel.setText(QCoreApplication.translate("W_LoginForm", u"Login", None))
    # retranslateUi

