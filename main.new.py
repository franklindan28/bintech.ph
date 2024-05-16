import sys
import re
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QLineEdit,QApplication,QHBoxLayout,QLabel,QMainWindow,QPushButton,QStackedLayout,QVBoxLayout,QWidget,QListWidget,QPlainTextEdit)
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
sys.path.insert(2,'/home/jetson/FINAL_KIOSK')
#import plastic_detection

#from plastic_detection import * 

#from flask import Flask, jsonify, request
#import requests
#import json

#URL = "https://jsonplaceholder.typicode.com/users"  

#response = requests.get(URL)

#if response.status_code == 200:
    # Get the data from the API response
#    data = response.json()
#    print(data)
#else:
#    print("Request failed with status code:", response.status_code)
#Other Win

sys.path.insert(1,'windows/Landing')
import LandingWin

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowTitle("Login")
        self.setWindowIcon(QIcon("Images/trashcashlogosymbolunstrace copy 1.png"))
        self.setStyleSheet("background-color : #FFFAF3")
        #self.setWindowFlag(Qt.FramelessWindowHint)
        #self.plastic_detection = main()
        layout = QHBoxLayout()
       # widget1 = QListWidget()
        title = QLabel(self)
        title.setText("TrashCash Kiosks")
        title.move(150,40)
        title.resize(500,100)
        title.setStyleSheet("QLabel { font-weight: 900; font-size: 50px; font-family: Roboto;font-weight: 900; font-style: normal; color: #0E7470; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )
        layout.addWidget(title)

        greeting= QLabel(self)
        #print(self.detect_res.my_text())
        greeting.setText("Hello There!")
        greeting.move(150,200)
        greeting.resize(500,100)
        greeting.setStyleSheet("QLabel { font-weight: 900; font-size: 50px; font-family: Roboto;font-weight: 900; font-style: normal; color: #0E7470; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )
        layout.addWidget(greeting)

        email = QLineEdit(self)
        email.setPlaceholderText("Email")
        email.move(150,300)
        email.resize(500,70)
        email.setStyleSheet("QLineEdit {  line-height: 42px; background-color: #FFFFFF; font-weight: 400; font-size: 20px; font-family: Roboto; font-style: normal; color: #979797; border-radius: 20px; padding-left: 24px; }" )
      #  layout.addWidget(username)

        password= QtWidgets.QLineEdit(self)
        password.setEchoMode(QLineEdit.Password)
        password.setPlaceholderText("Password")
        password.move(150,400)
        password.resize(500,70)
        password.setStyleSheet(" QLineEdit { line-height: 42px; background-color: #FFFFFF; font-weight: 400; font-size: 20px; font-family: Roboto; font-style: normal; color: #979797; border-radius: 20px; position: absolute; padding-left: 24px;}" )

        log_btn = QPushButton("Login",self)
        log_btn.setStyleSheet("QPushButton { font-size: 40px; background-color: #0E7470; font-family: Roboto;font-weight: 900; font-style: normal; color: white;  border-radius: 20px; }" "QPushButton:pressed { background-color: #0ef5a0 ; color:  #0E7470;  }" )
        log_btn.setGeometry(150, 500, 500, 70)
        log_btn.clicked.connect(self.clickedLanding)
        layout2 = QHBoxLayout()
        add = QLabel(self)
        add.pixmap = QPixmap('Images/trashcashlogosymbolunstrace copy 1.png')
        add.setPixmap(add.pixmap)
        add.resize(add.pixmap.width(),add.pixmap.height())
        add.move(800,200)   # Subjected to change for monitor size
        layout2.addWidget(add)
        self.setLayout(layout2)

        self.showFullScreen()

  #  def user_account(self):
   #     User = [
    #        {
     #           "Email": input(" "),
      #          "Password": input(" ")
       #     }
       # ]
    
    #def add_window(self):
    #    self.Window2.showMaximized()
    #    self.close()
    def clickedLanding(self):
        self._LandingWin = LandingWin.LandingWindow()
        self.hide()
        self._LandingWin.show()
        
        
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    #app.setStyleSheet(stylesheet)
    ex = Login()
    sys.exit(app.exec_())
