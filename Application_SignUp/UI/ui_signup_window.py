# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'signup_window.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_SignUpForm(object):
    def setupUi(self, SignUpForm):
        if not SignUpForm.objectName():
            SignUpForm.setObjectName(u"SignUpForm")
        SignUpForm.resize(500, 650)
        SignUpForm.setStyleSheet(u"QWidget {\n"
"    background-color: #1E1E1E;\n"
"    color: white;\n"
"    font-family: Arial;\n"
"    font-size: 18px;\n"
"}\n"
"QGroupBox {\n"
"    border: 1px solid #999999;\n"
"    border-radius: 7px;\n"
"    margin-top: 12px;\n"
"    padding-top: 10px;\n"
"    font-size: 19px;\n"
"}\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0 5px;\n"
"    color: white;\n"
"}\n"
"QLabel {\n"
"    color: white;\n"
"    background: transparent;\n"
"}\n"
"QLineEdit {\n"
"    background-color: #2B2B2B;\n"
"    color: white;\n"
"    border: 1px solid #393939;\n"
"    border-radius: 6px;\n"
"    padding: 5px 8px;\n"
"    font-size: 17px;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 1px solid #777777;\n"
"}\n"
"QCheckBox {\n"
"    spacing: 8px;\n"
"    color: white;\n"
"    font-size: 17px;\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 19px;\n"
"    height: 19px;\n"
"    border: 1px solid #AAAAAA;\n"
"    border-radius: 6px;\n"
"    background-color: #1E1E"
                        "1E;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #444444;\n"
"    border: 1px solid #AAAAAA;\n"
"}\n"
"QPushButton {\n"
"    background-color: #2B2B2B;\n"
"    color: white;\n"
"    border: 1px solid #393939;\n"
"    border-radius: 6px;\n"
"    font-size: 19px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #393939;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #444444;\n"
"}")
        self.main_layout = QVBoxLayout(SignUpForm)
        self.main_layout.setSpacing(12)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(17, 15, 17, 12)
        self.welcome_group = QGroupBox(SignUpForm)
        self.welcome_group.setObjectName(u"welcome_group")
        self.group_layout = QVBoxLayout(self.welcome_group)
        self.group_layout.setSpacing(9)
        self.group_layout.setObjectName(u"group_layout")
        self.group_layout.setContentsMargins(13, 17, 13, 15)
        self.username_label = QLabel(self.welcome_group)
        self.username_label.setObjectName(u"username_label")

        self.group_layout.addWidget(self.username_label)

        self.username_input = QLineEdit(self.welcome_group)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setMinimumSize(QSize(0, 36))

        self.group_layout.addWidget(self.username_input)

        self.email_label = QLabel(self.welcome_group)
        self.email_label.setObjectName(u"email_label")

        self.group_layout.addWidget(self.email_label)

        self.email_input = QLineEdit(self.welcome_group)
        self.email_input.setObjectName(u"email_input")
        self.email_input.setMinimumSize(QSize(0, 36))

        self.group_layout.addWidget(self.email_input)

        self.password_label = QLabel(self.welcome_group)
        self.password_label.setObjectName(u"password_label")

        self.group_layout.addWidget(self.password_label)

        self.password_input = QLineEdit(self.welcome_group)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setMinimumSize(QSize(0, 36))
        self.password_input.setEchoMode(QLineEdit.Password)

        self.group_layout.addWidget(self.password_input)

        self.confirm_label = QLabel(self.welcome_group)
        self.confirm_label.setObjectName(u"confirm_label")

        self.group_layout.addWidget(self.confirm_label)

        self.confirm_password_input = QLineEdit(self.welcome_group)
        self.confirm_password_input.setObjectName(u"confirm_password_input")
        self.confirm_password_input.setMinimumSize(QSize(0, 36))
        self.confirm_password_input.setEchoMode(QLineEdit.Password)

        self.group_layout.addWidget(self.confirm_password_input)

        self.show_password = QCheckBox(self.welcome_group)
        self.show_password.setObjectName(u"show_password")

        self.group_layout.addWidget(self.show_password)


        self.main_layout.addWidget(self.welcome_group)

        self.top_stretch = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.main_layout.addItem(self.top_stretch)

        self.signup_button = QPushButton(SignUpForm)
        self.signup_button.setObjectName(u"signup_button")
        self.signup_button.setMinimumSize(QSize(0, 38))

        self.main_layout.addWidget(self.signup_button)

        self.google_label = QLabel(SignUpForm)
        self.google_label.setObjectName(u"google_label")
        self.google_label.setAlignment(Qt.AlignCenter)

        self.main_layout.addWidget(self.google_label)

        self.google_button = QPushButton(SignUpForm)
        self.google_button.setObjectName(u"google_button")
        self.google_button.setMinimumSize(QSize(0, 38))

        self.main_layout.addWidget(self.google_button)

        self.bottom_stretch = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.main_layout.addItem(self.bottom_stretch)

        self.bottom_layout = QHBoxLayout()
        self.bottom_layout.setObjectName(u"bottom_layout")
        self.already_label = QLabel(SignUpForm)
        self.already_label.setObjectName(u"already_label")

        self.bottom_layout.addWidget(self.already_label)

        self.login_button = QPushButton(SignUpForm)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setMinimumSize(QSize(0, 38))

        self.bottom_layout.addWidget(self.login_button)


        self.main_layout.addLayout(self.bottom_layout)


        self.retranslateUi(SignUpForm)

        QMetaObject.connectSlotsByName(SignUpForm)
    # setupUi

    def retranslateUi(self, SignUpForm):
        SignUpForm.setWindowTitle(QCoreApplication.translate("SignUpForm", u"SIA2 Utilities", None))
        self.welcome_group.setTitle(QCoreApplication.translate("SignUpForm", u"Welcome", None))
        self.username_label.setText(QCoreApplication.translate("SignUpForm", u"Username", None))
        self.email_label.setText(QCoreApplication.translate("SignUpForm", u"Email Address", None))
        self.password_label.setText(QCoreApplication.translate("SignUpForm", u"Password", None))
        self.confirm_label.setText(QCoreApplication.translate("SignUpForm", u"Confirm Password", None))
        self.show_password.setText(QCoreApplication.translate("SignUpForm", u"Show Password", None))
        self.signup_button.setText(QCoreApplication.translate("SignUpForm", u"Create Account", None))
        self.google_label.setText(QCoreApplication.translate("SignUpForm", u"or Sign Up with", None))
        self.google_button.setText(QCoreApplication.translate("SignUpForm", u"Google", None))
        self.already_label.setText(QCoreApplication.translate("SignUpForm", u"Already have an account?", None))
        self.login_button.setText(QCoreApplication.translate("SignUpForm", u"Log In", None))
    # retranslateUi

