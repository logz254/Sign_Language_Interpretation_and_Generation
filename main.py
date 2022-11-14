import sys
import time
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QDialog, QSplashScreen, QWidget



class SplashScreen(QSplashScreen):
    def __init__(self):
        super(QSplashScreen, self).__init__()
        loadUi("splash.ui", self)
        self.setWindowFlag(Qt.FramelessWindowHint)  # Setting a frameless window
        pixmap = QPixmap("background.png")
        self.setPixmap(pixmap)

        
    def progress(self):
        for i in range(101):
            time.sleep(0.1)
            self.progressBar.setValue(i)
            

class Dashboard(QDialog):
    def __init__(self):
        super(Dashboard,self).__init__()
        loadUi("dashboard.ui",self)
        self.setFixedWidth(1201)
        self.setFixedHeight(801)

#if __name__ == '__main__':
#main
app = QApplication(sys.argv)
splash = SplashScreen()
splash.show()
splash.progress()
dashboard=Dashboard()

widget=QtWidgets.QStackedWidget()
widget.addWidget(splash)
widget.addWidget(dashboard)
widget.show()
widget.setCurrentIndex(widget.currentIndex()+1)
    
#splash.finish(widget) Don't need this code since QStackedWidget is in use.
app.exec_()
