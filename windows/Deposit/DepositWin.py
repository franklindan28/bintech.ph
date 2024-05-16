import sys
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QMessageBox, QLineEdit,QApplication,QHBoxLayout,QLabel,QMainWindow,QPushButton,QStackedLayout,QVBoxLayout,QWidget,QListWidget,QPlainTextEdit)
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
from PyQt5 import QtWidgets
import main
sys.path.insert(1,'windows/Loading')
import LoadingWin


class DepositWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowTitle("Deposit")
        self.setStyleSheet("background-color : #FFFAF3")
        self.help_btn1()
        self.welcome_to_plark1()
        self.logout_btn1()
        self.additional_info1()
        self.deposit_btn1()
        self.next_btn1()
        #self.Window4 = NewWindow3()

        self.showMaximized()

    def help_btn1(self):
        help = help_button = QPushButton(" ", self)
        help_button.setGeometry(20, 20, 55, 55)
        help.setStyleSheet("QPushButton:pressed { background-color: #0ef5a0 ; color:  #0E7470;  }" "QPushButton { shadow: 0px; background-image : url(Images/material-symbols_info.png);  border-radius: 30px;}")
        #help.clicked.connect(self.print)

    def welcome_to_plark1(self):
        layout2 = QHBoxLayout()
        #widget1 = QListWidget()
        title2 = QLabel(self)
        title2.setText("Welcome to PLARK")
        title2.move(150,20)
        title2.resize(1000,60)
        title2.setAlignment(QtCore.Qt.AlignCenter)
        title2.setStyleSheet("QLabel { font-weight: 900; font-size: 40px; font-family: Roboto;font-weight: 900; font-style: normal; color: #0E7470; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )
        layout2.addWidget(title2)
    
    def additional_info1(self):
        layout3 = QHBoxLayout()
        #widget1 = QListWidget()
        title3 = QLabel(self)
        title3.setText("TrashCash Plastic Recovery Kiosk")
        title3.move(150,80)
        title3.resize(1000,60)
        title3.setAlignment(QtCore.Qt.AlignCenter)
        title3.setStyleSheet("QLabel { font-weight: 400; font-size: 40px; font-family: Roboto; font-style: normal; color: #0E7470; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )
        layout3.addWidget(title3)
        
    def logout_btn1(self):
        logout = logout_button = QPushButton(" ", self)
        logout_button.setGeometry(1280, 20, 55, 55)
        logout.setStyleSheet("QPushButton:pressed { background-color: #0ef5a0 ; color:  #0E7470;  }" "QPushButton { background-image : url(Images/material-symbols_logout.png);  border-radius: 0px;}")
        logout.clicked.connect(self.clickedLogout)

    def deposit_btn1(self):
        deposit = deposit_button = QPushButton("Deposit", self)
        deposit_button.setIcon(QIcon('Images/plastic-containers-icon copy 1.png'))
        #deposit2  = QPushButton(" ", self)
        deposit_button.setGeometry(500, 220, 390, 370)
       # deposit2.setStyleSheet("QPushButton:pressed { background-color: #0ef5a0 ; color:  #0E7470;  }" "QPushButton { image : url(Images/plastic-container-icon copy 1.png); color: white; background-color: #0E7470;}" )
        deposit.setStyleSheet("QPushButton:pressed { background-color: #0ef5a0 ; color:  #0E7470;  }" "QPushButton { padding-top: 40px;  text-align: center; font-family: 'Roboto'; background-color: #0E7470; font-size: 40px;   border-radius: 30px; color: white;}" )
        #start.clicked.connect(self.)

    def next_btn1(self):
        next = next_button = QPushButton("Next", self)
        next_button.setGeometry(0, 670, 1500, 60)
        next.setStyleSheet("QPushButton:pressed { background-color: #0ef5a0 ; color:  #0E7470;  }" "QPushButton { background-color: #0E7470; font-size: 40px;   border-radius: 0px; color: white;}")
        next.clicked.connect(self.clickedLoading)
    
    def clickedLoading(self):
        self._LoadingWin = LoadingWin.LoadingWindow()
        self._LoadingWin.show()
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
    ex = DepositWindow()
    sys.exit(app.exec_())