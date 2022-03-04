import sys, os
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import win32gui, win32con

#HIDE CONSOLE

#hide_console = win32gui.GetForegroundWindow()
#win32gui.ShowWindow(hide_console , win32con.SW_HIDE)

## MAIN MENU

from ui_login_main import *

class Login_Menu(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Login_Menu()
        self.ui.setupUi(self)

        ## REMOVE TITLE BAR
        
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)    

        self.show()

        ## FUNCTIONS

        def button_CloseClicked():
            print("Close Button Clicked")
            window.close()

        def button_LoginClicked(): 
            username = (self.ui.text_username.text())
            password = (self.ui.text_password.text())
            print("Username: ", username)
            print("Password: ", password)
            print("Login Button Clicked")

        self.ui.button_close.clicked.connect(button_CloseClicked)
        self.ui.button_login.clicked.connect(button_LoginClicked)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login_Menu()
    sys.exit(app.exec_())
