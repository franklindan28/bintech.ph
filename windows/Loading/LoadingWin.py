import sys
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QMessageBox, QLineEdit,QApplication,QHBoxLayout,QLabel,QMainWindow,QPushButton,QStackedLayout,QVBoxLayout,QWidget,QListWidget,QPlainTextEdit)
from PyQt5.QtGui import *
from PyQt5 import QtWidgets

import main

sys.path.insert(1,'windows/Insert')
import InsertWin



class LoadingWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowTitle("Loading")
        self.setStyleSheet("background-color : #FFFAF3")
        self.help_btn()
        self.welcome_to_plark()
        self.logout_btn()
        self.additional_info()
        self.step_1()
        self.step1()
        self.done_btn()
        #self.Window5 = NewWindow4()
        self.showMaximized()
        
        #print("WINDOW 33333333")

    def help_btn(self):
        help = help_button = QPushButton(" ", self)
        help_button.setGeometry(20, 20, 55, 55)
        help.setStyleSheet("QPushButton:pressed { background-color: #0ef5a0 ; color:  #0E7470;  }" "QPushButton { shadow: 0px; background-image : url(Images/material-symbols_info.png);  border-radius: 30px;}")
        #help.clicked.connect(self.print)

    def welcome_to_plark(self):
        layout2 = QHBoxLayout()
        #widget1 = QListWidget()
        title2 = QLabel(self)
        title2.setText("Welcome to PLARK")
        title2.move(150,20)
        title2.resize(1000,60)
        title2.setAlignment(QtCore.Qt.AlignCenter)
        title2.setStyleSheet("QLabel { font-weight: 900; font-size: 40px; font-family: Roboto;font-weight: 900; font-style: normal; color: #0E7470; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )
        layout2.addWidget(title2)
    
    def additional_info(self):
        layout3 = QHBoxLayout()
        #widget1 = QListWidget()
        title3 = QLabel(self)
        title3.setText("TrashCash Plastic Recovery Kiosk")
        title3.move(150,80)
        title3.resize(1000,60)
        title3.setAlignment(QtCore.Qt.AlignCenter)
        title3.setStyleSheet("QLabel { font-weight: 400; font-size: 40px; font-family: Roboto; font-style: normal; color: #0E7470; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )
        layout3.addWidget(title3)
        
    def logout_btn(self):
        logout = logout_button = QPushButton(" ", self)
        logout_button.setGeometry(1280, 20, 55, 55)
        logout.setStyleSheet("QPushButton:pressed { background-color: #0ef5a0 ; color:  #0E7470;  }" "QPushButton { shadow: 0px; background-image : url(Images/material-symbols_logout.png);  border-radius: 0px;}")
        logout.clicked.connect(self.clickedLogout)

    def step_1(self):
        step_1_info = QLabel(self)
        step_1_info.setText("Please put your plastic waste to the hole.")
        step_1_info.move(500,565)
        step_1_info.resize(600,80)
        step_1_info.setStyleSheet("QLabel { font-weight: 700; font-size: 20px; font-family: Roboto; font-style: normal; color: #0E7470; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )
       
    def step1(self):
        step_1 = QLabel(self)
        step_1.pixmap = QPixmap('Images/Waste management-rafiki 1.png')
        step_1.setPixmap(step_1.pixmap)
        step_1.resize(step_1.pixmap.width(),step_1.pixmap.height())
        step_1.move(500,160)   # Subjected to change for monitor size


    def done_btn(self):
        done = done_button = QPushButton("Done", self)
        done_button.setGeometry(0, 670, 1500, 60)
        done.setStyleSheet("QPushButton:pressed { background-color: #0ef5a0 ; color:  #0E7470;  }" "QPushButton { background-color: #0E7470; font-size: 40px;   border-radius: 0px; color: white;}")
        done.clicked.connect(self.clickedInsert)

    def clickedInsert(self):
        self._InsertWin = InsertWin.InsertWindow()
        self._InsertWin.show()
        self.hide()

    def clickedLogout(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Are you sure you want to logout?")
        msgBox.setWindowTitle("TrashCash")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        #msgBox.buttonClicked.connect(msgButtonClick)
        #msgBox.show()

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Yes:
            self._LoginWin = main.Login()
            self._LoginWin.show()
            self.hide()
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = LoadingWindow()
    sys.exit(app.exec_())