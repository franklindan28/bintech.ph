from PyQt5 import QtWidgets, uic
import serial
from database import Database

class LoginWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/login.ui", self)

        self.db = Database()

        self.btn_login.clicked.connect(self.login)

        # Serial port initialization
        self.serial = serial.Serial('/dev/ttyACM0', 9600)  # Adjust port accordingly

    def login(self):
        username = self.txt_username.text()
        password = self.txt_password.text()

        if not username or not password:
            QtWidgets.QMessageBox.warning(self, "Warning", "Please enter username and password.")
            return

        # Read RFID tag
        rfid_tag = self.read_rfid()

        if not rfid_tag:
            QtWidgets.QMessageBox.warning(self, "Warning", "RFID tag not found.")
            return

        if self.db.login_user(username, password, rfid_tag):
            QtWidgets.QMessageBox.information(self, "Success", "Login Successful.")
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "Login Failed. Incorrect username or password.")

    def read_rfid(self):
        rfid_tag = self.serial.read(12)  # Assuming RFID tag is 12 bytes
        return rfid_tag.decode('utf-8') if rfid_tag else None

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    login_window = LoginWindow()
    login_window.show()
    app.exec()
