import sys
import serial
import mysql.connector
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget


class RFIDReaderApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Initialize serial port
        self.serial_port = serial.Serial('COM4', 9600)  # Change 'COM3' to your Arduino's serial port
        
        # Initialize database connection
        self.db_config = {
            'host': 'localhost',        # Change if your MySQL server is hosted elsewhere
            'user': 'username',         # Your MySQL username
            'password': 'password',     # Your MySQL password
            'database': 'rfid_database' # Your MySQL database name
        }
        self.conn = mysql.connector.connect(**self.db_config)
        self.cursor = self.conn.cursor()
        
        # Set up GUI
        self.setWindowTitle("RFID Reader")
        
        self.label = QLabel("Place RFID tag near the reader")
        self.btn_exit = QPushButton("Exit")
        self.btn_exit.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.btn_exit)
        
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Start reading RFID tags
        self.read_rfid()

    def read_rfid(self):
        while True:
            if self.serial_port.in_waiting > 0:
                uid = self.serial_port.readline().decode().strip()
                print("Received RFID Tag UID:", uid)
                self.label.setText(f"Received RFID Tag UID: {uid}")
                
                # Insert the UID into the database
                try:
                    self.cursor.execute("INSERT INTO rfid_tags (uid) VALUES (%s)", (uid,))
                    self.conn.commit()
                    print("RFID UID inserted successfully")
                except mysql.connector.Error as err:
                    print("Error:", err)


def main():
    app = QApplication(sys.argv)
    window = RFIDReaderApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
