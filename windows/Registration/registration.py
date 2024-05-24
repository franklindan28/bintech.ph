import sys
import re
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox, QHBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
import sqlite3

import login

class Register(QMainWindow):
    def __init__(self, labels, ser, cap, success, model):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowTitle("Login")
        self.setWindowIcon(QIcon("Images/bintech logo.png"))
        self.setStyleSheet("background-color : #FFFAF3")

        self.labels = labels
        self.ser = ser
        self.cap = cap
        self.success = success
        self.model = model
    
        layout = QHBoxLayout()

        greeting= QLabel(self)
        greeting.setText("Hello There!, Please Register")
        greeting.move(300,30)
        greeting.resize(900,100)
        greeting.setStyleSheet("QLabel {  font-size: 50px; font-family: Roboto;font-weight: 900; font-style: normal; color:  #699913; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )
        layout.addWidget(greeting)

        self.email = QLineEdit(self)
        self.email.setPlaceholderText("Email")
        self.email.move(300,140)
        self.email.resize(600,90)
        self.email.setStyleSheet("QLineEdit {  line-height: 42px; background-color: #FFFFFF; font-weight: 400; font-size: 20px; font-family: Roboto; font-style: normal; color: #979797; border-radius: 20px; padding-left: 24px; }" )

        self.username = QLineEdit(self)
        self.username.setPlaceholderText("Username")
        self.username.move(300,250)
        self.username.resize(600,90)
        self.username.setStyleSheet("QLineEdit {  line-height: 42px; background-color: #FFFFFF; font-weight: 400; font-size: 20px; font-family: Roboto; font-style: normal; color: #979797; border-radius: 20px; padding-left: 24px; }" )
        
        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setPlaceholderText("Password")
        self.password.move(300,360)
        self.password.resize(600,90)
        self.password.setStyleSheet(" QLineEdit { line-height: 42px; background-color: #FFFFFF; font-weight: 400; font-size: 20px; font-family: Roboto; font-style: normal; color: #979797; border-radius: 20px; position: absolute; padding-left: 24px;}" )

        self.confirm_password = QLineEdit(self)
        self.confirm_password.setEchoMode(QLineEdit.Password)
        self.confirm_password.setPlaceholderText("Confirm Password")
        self.confirm_password.move(300,470)
        self.confirm_password.resize(600,90)
        self.confirm_password.setStyleSheet(" QLineEdit { line-height: 42px; background-color: #FFFFFF; font-weight: 400; font-size: 20px; font-family: Roboto; font-style: normal; color: #979797; border-radius: 20px; position: absolute; padding-left: 24px;}" )

        self.rfid = QLineEdit(self)
        self.rfid.setPlaceholderText("Card Code")
        self.rfid.move(300,580)
        self.rfid.resize(600,90)
        self.rfid.setStyleSheet(" QLineEdit { line-height: 42px; background-color: #FFFFFF; font-weight: 400; font-size: 20px; font-family: Roboto; font-style: normal; color: #979797; border-radius: 20px; position: absolute; padding-left: 24px;}" )

        reg_btn = QPushButton("Register",self)
        reg_btn.setStyleSheet("QPushButton { font-size: 40px; background-color:  #699913; font-family: Roboto;font-weight: 900; font-style: normal; color: white;  border-radius: 20px; }" "QPushButton:pressed { background-color: #0E7470; color:  #FFFFFF;  }" )
        reg_btn.setGeometry(300, 690, 600, 90)
        reg_btn.clicked.connect(self.register)

        back_btn = QPushButton("Cancel",self)
        back_btn.setStyleSheet("QPushButton { font-size: 40px; background-color:  #699913; font-family: Roboto;font-weight: 900; font-style: normal; color: white;  border-radius: 20px; }" "QPushButton:pressed { background-color: #0E7470; color:  #FFFFFF;  }" )
        back_btn.setGeometry(300, 800, 600, 90)
        back_btn.clicked.connect(self.clicked_back)

        logo = QLabel(self)
        logo.pixmap = QPixmap('Images/BINTECH LOGO.png')
        logo.setPixmap(logo.pixmap)
        logo.resize(logo.pixmap.width(),logo.pixmap.height())
        logo.move(1100,320) 

        self.showFullScreen()

    def clicked_back(self):    
        self._login = login.Login(self.labels, self.ser, self.cap, self.success, self.model)
        self.close()
        self._login.show()
    
    def register(self):
        user_email = self.email.text()
        user_name = self.username.text()
        user_password = self.password.text()
        user_confirm_password = self.confirm_password.text()
        user_rfid = self.rfid.text()
        
        if not user_email or not user_name or not user_password or not user_confirm_password or not user_rfid:
            QMessageBox.warning(self, 'Error', 'Please fill out all fields!')
            self.email.clear()
            self.username.clear()
            self.password.clear()
            self.confirm_password.clear()
            self.rfid.clear()
            return
        
        if not re.match(r"[^@]+@[^@]+\.[^@]+", user_email):
            QMessageBox.warning(self, 'Error', 'Please enter a valid email address!')
            self.email.clear()
            self.username.clear()
            self.password.clear()
            self.confirm_password.clear()
            self.rfid.clear()
            return
        
        if user_password != user_confirm_password:
            QMessageBox.warning(self, 'Error', 'Passwords do not match!')
            self.email.clear()
            self.username.clear()
            self.password.clear()
            self.confirm_password.clear()
            self.rfid.clear()
            return

        try:
            # Connect to SQLite database
            conn = sqlite3.connect('bintech.db')
            cursor = conn.cursor()

            cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    email TEXT UNIQUE,
                    username TEXT NOT NULL,
                    password INTEGER,
                    rfid TEXT UNIQUE
                 )''')

            # Execute query to insert user data into the database

            cursor.execute("SELECT * FROM users WHERE email = ? AND username = ?", (user_email, user_name))
            existing_user = cursor.fetchone()
            if existing_user:
                QMessageBox.warning(self, 'Error', 'Email or Username is already registered!')
                self.email.clear()
                self.username.clear()
                self.password.clear()
                self.confirm_password.clear()
                self.rfid.clear()
                return
            
            cursor.execute("INSERT INTO users (email, username, password, rfid) VALUES (?,?,?,?)", (user_email, user_name, user_password, user_rfid))
            conn.commit()

            # Close cursor and connection
            cursor.close()
            conn.close()

            QMessageBox.information(self, 'Success', 'Registration successful!')

        except sqlite3.Error as e:
            QMessageBox.critical(self, 'Error', f'Failed to connect to database. Error: {str(e)}')
        
        self.hide()
        self._login = login.Login(self.labels, self.ser, self.cap, self.success, self.model)
        self._login.show()
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Register()
    sys.exit(app.exec_())
