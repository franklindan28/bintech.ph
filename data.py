import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon
import sqlite3

class DisplayUsers(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("User Data")
        self.setWindowIcon(QIcon("Images/bintech logo.png"))
        self.setGeometry(100, 100, 800, 600)

        self.table_widget = QTableWidget()
        self.load_data()

        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def load_data(self):
        try:
            conn = sqlite3.connect('bintech.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users")
            data = cursor.fetchall()
            conn.close()

            self.table_widget.setRowCount(len(data))
            self.table_widget.setColumnCount(len(data[0]))

            for i, row in enumerate(data):
                for j, value in enumerate(row):
                    self.table_widget.setItem(i, j, QTableWidgetItem(str(value)))

        except sqlite3.Error as e:
            QMessageBox.critical(self, 'Error', f'Failed to connect to database. Error: {str(e)}')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = DisplayUsers()
    ex.show()
    sys.exit(app.exec_())