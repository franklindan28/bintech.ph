from PyQt5 import QtWidgets, uic
from database import Database

class RegistrationWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/registration.ui", self)

        self.db = Database()

        self.btn_register.clicked.connect(self.register_user)

    def register_user(self):
        username = self.txt_username.text()
        password = self.txt_password.text()

        if not username or not password:
            QtWidgets.QMessageBox.warning(self, "Warning", "Please enter username and password.")
            return

        if self.db.register_user(username, password):
            QtWidgets.QMessageBox.information(self, "Success", "Registration Successful.")
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "Registration Failed. Username may already exist.")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    registration_window = RegistrationWindow()
    registration_window.show()
    app.exec()
