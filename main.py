import sys
import time
import sqlite3
import bcrypt
import subprocess
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
        self.login1.clicked.connect(self.gotologin)
        self.create.clicked.connect(self.gotocreate)

    def gotologin(self):
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def gotocreate(self):
        create=CreateAccountScreen()
        widget.addWidget(create)
        widget.setCurrentIndex(widget.currentIndex()+1)

class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen,self).__init__()
        loadUi("log_in.ui",self)
        self.password_login.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login2.clicked.connect(self.loginfunction)
    
    def loginfunction(self):
        user=self.username_login.text()
        password=self.password_login.text()

        if len(user)==0 or len(password)==0:
            self.error.setText("Please fill all fields.")
        
        else:

            passBytes=password.encode('utf-8')
            

            conn = sqlite3.connect("user_data.db")
            cur = conn.cursor()
            query = 'SELECT Password FROM Login_info WHERE Username =\''+user+"\'"
            cur.execute(query)
            result_pass = cur.fetchone()[0]
            result_pass2 = bcrypt.checkpw(passBytes,result_pass)
            if result_pass2 == True:
                print("Successfully logged in.")
                self.error.setText("")
                option=OptionScreen()
                widget.addWidget(option)
                widget.setCurrentIndex(widget.currentIndex()+1)
            else:
                self.error.setText("Invalid username or password!")

class CreateAccountScreen(QDialog):
   def __init__(self):
        super(CreateAccountScreen,self).__init__()
        loadUi("sign_up.ui",self)
        self.password_signup.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpass_signup.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signup1.clicked.connect(self.signupfunction)

   def signupfunction(self):
        user =self.username_signup.text()
        fname =self.fname_signup.text()
        lname =self.lname_signup.text()
        phonenumber=self.phoneno_signup.text()
        password =self.password_signup.text()
        confirmpass =self.confirmpass_signup.text()

        if len(user)==0 or len(fname)==0 or len(lname)==0 or len(phonenumber)==0 or len(password)==0 or len(confirmpass)==0:
            self.error.setText("Please fill in all the fields")
        
        elif password!=confirmpass:
            self.error.setText("Passwords do not match")

        else:

            #Hashing Password
            passBytes=password.encode('utf-8')
            salt=bcrypt.gensalt()
            hashedpassword=bcrypt.hashpw(passBytes,salt)

            conn = sqlite3.connect("user_data.db")
            cur = conn.cursor()
            user_info=[user,fname,lname,phonenumber,hashedpassword]
            cur.execute('INSERT INTO Login_info (Username,Fname,Lname,Phone_number,Password) VALUES (?,?,?,?,?)',user_info)

            conn.commit()
            conn.close()

            login = LoginScreen()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex()+1)

class OptionScreen(QDialog):
    def __init__(self):
        super(OptionScreen,self).__init__()
        loadUi("option.ui",self)
        self.generation_btn.clicked.connect(self.gotogeneration)

    def gotogeneration(self):
        subprocess.call([r'C:\Users\Allan\Documents\STRATHMORE\4_YEAR\IS_PROJECT_II\project\Sign_Language_Interpretation_and_Generation\Generation'])





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
