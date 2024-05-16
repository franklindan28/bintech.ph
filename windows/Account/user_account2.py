import sys
import re
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
import mysql.connector

import login

sys.path.insert(1,'windows/Landing')
import LandingWin



class User_Account(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowTitle("User Account")
        self.setWindowIcon(QIcon("Images/bintech logo.png"))
        self.setStyleSheet("background-color : #FFFAF3")
    
        layout = QHBoxLayout()

        greeting= QLabel(self)
        greeting.setText("Hello There!")
        greeting.move(300,150)
        greeting.resize(900,100)
        greeting.setStyleSheet("QLabel {  font-size: 80px; font-family: Roboto;font-weight: 900; font-style: normal; color:  #699913; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )
        layout.addWidget(greeting)
       
        profile_btn = QPushButton("View Profile",self)
        profile_btn.setStyleSheet("QPushButton { font-size: 40px; background-color:  #699913; font-family: Roboto;font-weight: 900; font-style: normal; color: white;  border-radius: 20px; }" "QPushButton:pressed { background-color: #0E7470; color:  #FFFFFF;  }" )
        profile_btn.setGeometry(300, 360, 600, 150)
      #  profile_btn.clicked.connect(self.clicked_ViewProfile)

        start_btn = QPushButton("Start Now",self)
        start_btn.setStyleSheet("QPushButton { font-size: 40px; background-color:  #699913; font-family: Roboto;font-weight: 900; font-style: normal; color: white;  border-radius: 20px; }" "QPushButton:pressed { background-color: #0E7470; color:  #FFFFFF;  }" )
        start_btn.setGeometry(300, 580, 600, 150)
        start_btn.clicked.connect(self.clicked_Start)

        logout_btn = QPushButton("Logout",self)
        logout_btn.setStyleSheet("QPushButton { font-size: 40px; background-color:  #699913; font-family: Roboto;font-weight: 900; font-style: normal; color: white;  border-radius: 20px; }" "QPushButton:pressed { background-color: #0E7470; color:  #FFFFFF;  }" )
        logout_btn.setGeometry(300, 800, 600, 150)
        logout_btn.clicked.connect(self.clicked_logout)

        logo = QLabel(self)
        logo.pixmap = QPixmap('Images/BINTECH LOGO.png')
        logo.setPixmap(logo.pixmap)
        logo.resize(logo.pixmap.width(),logo.pixmap.height())
        logo.move(1100,320) 


        self.showFullScreen()



    #def add_window(self):
    #    self.Window2.showMaximized()
    #    self.close()
    def clicked_Start(self):
        self._LandingWin = LandingWin.LandingWindow()
        self.hide()
        self._LandingWin.show()
    

    
    def clicked_logout(self):
        reply = QMessageBox.question(self, 'Logout', 'Are you sure you want to logout?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self._login = login.Login()
            self.close()
            self._login.show()


        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = User_Account()
    sys.exit(app.exec_())
