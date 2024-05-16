import sys
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QLineEdit,QApplication,QHBoxLayout,QLabel,QMainWindow,QPushButton,QStackedLayout,QVBoxLayout,QWidget,QListWidget,QPlainTextEdit)
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from PIL import Image

from datetime import date, time, datetime
# import modules
import qrcode

import main

class QRWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowTitle("QR")
        self.setStyleSheet("background-color : #FFFAF3")
        self.help_btn()
        self.welcome_to_plark()
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
        
    

    def review_transaction(self):
        # taking image which user wants
        # in the QR code center
        Logo_link = r'Images\trashcash_logo.png'
        
        logo = Image.open(Logo_link)
        
        # taking base width
        basewidth = 100
        
        # adjust image size
        wpercent = (basewidth/float(logo.size[0]))
        hsize = int((float(logo.size[1])*float(wpercent)))
        logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
        QRcode = qrcode.QRCode(
            error_correction=qrcode.constants.ERROR_CORRECT_H
        )
        
        # taking url or text
        today = datetime.now() 
        qr_name = str(today.year)+str(today.month)+str(today.day)+str(today.hour)+str(today.minute)+str(today.second)+'.png'

        QRText = 'Q'+str(today.year)+str(today.month)+str(today.day)+str(today.hour)+str(today.minute)+str(today.second)
        
        # adding URL or text to QRcode
        QRcode.add_data(QRText)
        
        # generating QR code
        QRcode.make()
        
        # taking color name from user
        QRcolor = 'Green'
        
        # adding color to QR code
        QRimg = QRcode.make_image(
            fill_color=QRcolor, back_color="white").convert('RGB')
        
        # set size of QR code
        pos = ((QRimg.size[0] - logo.size[0]) // 2,
            (QRimg.size[1] - logo.size[1]) // 2)
        QRimg.paste(logo, pos)
        
        # save the QR code generated
        QRimg.save(r'Images/'+qr_name)
        
        #print('QR code generated!')
     
        self.QRlabel = QLabel(self)
        self.QRpixmap = QPixmap(r'Images/'+qr_name)
        self.QRlabel.setPixmap(self.QRpixmap)
        self.QRlabel.resize(330,330)
        self.QRlabel.move(1000,160)
        #self.QRlabel.show()

        self.QRlabelText = QLabel(QRText, self)
        self.QRlabelText.move(1100,160+330+30)

    def next_btn(self):
        next = next_button = QPushButton("Next", self)
        next_button.setGeometry(0, 670, 1500, 60)
        next.setStyleSheet("QPushButton:pressed { background-color: #0ef5a0 ; color:  #0E7470;  }" "QPushButton { background-color: #0E7470; font-size: 40px;   border-radius: 0px; color: white;}")
        #next.clicked.connect(self.clickedQR)

    def clickedLogout(self):
        self._LoginWin = main.Login()
        self._LoginWin.show()
        self.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = QRWindow()
    sys.exit(app.exec_())