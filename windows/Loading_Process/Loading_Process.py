import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox, QHBoxLayout, QProgressBar
from PyQt5.QtGui import QIcon
import sqlite3

sys.path.insert(5,'windows/Add_On')
import Add_On


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

class Loading_Process(QMainWindow):
    def __init__(self, username, labels, ser, cap, success, model):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowTitle("Loading Process")
        self.setWindowIcon(QIcon("Images/bintech logo.png"))
        self.setStyleSheet("background-color : #FFFAF3")
        self.user_name = username
        self.labels = labels
        self.ser = ser
        self.cap = cap
        self.success = success
        self.model = model

        layout = QHBoxLayout()

        # OPEN THE DOOR
        self.sendToArduino("OPEN")

        self.resutlt = QLabel(self)
        self.resutlt.setText(f"RESULT: ...")  # Display user's email
        self.resutlt.move(700, 200)
        self.resutlt.resize(900, 100)
        self.resutlt.setStyleSheet("QLabel {  font-size: 80px; font-family: Roboto;font-weight: 900; font-style: normal; color:  #699913; }" )
        layout.addWidget(self.resutlt)

        greeting = QLabel(self)
        greeting.setText(f"Please Wait")  # Display user's email
        greeting.move(700, 400)
        greeting.resize(900, 100)
        greeting.setStyleSheet("QLabel {  font-size: 80px; font-family: Roboto;font-weight: 900; font-style: normal; color:  #699913; }" )
        layout.addWidget(greeting)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(500, 600, 900, 60)
       # self.progress_bar.setStyleSheet("QProgressBar{""border-radius: 10px;"  "QProgressBar::chunk {""background-color:   #699913;""border-radius: 10px;" )
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setStyleSheet("QProgressBar {"
                                        "border: 2px solid grey;"
                                        "border-radius: 10px;"  
                                        "background-color: #FFFFFF;"
                                        "}"
                                        "QProgressBar::chunk {"
                                        "background-color: #699913;"
                                        "border-radius: 10px;" 
                                        "}")   
        
        self.showFullScreen()
        # time.sleep(3)
        self.progress = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(1000)

    def update_progress(self):
          
        # self.progress += 1
        # self.progress_bar.setValue(self.progress)

        if self.labels:
            result_detect = []

            while(len(result_detect) != 10):
                self.success, frame = self.cap.read()
                frame = cv2.resize(frame, (320,320),interpolation=cv2.INTER_LINEAR)
        
                #pprint(dir(model(frame)[0]))
                result = self.model(frame,max_det=1)[0]
                detections=sv.Detections.from_yolov8(result)
                self.labels = [
                    f"{self.model.model.names[class_id]} {confidence:0.2f}"
                    for _, confidence, class_id, _
                    in detections
                    ]
                
                box_annotator = sv.BoxAnnotator(
                    thickness=2,                                                                      
                    text_thickness=2,
                    text_scale=1
                )

                if self.labels:
                    frame = box_annotator.annotate(scene=frame, detections=detections, labels = self.labels)
                    print(f"FRAME: {frame})")
                    print(f"self.labels: {self.labels})")
                    extract = " ".join(re.findall("[a-zA-Z]+", str(self.labels[0])))
                    var_data = extract
                    
                    result_detect.append(var_data)

                else:
                    print("No detections")

                time.sleep(1)

            print(f"result_detect: {result_detect}")
            # print(f"result_detect: {self.find_most_frequent_max_string(result_detect)}")

            result_data = self.find_most_frequent_max_string(result_detect)
            print(f"final_result_detect: {result_detect}")

            # CLOSE THE DOOR
            self.sendToArduino("CLOSE")
            self.resutlt.setText(f"RESULT: {result_data}")

            self.sendToArduino(result_data)

            conn = sqlite3.connect('bintech.db')
            cursor = conn.cursor()

            cursor.execute('''CREATE TABLE IF NOT EXISTS plastics (
                    id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    plastic_type TEXT NOT NULL,
                    date_created datetime default current_timestamp,
                    FOREIGN KEY (user_id) 
                        REFERENCES users (id) 
                            ON DELETE CASCADE 
                            ON UPDATE NO ACTION                    
                 )''')
            
            cursor.execute("SELECT * FROM users WHERE username = ?", (self.user_name,))
            user = cursor.fetchone()
            # print(user)
            id = user[0]

            cursor.execute("INSERT INTO plastics (user_id, plastic_type) VALUES (?,?)", (id, result_data))
            conn.commit()

            # Close cursor and connection
            cursor.close()
            conn.close()
            
            timeLoading = 20

            for i in range(timeLoading):
                time.sleep(1)
                self.progress = (i/timeLoading) * 100
                self.progress = int(self.progress)
                self.progress_bar.setValue(self.progress)

            self.timer.stop()
            # QTimer.singleShot(2000, self.reset_loading)  # Reset loading after 2 seconds
            # QTimer.singleShot(2000, self.add)  # Reset loading after 2 seconds
            self.add()
        else:
            print("No detections")
            self.progress += 2
            self.progress_bar.setValue(self.progress)
        #         #print(get_data())
        #     # else:
        #     #     print("No detections")
        #     if (cv2.waitKey(30) == 27):
        #         break


        # if self.progress >= 100:
        #     self.timer.stop()
        #     QTimer.singleShot(2000, self.reset_loading)  # Reset loading after 2 seconds
        #     QTimer.singleShot(2000, self.add)  # Reset loading after 2 seconds
        #     self.showFullScreen()

    def reset_loading(self):
        self.progress = 0
        self.progress_bar.setValue(0)
        self.timer.start(50)
        

    def add(self):
        self._add_on = Add_On.Add_on(self.user_name, self.labels, self.ser, self.cap, self.success, self.model)  
        self.hide()
        self._add_on.show() 

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
                self._Loading_Process = Loading_Process(email)  # Pass user's email to the constructor
                self.hide()
                self._user_account.show()
            else:
                QMessageBox.warning(self, 'Error', 'Incorrect email or password!')
                # Clear email and password fields if you have them

        except sqlite3.Error as e:
            QMessageBox.critical(self, 'Error', f'Failed to connect to database. Error: {str(e)}')

    def sendToArduino(self, detectionResult):
        try:
            # while True:
            #     user_input = input("Enter Command (start): ").upper()
            #     ser.write(user_input.encode())
            #     print(f'Sent command: {user_input}')
            detectionResult = detectionResult.upper()
            self.ser.write(detectionResult.encode())
            print(f'Sent command: {detectionResult}')
            
        except KeyboardInterrupt:
            print("Terminated! Restart the System!")
            self.ser.close()

    def find_most_frequent_max_string(arr):
        if not arr:
            return None

        # Step 1: Count each string in the array using a dictionary
        count = {}
        for string in arr:
            if string in count:
                count[string] += 1
            else:
                count[string] = 1

        # Step 2: Determine the highest frequency
        max_count = 0
        most_frequent_strings = []
        for string, freq in count.items():
            if freq > max_count:
                max_count = freq
                most_frequent_strings = [string]
            elif freq == max_count:
                most_frequent_strings.append(string)

        # Step 3: Get the highest (alphabetically) string among those with the highest frequency
        most_frequent_max_string = max(most_frequent_strings)

        return most_frequent_max_string

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Loading_Process()  # Pass the user's email here
    sys.exit(app.exec_())