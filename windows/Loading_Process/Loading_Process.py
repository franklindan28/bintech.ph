import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox, QHBoxLayout, QProgressBar
from PyQt5.QtGui import QIcon
import sqlite3

sys.path.insert(5,'windows/Add_On')
import Add_On

class Loading_Process(QMainWindow):
    def __init__(self, username):
        super().__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowTitle("Loading Process")
        self.setWindowIcon(QIcon("Images/bintech logo.png"))
        self.setStyleSheet("background-color : #FFFAF3")
        self.user_name = username

        layout = QHBoxLayout()

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

        self.progress = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(0)

    def update_progress(self):
        self.progress += 1
        self.progress_bar.setValue(self.progress)
        
        if self.progress >= 100:
            self.timer.stop()
            QTimer.singleShot(2000, self.reset_loading)  # Reset loading after 2 seconds
            QTimer.singleShot(2000, self.add)  # Reset loading after 2 seconds
            self.showFullScreen()

    def reset_loading(self):
        self.progress = 0
        self.progress_bar.setValue(0)
        self.timer.start(50)
        

    def add(self):
        self._add_on = Add_On.Add_on(self.user_name)  
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Loading_Process()  # Pass the user's email here
    sys.exit(app.exec_())