import sys
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QMessageBox, QLineEdit,QApplication,QHBoxLayout,QLabel,QMainWindow,QPushButton,QStackedLayout,QVBoxLayout,QWidget,QListWidget,QPlainTextEdit)
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
'''import ultralytics
import cv2
import argparse
#import onnxruntime as ort

from ultralytics import YOLO
import supervision as sv
import numpy as np

from pprint import pprint
import re
import time
import torch

torch.cuda.set_device(0)

from plastic_detection import main
'''

sys.path.insert(1,'windows/Deposit')
import DepositWin

#sys.path.insert(2,'/home/jetson/FINAL_KIOSK')
#import plastic_detection

#from plastic_detection import * 

class LandingWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowTitle("Welcome Screen 1")
        self.setStyleSheet("background-color : #FFFAF3")
        self.help_btn()
        self.welcome_to_plark()
        self.logout_btn()
        self.additional_info()
        self.step_1()
        self.step1()
        self.step_2()
        self.step2()
        self.step_3()
        self.step3()
        self.start_btn()
        #self.Window3 = NewWindow2()
        self.showMaximized()
   #     self.plastic_detection = main()
    #    self.detection()

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
        step_1_info.setText("Put your recyclables""\n""\r\r\r\r\r\r\r\r\r""to PLARK""\n""\r\r\r\r\r\r\r\r\r")
        step_1_info.resize(300,80)
        step_1_info.move(150,565)
        step_1_info.setStyleSheet("QLabel { font-weight: 700; font-size: 20px; font-family: Roboto; font-style: normal; color: #0E7470; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )
        step_1_extend = QLabel(self)
        step_1_extend.setText("Step 1")
        step_1_extend.move(220,620)
        step_1_extend.resize(150,25)
       # step_1_extend.setAlignment(QtCore.Qt.AlignLeft)
        step_1_extend.setStyleSheet("QLabel { font-weight: 400; font-size: 20px; font-family: Roboto; font-style: normal; color: #0E7470; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )


    def step1(self):
        step_1 = QLabel(self)
        step_1.pixmap = QPixmap('Images/Waste management-rafiki 1.png')
        step_1.setPixmap(step_1.pixmap)
        step_1.resize(step_1.pixmap.width(),step_1.pixmap.height())
        step_1.move(50,160)   # Subjected to change for monitor size

    def step_2(self):
        step_2_info = QLabel(self)
        step_2_info.setText("Our AI will sort""\n""\r\r\r""your plastic""\n""\r\r\r\r\r\r\r\r\r")
        step_2_info.move(620,565)
        step_2_info.resize(300,80)
        step_2_info.setStyleSheet("QLabel { font-weight: 700; font-size: 20px; font-family: Roboto; font-style: normal; color: #0E7470; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )
        step_2_extend = QLabel(self)
        step_2_extend.setText("Step 2")
        step_2_extend.move(670,620)
        step_2_extend.resize(150,25)
       # step_2_extend.setAlignment(QtCore.Qt.AlignCenter)
        step_2_extend.setStyleSheet("QLabel { font-weight: 400; font-size: 20px; font-family: Roboto; font-style: normal; color: #0E7470; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )

    def step2(self):
        step_2 = QLabel(self)
        step_2.pixmap = QPixmap('Images/Waste management-amico 1.png')
        step_2.setPixmap(step_2.pixmap)
        step_2.resize(step_2.pixmap.width(),step_2.pixmap.height())
        step_2.move(500,160)   # Subjected to change for monitor size


    def step_3(self):
        step_3_info = QLabel(self)
        step_3_info.setText("Earn point and redeem""\n""\r\r\r\r\r\r\r\r\r\r\r\r\r""rewards")
        step_3_info.move(1020,550)
        step_3_info.resize(300,80)
        step_3_info.setStyleSheet("QLabel { font-weight: 700; font-size: 20px; font-family: Roboto; font-style: normal; color: #0E7470; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )
        step_3_extend = QLabel(self)
        step_3_extend.setText("Step 3")
        step_3_extend.move(1113,620)
        step_3_extend.resize(150,25)
       # step_2_extend.setAlignment(QtCore.Qt.AlignCenter)
        step_3_extend.setStyleSheet("QLabel { font-weight: 400; font-size: 20px; font-family: Roboto; font-style: normal; color: #0E7470; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )

    def step3(self):
        step_1 = QLabel(self)
        step_1.pixmap = QPixmap('Images/Subscriber-bro 1.png')
        step_1.setPixmap(step_1.pixmap)
        step_1.resize(step_1.pixmap.width(),step_1.pixmap.height())
        step_1.move(950,160)   # Subjected to change for monitor size

    def add_manually(self):
        self.add_manual = QMainWindow()
        self.setWindowFlag(Qt.FramelessWindowHint)
       # self.add_manual.setGeometry(0, 0, 1920, 1080)
        self.add_manual = QLabel(self)
        self.add_manual.setText("Please input your mobile number")
        self.add_manual.setStyleSheet("QLabel {font-weight: 900; font-size: 60px; font-family: Roboto; font-style: normal; color: #0E7470; }" )
      #  self.add_manual.move(440,300)
      #  self.add_manual.resize(1000,80)
        self.add_manual.setWindowIcon(QIcon("Images/trashcash.jpg"))
        self.num_input()
        self.num_btn()
       # self.add_manual.showMaximized()

    def num_input(self):
        num = QLineEdit(self)
        num.setMaxLength(4)
        num.setAlignment(Qt.AlignCenter)
        num.setFont(QFont("Roboto",50))
        num.move(440,400)
        num.resize(1000,100)
        num.setInputMask('09999999999')
        num.setStyleSheet("QLineEdit { background-color: white; border-radius: 20px; }" )

    def num_btn(self):
        num_button = QPushButton("Next",self)
        num_button.setStyleSheet("QPushButton { font-size: 40px; background-color: #0E7470; font-family: Roboto;font-weight: 900; font-style: normal; color: white;  border-radius: 20px; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )
        num_button.setGeometry(440, 200, 1000, 100)

    def start_btn(self):
        start = start_button = QPushButton("Start", self)
        start_button.setGeometry(0, 670, 1500, 60)
        start.setStyleSheet("QPushButton:pressed { background-color: #0ef5a0 ; color:  #0E7470;  }" "QPushButton { background-color: #0E7470; font-size: 40px;   border-radius: 0px; color: white;}")
        start.clicked.connect(self.clickedDeposit)

    #def detection(self):
     #   self.detection = plastic_detection.main()
      #  detect = QLabel(self)
       # detect.setText(extract)

    '''def clickDetection(self):
        
        exec(open('plastic_detection.py').read())
       #detection = plastic_detection.main()
        extracts = extract.main()
        extracts = QLabel(self)
        extract.setText("")
'''
    def clickedDeposit(self):

        self._DepositWin = DepositWin.DepositWindow()
        self._DepositWin.show()
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
    ex = LandingWindow()
    sys.exit(app.exec_())
