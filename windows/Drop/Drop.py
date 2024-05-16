import sys
from PyQt5.QtCore import Qt, QTimer
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

sys.path.insert(5,'windows/Add_On')
import Add_On

sys.path.insert(6,'windows/Loading_Process')
import Loading_Process

class Drop(QMainWindow):
    def __init__(self, username, labels):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowTitle("Drop")
        self.setWindowIcon(QIcon("Images/bintech logo.png"))
        self.setStyleSheet("background-color : #FFFAF3")
        self.user_name = username
        self.labels = labels

        layout = QHBoxLayout()

        greeting = QLabel(self)
        greeting.setText(f"Please Scan your plastic in the orange dot")  # Display user's email
        greeting.move(450, 150)
        greeting.resize(1300, 100)
        greeting.setStyleSheet("QLabel {  font-size: 50px; font-family : Roboto;font-weight: 900; font-style: normal; color:  #699913; }" )
        layout.addWidget(greeting)
       
        cancel_btn = QPushButton("CANCEL", self)
        cancel_btn.setStyleSheet("QPushButton { font-size: 40px; background-color:  #699913; font-family: Roboto;font-weight: 900; font-style: normal; color: white;  border-radius: 20px; }" "QPushButton:pressed { background-color: #0E7470; color:  #FFFFFF;  }" )
        cancel_btn.setGeometry(530, 580, 900, 150)
        cancel_btn.clicked.connect(self.clicked_cancel)

        drop_indication = QLabel("DROP IT", self)
        drop_indication.setStyleSheet("QLabel { font-size: 40px; background-color:  #699913; font-family: Roboto;font-weight: 900; font-style: normal; color: white;  border-radius: 20px;}" )
        drop_indication.setGeometry(530, 360, 440, 150)
        drop_indication.setAlignment(Qt.AlignCenter)

        not_allowed_indication = QLabel("NOT ALLOWED", self)
        not_allowed_indication.setStyleSheet("QLabel { font-size: 40px; background-color:  #699913; font-family: Roboto;font-weight: 900; font-style: normal; color: white;  border-radius: 20px;}" )
        not_allowed_indication.setGeometry(980, 360, 440, 150)
        not_allowed_indication.setAlignment(Qt.AlignCenter)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.timerEvent)

        self.showFullScreen()

        # while True:                                                                                             
        #     if self.labels:
        #         time.sleep(0.5)
        #         extract = " ".join(re.findall("[a-zA-Z]+", str(self.labels[0])))
        #         var_data = extract
        #         print(var_data)

        #         #print(get_data())
        #     # else:
        #     #     print("No detections")
        #     if (cv2.waitKey(30) == 27):
        #         break

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
                self._user_account = user_account.User_Account(email)  # Pass user's email to the constructor
                self.hide()
                self._user_account.show()
            else:
                QMessageBox.warning(self, 'Error', 'Incorrect email or password!')
                # Clear email and password fields if you have them

        except sqlite3.Error as e:
            QMessageBox.critical(self, 'Error', f'Failed to connect to database. Error: {str(e)}')

    def clicked_cancel2(self):
        reply = QMessageBox.question(self, 'Cancel', 'Are you sure you want to cancel?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self._user_account = user_account.User_Account(self.user_name, self.labels) 
            self.hide()
            self._user_account.show()
            
    def clicked_cancel2(self):
            self._add_on = Add_On.Add_on(self.user_name, self.labels)  
            self.hide()
            self._add_on.show() 

    def clicked_cancel(self):
            self._loading_process = Loading_Process.Loading_Process(self.user_name, self.labels)  
            self.hide()
            self._loading_process.show() 
            self.timer.start(3000)
            self.timer.stop()   


    def timerEvent(self):
        print("Timer triggered!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Drop() 
    sys.exit(app.exec_())
