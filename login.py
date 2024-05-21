import sys
import re
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox, QHBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
import sqlite3


import ultralytics
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


sys.path.insert(1,'windows/Registration')
import registration

sys.path.insert(2,'windows/Account')
import user_account

class Login(QMainWindow):
    def __init__(self, labels):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowTitle("Login")
        self.setWindowIcon(QIcon("Images/bintech logo.png"))
        self.setStyleSheet("background-color : #FFFAF3")

        self.labels = labels
    
        layout = QHBoxLayout()

        greeting= QLabel(self)
        greeting.setText("Hello There!")
        greeting.move(300,150)
        greeting.resize(900,100)
        greeting.setStyleSheet("QLabel {  font-size: 90px; font-family: Roboto;font-weight: 900; font-style: normal; color:  #699913; }" "QPushButton:pressed { background-color: #0ef5a0 ;  }" )
        layout.addWidget(greeting)

        self.email = QLineEdit(self)
        self.email.releaseKeyboard()
        self.email.setPlaceholderText("Email")
        self.email.move(300,300)
        self.email.resize(600,100)
        self.email.setStyleSheet("QLineEdit {  line-height: 42px; background-color: #FFFFFF; font-weight: 400; font-size: 20px; font-family: Roboto; font-style: normal; color: #979797; border-radius: 20px; padding-left: 24px; }" )

        self.password= QLineEdit(self)
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

    def clicked_Registration(self):
        self._registration = registration.Register(self.labels)
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
            # Connect to SQLite database
            conn = sqlite3.connect('bintech.db')
            cursor = conn.cursor()

            # Execute query to verify user credentials
            cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (user_email, user_password))
            user = cursor.fetchone()

            # Close cursor and connection
            cursor.close()
            conn.close()
            
            if user:
                username = user[2]
                self._user_account = user_account.User_Account(username, self.labels)
                self.hide()
                self._user_account.show()
            else:
                QMessageBox.warning(self, 'Error', 'Incorrect email or password!')
                self.email.clear()
                self.password.clear()

        except sqlite3.Error as e:
            QMessageBox.critical(self, 'Error', f'Failed to connect to database. Error: {str(e)}')

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)

    model = YOLO('best 2.pt', task='detect')
   
    box_annotator = sv.BoxAnnotator(
        thickness=2,                                                                      
        text_thickness=2,
        text_scale=1
    )
    
    if cap.isOpened():
        success, img = cap.read()
        print(success)

        if success:
            success, frame = cap.read()
            frame = cv2.resize(frame, (320,320),interpolation=cv2.INTER_LINEAR)
    
            #pprint(dir(model(frame)[0]))
            result = model(frame,max_det=1)[0]
            detections=sv.Detections.from_yolov8(result)
            labels = [
                f"{model.model.names[class_id]} {confidence:0.2f}"
                for _, confidence, class_id, _
                in detections
                ]

            frame = box_annotator.annotate(scene=frame, detections=detections, labels = labels)
            #cv2.imshow("plastic detection", frame)

            # if labels:
            #     time.sleep(0.5)
            #     extract = " ".join(re.findall("[a-zA-Z]+", str(labels[0])))
            #     var_data = extract
            #     print(var_data)
                

            app = QApplication(sys.argv)
            ex = Login(labels)
            sys.exit(app.exec_())
            # while True:                                                                                             
            #     
            #     if labels:
            #         time.sleep(0.5)
            #         extract = " ".join(re.findall("[a-zA-Z]+", str(labels[0])))
            #         var_data = extract
            #         #print(var_data)
            #         print(get_data())
                    
            #     else:
            #         print("No detections")
            #     if (cv2.waitKey(30) == 27):
            #         break	
        else:
            print("cannot capture frames")
        
    else:
        print("cannot open camera")
    
    cap.release()
    cv2.destroyAllWindows()
