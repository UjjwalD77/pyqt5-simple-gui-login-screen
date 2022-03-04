# import sys

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import source

def display():
    print(line_edit.text())

class Ui_Login_Menu(object):
    def setupUi(self, Login_Menu):
        if not Login_Menu.objectName():
            Login_Menu.setObjectName(u"Login_Menu")
        Login_Menu.resize(422, 614)
        Login_Menu.setMinimumSize(QSize(422, 614))
        Login_Menu.setMaximumSize(QSize(422, 614))
        self.centralwidget = QWidget(Login_Menu)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(u"QFrame {	\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0.534318, x2:0, y2:0.528045, stop:0 rgba(87, 83, 111, 255), stop:1 rgba(57, 54, 72, 255));\n"
"	color: rgb(220, 220, 220);\n"
"	border-radius: 10px;\n"
"}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.text_donthaveaccount = QLabel(self.dropShadowFrame)
        self.text_donthaveaccount.setObjectName(u"text_donthaveaccount")
        self.text_donthaveaccount.setGeometry(QRect(0, 550, 401, 31))
        font = QFont()
        font.setFamily(u"Segoe UI Light")
        font.setPointSize(5)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.text_donthaveaccount.setFont(font)
        self.text_donthaveaccount.setStyleSheet(u"color: rgb(130, 127, 148);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 25 5pt \"Segoe UI Light\";")
        self.text_donthaveaccount.setAlignment(Qt.AlignCenter)
        self.button_login = QPushButton(self.dropShadowFrame)
        self.button_login.setObjectName(u"button_login")
        self.button_login.setEnabled(True)
        self.button_login.setGeometry(QRect(70, 370, 261, 41))
        self.button_login.setCursor(QCursor(Qt.ArrowCursor))
        self.button_login.setMouseTracking(False)
        self.button_login.setLayoutDirection(Qt.LeftToRight)
        self.button_login.setAutoFillBackground(False)
        self.button_login.setStyleSheet(u"QPushButton {\n"
"   background-color: rgb(53, 50, 67);\n"
"   color: rgb(208, 208, 208);\n"
"   font: 12pt \"Segoe UI\";\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	\n"
"	background-color: rgb(55, 52, 70);\n"
"\n"
"}")
        self.button_login.setCheckable(False)
        self.button_login.setAutoRepeat(False)
        self.button_login.setAutoExclusive(False)
        self.button_login.setAutoDefault(True)
        self.button_login.setFlat(False)

        self.text_password = QLineEdit(self.dropShadowFrame)
        self.text_password.setObjectName(u"text_password")
        self.text_password.setEnabled(True)
        self.text_password.setGeometry(QRect(90, 310, 221, 21))
        self.text_password.setAcceptDrops(True)
        self.text_password.setAutoFillBackground(False)
        self.text_password.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(208, 208, 208);\n"
"font: 25 12pt \"Segoe UI Light\";")
        self.text_password.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.text_password.setFrame(False)
        self.text_password.setEchoMode(QLineEdit.Password)
        self.text_password.setAlignment(Qt.AlignCenter)
        self.text_password.setDragEnabled(False)
        self.text_password.setReadOnly(False)
        self.text_password.setClearButtonEnabled(True)
        self.text_forgot = QLabel(self.dropShadowFrame)
        self.text_forgot.setObjectName(u"text_forgot")
        self.text_forgot.setGeometry(QRect(0, 420, 401, 21))
        self.text_forgot.setFont(font)
        self.text_forgot.setStyleSheet(u"\n"
"color: rgb(130, 127, 148);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"font: 25 5pt \"Segoe UI Light\";")
        self.text_forgot.setAlignment(Qt.AlignCenter)
        self.line_password = QFrame(self.dropShadowFrame)
        self.line_password.setObjectName(u"line_password")
        self.line_password.setGeometry(QRect(62, 340, 280, 1))
        self.line_password.setLayoutDirection(Qt.LeftToRight)
        self.line_password.setStyleSheet(u"background-color: rgb(130, 127, 148);")
        self.line_password.setFrameShadow(QFrame.Raised)
        self.line_password.setFrameShape(QFrame.HLine)
        self.line_username = QFrame(self.dropShadowFrame)
        self.line_username.setObjectName(u"line_username")
        self.line_username.setGeometry(QRect(62, 290, 280, 1))
        self.line_username.setLayoutDirection(Qt.LeftToRight)
        self.line_username.setStyleSheet(u"background-color: rgb(130, 127, 148);")
        self.line_username.setFrameShadow(QFrame.Raised)
        self.line_username.setFrameShape(QFrame.HLine)
        self.text_username = QLineEdit(self.dropShadowFrame)
        self.text_username.setObjectName(u"text_username")
        self.text_username.setEnabled(True)
        self.text_username.setGeometry(QRect(90, 260, 221, 21))
        self.text_username.setAcceptDrops(True)
        self.text_username.setAutoFillBackground(False)
        self.text_username.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(208, 208, 208);\n"
"font: 25 12pt \"Segoe UI Light\";")
        self.text_username.setInputMethodHints(Qt.ImhNone)
        self.text_username.setFrame(False)
        self.text_username.setEchoMode(QLineEdit.Normal)
        self.text_username.setAlignment(Qt.AlignCenter)
        self.text_username.setDragEnabled(False)
        self.text_username.setReadOnly(False)
        self.text_username.setClearButtonEnabled(False)
        self.horizontalLayoutWidget = QWidget(self.dropShadowFrame)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 40, 401, 161))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.img_Logo = QLabel(self.horizontalLayoutWidget)
        self.img_Logo.setObjectName(u"img_Logo")
        self.img_Logo.setLayoutDirection(Qt.LeftToRight)
        self.img_Logo.setStyleSheet(u"image: url(:/Logo/img/Logo.png);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.img_Logo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.img_Logo)

        self.icon_user = QLabel(self.dropShadowFrame)
        self.icon_user.setObjectName(u"icon_user")
        self.icon_user.setGeometry(QRect(40, 260, 61, 21))
        self.icon_user.setStyleSheet(u"image: url(:/User/img/user.png);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.icon_lock = QLabel(self.dropShadowFrame)
        self.icon_lock.setObjectName(u"icon_lock")
        self.icon_lock.setGeometry(QRect(40, 310, 61, 21))
        self.icon_lock.setStyleSheet(u"image: url(:/Lock/img/lock.png);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.button_close = QPushButton(self.dropShadowFrame)
        self.button_close.setObjectName(u"button_close")
        self.button_close.setGeometry(QRect(370, 10, 21, 21))
        self.button_close.setStyleSheet(u"QPushButton {\n"
"   border:none;\n"
"   border-radius:8px;\n"
"   background-color: rgb(53, 50, 67);\n"
"   color: rgb(208, 208, 208);\n"
"   font: 6pt \"Segoe UI\";\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(58, 55, 74);\n"
"\n"
"\n"
"}")    
        self.verticalLayout.addWidget(self.dropShadowFrame)

        Login_Menu.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login_Menu)

        self.button_login.setDefault(False)


        QMetaObject.connectSlotsByName(Login_Menu)
    # setupUi

    def retranslateUi(self, Login_Menu):
        Login_Menu.setWindowTitle(QCoreApplication.translate("Login_Menu", u"MainWindow", None))
        self.text_donthaveaccount.setText(QCoreApplication.translate("Login_Menu", u"<html><head/><body><p><span style=\" font-size:11pt;\">Don't have an account? </span><span style=\" font-size:11pt; font-weight:600;\">Create one</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
#endif // QT_CONFIG(tooltip)
        self.button_login.setText(QCoreApplication.translate("Login_Menu", u"Log In", None))
        self.text_password.setInputMask("")
        self.text_password.setText("")
        self.text_password.setPlaceholderText(QCoreApplication.translate("Login_Menu", u"Password", None))
#if QT_CONFIG(whatsthis)
        self.text_forgot.setWhatsThis(QCoreApplication.translate("Login_Menu", u"<html><head/><body><p>Forgot your <span style=\" font-weight:600;\">password?</span></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.text_forgot.setText(QCoreApplication.translate("Login_Menu", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:400;\">Forgot your password?</span></p></body></html>", None))
        self.text_username.setInputMask("")
        self.text_username.setText("")
        self.text_username.setPlaceholderText(QCoreApplication.translate("Login_Menu", u"Username", None))
        self.img_Logo.setText("")
        self.icon_user.setText("")
        self.icon_lock.setText("")
        self.button_close.setText(QCoreApplication.translate("Login_Menu", u"X", None))
    # retranslateUi

