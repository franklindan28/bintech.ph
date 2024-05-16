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



class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowTitle("Login")
        self.setWindowIcon(QIcon("Images/bintech logo.png"))
        self.setStyleSheet("background-color : #FFFAF3")
    
        layout = QHBoxLayout()

        greeting= QLabel(self)
        greeting.setText("Hello There!, Please Register")
        greeting.move(300,150)
        greeting.resize(900,100)
        greeting.setStyleSheet("QLabel {  font-size: 50px; font-family: Roboto;font-weight: 900; font-style: normal; color:  #699913; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )
        layout.addWidget(greeting)

        self.email = QLineEdit(self)
        self.email.setPlaceholderText("Email")
        self.email.move(300,300)
        self.email.resize(600,100)
        self.email.setStyleSheet("QLineEdit {  line-height: 42px; background-color: #FFFFFF; font-weight: 400; font-size: 20px; font-family: Roboto; font-style: normal; color: #979797; border-radius: 20px; padding-left: 24px; }" )

        self.password= QtWidgets.QLineEdit(self)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setPlaceholderText("Password")
        self.password.move(300,425)
        self.password.resize(600,100)
        self.password.setStyleSheet(" QLineEdit { line-height: 42px; background-color: #FFFFFF; font-weight: 400; font-size: 20px; font-family: Roboto; font-style: normal; color: #979797; border-radius: 20px; position: absolute; padding-left: 24px;}" )

        self.confirm_password= QtWidgets.QLineEdit(self)
        self.confirm_password.setEchoMode(QLineEdit.Password)
        self.confirm_password.setPlaceholderText("Confirm Password")
        self.confirm_password.move(300,550)
        self.confirm_password.resize(600,100)
        self.confirm_password.setStyleSheet(" QLineEdit { line-height: 42px; background-color: #FFFFFF; font-weight: 400; font-size: 20px; font-family: Roboto; font-style: normal; color: #979797; border-radius: 20px; position: absolute; padding-left: 24px;}" )

        reg_btn = QPushButton("Register",self)
        reg_btn.setStyleSheet("QPushButton { font-size: 40px; background-color:  #699913; font-family: Roboto;font-weight: 900; font-style: normal; color: white;  border-radius: 20px; }" "QPushButton:pressed { background-color: #0E7470; color:  #FFFFFF;  }" )
        reg_btn.setGeometry(300, 700, 600, 100)
        reg_btn.clicked.connect(self.register)

        back_btn = QPushButton("Cancel",self)
        back_btn.setStyleSheet("QPushButton { font-size: 40px; background-color:  #699913; font-family: Roboto;font-weight: 900; font-style: normal; color: white;  border-radius: 20px; }" "QPushButton:pressed { background-color: #0E7470; color:  #FFFFFF;  }" )
        back_btn.setGeometry(300, 820, 600, 100)
        back_btn.clicked.connect(self.clicked_back)


        logo = QLabel(self)
        logo.pixmap = QPixmap('Images/BINTECH LOGO.png')
        logo.setPixmap(logo.pixmap)
        logo.resize(logo.pixmap.width(),logo.pixmap.height())
        logo.move(1100,320) 


        self.showFullScreen()



    #def add_window(self):
    #    self.Window2.showMaximized()
    #    self.close()
    def clicked_back(self):    
        self._login = login.Login()
        self.close()
        self._login.show()

    def clickedLanding(self):
        self._LandingWin = LandingWin.LandingWindow()
        self.hide()
        self._LandingWin.show()
    
    def register(self):
        user_email = self.email.text()
        user_password = self.password.text()
        user_confirm_password = self.confirm_password.text()

        
        if not user_email or not user_password or not user_confirm_password:
            QMessageBox.warning(self, 'Error', 'Please fill out all fields!')
            self.email.clear()
            self.password.clear()
            self.confirm_password.clear()
            return
        
        if not re.match(r"[^@]+@[^@]+\.[^@]+", user_email):
            QMessageBox.warning(self, 'Error', 'Please enter a valid email address!')
            self.email.clear()
            self.password.clear()
            self.confirm_password.clear()
            return
        
        if user_password != user_confirm_password:
            QMessageBox.warning(self, 'Error', 'Passwords do not match!')
            self.email.clear()
            self.password.clear()
            self.confirm_password.clear()
            return
    


        try:
            # Connect to MySQL database
            conn = mysql.connector.connect(
                host='127.0.0.1',
                user='qwerty',
                password='password123',
                database='plark'
            )

            # Create cursor
            cursor = conn.cursor()

            # Execute query to insert user data into the database
            cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (user_email, user_password))

            cursor.execute("SELECT * FROM users WHERE email = %s", (user_email,))
            existing_user = cursor.fetchone()
            if existing_user:
                QMessageBox.warning(self, 'Error', 'Email already registered!')
                self.email.clear()
                self.password.clear()
                self.confirm_password.clear()
                return
            conn.commit()

            # Close cursor and connection
            cursor.close()
            conn.close()

            QMessageBox.information(self, 'Success', 'Registration successful!')

        except mysql.connector.Error as e:
            QMessageBox.critical(self, 'Error', f'Failed to connect to database. Error: {str(e)}')
        
        self.hide()
        self._login = login.Login()
        self._login.show()
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Register()
    sys.exit(app.exec_())
