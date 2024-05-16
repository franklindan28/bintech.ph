import sys
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QMessageBox, QLineEdit,QApplication,QHBoxLayout,QLabel,QMainWindow,QPushButton,QStackedLayout,QVBoxLayout,QWidget,QListWidget,QPlainTextEdit)
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import main
sys.path.insert(1,'windows/QR')
import QRWin

class TransactionWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowTitle("Tranaction")
        self.setStyleSheet("background-color : #FFFAF3")
        self.help_btn()
        self.welcome_to_plark()
        self.logout_btn()
        self.additional_info()
        self.review_transaction()
        self.next_btn()
     #   self.Window5 = NewWindow4()
        self.showMaximized()

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

    def review_transaction(self):
        review_transact = QLabel(self)
        review_transact.setText("Please Review")
        review_transact.move(50,150)
        review_transact.resize(300,50)
        review_transact.setStyleSheet("QLabel { font-weight: 700; font-size: 40px; font-family: Roboto; font-style: normal; color: #0E7470; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )
        step_2_info1 = QLabel(self)
        step_2_info1.setText("Category")
        step_2_info1.move(50,200)
        step_2_info1.resize(300,40)
        step_2_info1.setStyleSheet("QLabel { font-weight: 700; font-size: 20px; font-family: Roboto; font-style: normal; color: #0E7470; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )
        step_2_info2 = QLabel(self)
        step_2_info2.setText("Weight")
        step_2_info2.move(270,200)
        step_2_info2.resize(300,40)
        step_2_info2.setStyleSheet("QLabel { font-weight: 700; font-size: 20px; font-family: Roboto; font-style: normal; color: #0E7470; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )
        step_2_info3 = QLabel(self)
        step_2_info3.setText("Points")
        step_2_info3.move(270,200)
        step_2_info3.resize(300,40)
        step_2_info3.setStyleSheet("QLabel { font-weight: 700; font-size: 20px; font-family: Roboto; font-style: normal; color: #0E7470; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )

    def next_btn(self):
        next = next_button = QPushButton("Next", self)
        next_button.setGeometry(0, 670, 1500, 60)
        next.setStyleSheet("QPushButton:pressed { background-color: #0ef5a0 ; color:  #0E7470;  }" "QPushButton { background-color: #0E7470; font-size: 40px;   border-radius: 0px; color: white;}")
        next.clicked.connect(self.clickedQR)

    def clickedQR(self):
        self._QRWin = QRWin.QRWindow()
        self._QRWin.show()
        self.hide()

    def clickedLogout(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Are you sure you want to logout?")
        msgBox.setWindowTitle("TrashCash")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        #msgBox.buttonClicked.connect(msgButtonClick)
        #msgBox.show()

    def chart(self):
        


        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Yes:
            self._LoginWin = main.Login()
            self._LoginWin.show()
            self.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = TransactionWindow()
    sys.exit(app.exec_())