import sys
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QMessageBox, QLineEdit,QApplication,QHBoxLayout,QLabel,QMainWindow,QPushButton,QStackedLayout,QVBoxLayout,QWidget,QListWidget,QPlainTextEdit)
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import sqlite3

sys.path.insert(1,'windows/Account')
import user_account

class User_Dashboard_Window(QMainWindow):
    def __init__(self, user_name):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowTitle("User Dashboard")
        self.setWindowIcon(QIcon("Images/bintech logo.png"))
        self.setStyleSheet("background-color : #FFFAF3")
        self.user_name = user_name
        
        layout = QHBoxLayout()
        
        greeting = QLabel(self)
        greeting.setText("My Dashboard") 
        greeting.move(300, 150)
        greeting.resize(900, 100)
        greeting.setStyleSheet("QLabel {font-size: 80px; font-family: Roboto;font-weight: 900; font-style: normal; color:  #699913; }" )
        layout.addWidget(greeting)

        self.plastic_type()
        self.PET_plastic_type()
        self.HDPE_plastic_type()
        self.PP_plastic_type()
        self.OTHER_plastic_type()
        self.back_btn()
        

        self.showFullScreen()
        
    def back_btn(self):
        back_button = QPushButton("BACK", self)
        back_button.setGeometry(300, 720, 600, 100)
        back_button.setStyleSheet("QPushButton { font-size: 40px; background-color: #699913; font-family: Roboto;font-weight: 900; font-style: normal; color: white;  border-radius: 20px; }" "QPushButton:pressed { background-color: #0E7470; color: #FFFFFF;  }" )
        back_button.clicked.connect(self.clicked_Back)  # Connect to clicked_Back without passing any arguments


    def plastic_type(self):
        Plastic_Type = QLabel(self)
        Plastic_Type.setText("Plastic Type")
        Plastic_Type.move(300,300)
        Plastic_Type.resize(300,50)
        Plastic_Type.setStyleSheet("QLabel { font-size: 40px; font-family: Roboto;font-weight: 1000; font-style: normal; color:  #699913; }" )

    def PET_plastic_type(self):
        PET_Plastic_Type = QLabel(self)
        PET_Plastic_Type.setText("PET")
        PET_Plastic_Type.move(300,375)
        PET_Plastic_Type.resize(300,50)
        PET_Plastic_Type.setStyleSheet("QLabel { font-size: 40px; font-family: Roboto;font-weight: 900; font-style: normal; color:  #699913; }" )

    def HDPE_plastic_type(self):
        HDPE_Plastic_Type = QLabel(self)
        HDPE_Plastic_Type.setText("HDPE")
        HDPE_Plastic_Type.move(300,450)
        HDPE_Plastic_Type.resize(300,50)
        HDPE_Plastic_Type.setStyleSheet("QLabel { font-size: 40px; font-family: Roboto;font-weight: 900; font-style: normal; color:  #699913; }" )

    def PP_plastic_type(self):
        HDPE_Plastic_Type = QLabel(self)
        HDPE_Plastic_Type.setText("PP")
        HDPE_Plastic_Type.move(300,525)
        HDPE_Plastic_Type.resize(300,50)
        HDPE_Plastic_Type.setStyleSheet("QLabel { font-size: 40px; font-family: Roboto;font-weight: 900; font-style: normal; color:  #699913; }" )

    def OTHER_plastic_type(self):
        HDPE_Plastic_Type = QLabel(self)
        HDPE_Plastic_Type.setText("OTHER")
        HDPE_Plastic_Type.move(300,600)
        HDPE_Plastic_Type.resize(300,50)
        HDPE_Plastic_Type.setStyleSheet("QLabel { font-size: 40px; font-family: Roboto;font-weight: 900; font-style: normal; color:  #699913; }" )

    def username_retrieve(self, email):
        try:
            # Connect to SQLite database
            conn = sqlite3.connect('bintech.db')
            cursor = conn.cursor()

            # Execute query to verify user credentials
            cursor.execute("SELECT * FROM users WHERE email = ?", (email))
            user = cursor.fetchone()


            # Close cursor and connection
            cursor.close()
            conn.close()
           
            if user:
                username = user[2]
                self._user_account = user_account(username)  # Pass user's email to the constructor
                self.hide()
                self._user_account.show()
            else:
                QMessageBox.warning(self, 'Error', 'Incorrect email or password!')
                # Clear email and password fields if you have them

        except sqlite3.Error as e:
            QMessageBox.critical(self, 'Error', f'Failed to connect to database. Error: {str(e)}')

    def clicked_Back(self):
        self._user_account = user_account.User_Account(self.user_name)
        self.hide()
        self._user_account.show()
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = User_Dashboard_Window()
    sys.exit(app.exec_())