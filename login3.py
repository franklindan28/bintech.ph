import sys
import re
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
import mysql.connector


sys.path.insert(2,'windows/Account')
import user_account

sys.path.insert(1,'windows/Registration')
import registration



class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowTitle("Login")
        self.setWindowIcon(QIcon("Images/bintech logo.png"))
        self.setStyleSheet("background-color : #FFFAF3")
    
        layout = QHBoxLayout()

        greeting= QLabel(self)
        greeting.setText("Hello There!")
        greeting.move(300,150)
        greeting.resize(900,100)
        greeting.setStyleSheet("QLabel {  font-size: 90px; font-family: Roboto;font-weight: 900; font-style: normal; color:  #699913; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )
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

        log_btn = QPushButton("Login",self)
        log_btn.setStyleSheet("QPushButton { font-size: 40px; background-color:  #699913; font-family: Roboto;font-weight: 900; font-style: normal; color: white;  border-radius: 20px; }" "QPushButton:pressed { background-color: #0E7470; color:  #FFFFFF;  }" )
        log_btn.setGeometry(300, 600, 600, 100)
        log_btn.clicked.connect(self.clicked_Login)

        reg_btn = QPushButton("Register",self) 
        reg_btn.setStyleSheet("QPushButton { font-size: 40px; background-color: #699913; font-family: Roboto;font-weight: 900; font-style: normal; color: white;  border-radius: 20px; }" "QPushButton:pressed { background-color: #0E7470; color: #FFFFFF;  }" )
        reg_btn.setGeometry(300, 720, 600, 100)
        reg_btn.clicked.connect(self.clicked_Registration)

        logo = QLabel(self)
        logo.pixmap = QPixmap('Images/BINTECH LOGO.png')
        logo.setPixmap(logo.pixmap)
        logo.resize(logo.pixmap.width(),logo.pixmap.height())
        logo.move(1100,320) 
 


        self.showFullScreen()



    #def add_window(self):
    #    self.Window2.showMaximized()
    #    self.close()
    def clicked_Registration(self):
        self._registration = registration.Register()
        self.hide()
        self._registration.show()
        
    def clicked_Login(self):
        user_email = self.email.text()
        user_password = self.password.text()

        if not user_email or not user_password:
            QMessageBox.warning(self, 'Error', 'Please fill out all fields!')
            self.email.clear()
            self.password.clear()
            return
        
        if not re.match(r"[^@]+@[^@]+\.[^@]+", user_email):
            QMessageBox.warning(self, 'Error', 'Please enter a valid email address!')
            self.email.clear()
            self.password.clear()
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

            # Execute query to verify user credentials
            cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (user_email, user_password))
            user = cursor.fetchone()

            # Close cursor and connection
            cursor.close()
            conn.close()

            if user:
                self._user_account = user_account.User_Account()
                self.hide()
                self._user_account.show()
            else:
                QMessageBox.warning(self, 'Error', 'Incorrect email or password!')
                self.email.clear()
                self.password.clear()

        except mysql.connector.Error as e:
            QMessageBox.critical(self, 'Error', f'Failed to connect to database. Error: {str(e)}')
    

        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    #app.setStyleSheet(stylesheet)
    ex = Login()
    sys.exit(app.exec_())
