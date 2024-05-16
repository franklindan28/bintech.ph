import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QMessageBox, QHBoxLayout
from PyQt5.QtGui import QIcon, QPixmap

import sqlite3

import login

sys.path.insert(3,'windows/User_Dashboard')
import user_dashboard

sys.path.insert(2,'windows/Landing')
import LandingWin

sys.path.insert(1,'windows/Registration')
import registration

sys.path.insert(4,'windows/Drop')
import Drop

class User_Account(QMainWindow):
    def __init__(self, user_name, labels):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowTitle("User Account")
        self.setWindowIcon(QIcon("Images/bintech logo.png"))
        self.setStyleSheet("background-color : #FFFAF3")
        self.user_name = user_name
        self.labels = labels
        
        layout = QHBoxLayout()

        greeting = QLabel(self)
        greeting.setText(f"Hello There, {user_name}!")  # Display user's email
        greeting.move(300, 150)
        greeting.resize(900, 100)
        greeting.setStyleSheet("QLabel {  font-size: 80px; font-family: Roboto;font-weight: 900; font-style: normal; color:  #699913; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )
        layout.addWidget(greeting)
       
        profile_btn = QPushButton("View Profile", self)
        profile_btn.setStyleSheet("QPushButton { font-size: 40px; background-color:  #699913; font-family: Roboto;font-weight: 900; font-style: normal; color: white;  border-radius: 20px; }" "QPushButton:pressed { background-color: #0E7470; color:  #FFFFFF;  }" )
        profile_btn.setGeometry(300, 360, 600, 150)
        profile_btn.clicked.connect(self.clicked_User_Dashboard)

        start_btn = QPushButton("Start Now", self)
        start_btn.setStyleSheet("QPushButton { font-size: 40px; background-color:  #699913; font-family: Roboto;font-weight: 900; font-style: normal; color: white;  border-radius: 20px; }" "QPushButton:pressed { background-color: #0E7470; color:  #FFFFFF;  }" )
        start_btn.setGeometry(300, 580, 600, 150)
        start_btn.clicked.connect(self.clicked_Start)

        logout_btn = QPushButton("Logout", self)
        logout_btn.setStyleSheet("QPushButton { font-size: 40px; background-color:  #699913; font-family: Roboto;font-weight: 900; font-style: normal; color: white;  border-radius: 20px; }" "QPushButton:pressed { background-color: #0E7470; color:  #FFFFFF;  }" )
        logout_btn.setGeometry(300, 800, 600, 150)
        logout_btn.clicked.connect(self.clicked_logout)

        logo = QLabel(self)
        logo.pixmap = QPixmap('Images/BINTECH LOGO.png')
        logo.setPixmap(logo.pixmap)
        logo.resize(logo.pixmap.width(), logo.pixmap.height())
        logo.move(1100, 320) 

        self.showFullScreen()

    def clicked_Start(self):
        self._Drop = Drop.Drop(self.user_name, self.labels)
        self.hide()
        self._Drop.show()

    
    def clicked_logout(self):
        reply = QMessageBox.question(self, 'Logout', 'Are you sure you want to logout?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self._login = login.Login()
            self.close()
            self._login.show()

    def clicked_User_Dashboard(self):
        self._user_dashboard = user_dashboard.User_Dashboard_Window(self.user_name, self.labels)
        self.hide()
        self._user_dashboard.show()   

    def username_retrieve(self, email):
        try:
            # Connect to SQLite database
            conn = sqlite3.connect('bintech.db')
            cursor = conn.cursor()

            # Execute query to verify user credentials
            cursor.execute("SELECT * FROM users WHERE email = ? AND username", (email, username))
            user = cursor.fetchone()

            # Close cursor and connection
            cursor.close()
            conn.close()

            if user:
                username = user[2]
                self._user_account = User_Account(username)  # Pass user's email to the constructor
                self.hide()
                self._user_account.show()

            else:
                QMessageBox.warning(self, 'Error', 'Incorrect email or password!')
                # Clear email and password fields if you have them

        except sqlite3.Error as e:
            QMessageBox.critical(self, 'Error', f'Failed to connect to database. Error: {str(e)}')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = User_Account()  # Pass the user's email here
    sys.exit(app.exec_())
