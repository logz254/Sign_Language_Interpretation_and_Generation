import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QSplashScreen,QWidget
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import time
import sqlite3


class SplashScreen(QSplashScreen):
    def __init__(self):
        super(QSplashScreen, self).__init__()
        loadUi("splash.ui", self)
        self.setWindowFlag(Qt.FramelessWindowHint)  # Setting a frameless window
        pixmap = QPixmap("background.png")
        self.setPixmap(pixmap)

    def progress(self):
        for i in range(100):
            time.sleep(0.1)
            self.progressBar.setValue(i)

class Dashboard(QDialog):
    def __init__(self):
        super(QDialog, self).__init__()
        loadUi("dashboard.ui", self)
        self.login1.clicked.connect(self.gotologin)
    
    def gotoLogin(self):
       login1=LoginScreen()
        


class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen,self).__init__()
        loadUi("login.ui",self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    splash = SplashScreen()
    splash.show()
    splash.progress()

    window = Dashboard()
    window.show()

    splash.finish(window)
    app.exec_()
