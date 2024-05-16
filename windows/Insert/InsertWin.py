import sys
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QMessageBox, QLineEdit,QApplication,QHBoxLayout,QLabel,QMainWindow,QPushButton,QStackedLayout,QVBoxLayout,QWidget,QListWidget,QPlainTextEdit)
from PyQt5.QtGui import *
from PyQt5 import QtWidgets

import main
sys.path.insert(1,'windows/Transaction')
import TransactionWin

class InsertWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowTitle("Insert")
        self.setStyleSheet("background-color : #FFFAF3")
        self.help_btn()
        self.welcome_to_plark()
        self.logout_btn()
        self.additional_info()
        self.step_2()
        self.step2()
        self.done_btn()
        #self.Window6 = NewWindow5()

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

    def step_2(self):
        step_2_info = QLabel(self)
        step_2_info.setText("Our AI is currently sorting your plastic waste.")
        step_2_info.move(465,565)
        step_2_info.resize(600,80)
        step_2_info.setStyleSheet("QLabel { font-weight: 700; font-size: 20px; font-family: Roboto; font-style: normal; color: #0E7470; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )
        step_2_info1 = QLabel(self)
        step_2_info1.setText("Please wait...")
        step_2_info1.move(620,620)
        step_2_info1.resize(600,20)
        step_2_info1.setStyleSheet("QLabel { font-weight: 700; font-size: 20px; font-family: Roboto; font-style: normal; color: #0E7470; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )

    def step2(self):
        step_2 = QLabel(self)
        step_2.pixmap = QPixmap('Images/Waste management-amico 1.png')
        step_2.setPixmap(step_2.pixmap)
        step_2.resize(step_2.pixmap.width(),step_2.pixmap.height())
        step_2.move(500,160)   # Subjected to change for monitor size


    def done_btn(self):
        done = done_button = QPushButton("Done", self)
        done_button.setGeometry(0, 670, 1500, 60)
        done.setStyleSheet("QPushButton:pressed { background-color: #0ef5a0 ; color:  #0E7470;  }" "QPushButton { background-color: #0E7470; font-size: 40px;   border-radius: 0px; color: white;}")
        done.clicked.connect(self.clickedTransaction)

    def clickedTransaction(self):
        self._TransactionWin = TransactionWin.TransactionWindow()
        self._TransactionWin.show()
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
    ex = InsertWindow()
    sys.exit(app.exec_())