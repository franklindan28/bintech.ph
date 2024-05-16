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

sys.path.insert(4,'windows/Account')
import user_account

sys.path.insert(5,'windows/Drop')
import Drop


class Add_on(QMainWindow):
    def __init__(self, username, labels):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowTitle("Add On")
        self.setWindowIcon(QIcon("Images/bintech logo.png"))
        self.setStyleSheet("background-color : #FFFAF3")

        self.user_name = username
        self.labels = labels
    
        layout = QHBoxLayout()

        add_btn = QPushButton("ADD PLASTIC", self)
        add_btn.setStyleSheet("QPushButton { font-size: 40px; background-color:  #699913; font-family: Roboto;font-weight: 900; font-style: normal; color: white;  border-radius: 20px; }" "QPushButton:pressed { background-color: #0E7470; color:  #FFFFFF;  }" )
        add_btn.setGeometry(530, 580, 900, 150)
        add_btn.clicked.connect(self.clicked_add)
        
        done_btn = QPushButton("DONE", self)
        done_btn.setStyleSheet("QPushButton { font-size: 40px; background-color:  #699913; font-family: Roboto;font-weight: 900; font-style: normal; color: white;  border-radius: 20px; }" "QPushButton:pressed { background-color: #0E7470; color:  #FFFFFF;  }" )
        done_btn.setGeometry(530, 880, 900, 150)
        done_btn.clicked.connect(self.clicked_done)

        self.showFullScreen()

   
    def clicked_add(self):
            self._drop = Drop.Drop(self.user_name, self.labels)  # Pass user's email to the constructor
            self.hide()
            self._drop.show()
    
    def clicked_done(self):
            self._user_account = user_account.User_Account(self.user_name, self.labels)  # Pass user's email to the constructor
            self.hide()
            self._user_account.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Add_on() 
    sys.exit(app.exec_())
