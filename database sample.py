import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox
import mysql.connector

class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Simple CRUD Dashboard")

        # Connect to MySQL Database
        self.conn = mysql.connector.connect(
            host="127.0.0.1",
            user="qwerty",
            password="password123",
            database="login"
        )

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Widgets
        self.name_label = QLabel("Name:")
        self.name_input = QLineEdit()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)

        self.add_button = QPushButton("Add")
        self.add_button.clicked.connect(self.add_data)
        layout.addWidget(self.add_button)

        self.delete_button = QPushButton("Delete")
        self.delete_button.clicked.connect(self.delete_data)
        layout.addWidget(self.delete_button)

        self.update_button = QPushButton("Update")
        self.update_button.clicked.connect(self.update_data)
        layout.addWidget(self.update_button)

        self.show()

    def add_data(self):
        name = self.name_input.text()
        if name:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO employees (name) VALUES (%s)", (name,))
            self.conn.commit()
            cursor.close()
            QMessageBox.information(self, "Success", f"Added {name} successfully!")
            self.name_input.clear()
        else:
            QMessageBox.warning(self, "Error", "Name cannot be empty!")

    def delete_data(self):
        name = self.name_input.text()
        if name:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM employees WHERE name = %s", (name,))
            self.conn.commit()
            cursor.close()
            QMessageBox.information(self, "Success", f"Deleted {name} successfully!")
            self.name_input.clear()
        else:
            QMessageBox.warning(self, "Error", "Name cannot be empty!")

    def update_data(self):
        old_name = self.name_input.text()
        new_name = input("Enter the new name: ")
        if old_name and new_name:
            cursor = self.conn.cursor()
            cursor.execute("UPDATE employees SET name = %s WHERE name = %s", (new_name, old_name))
            self.conn.commit()
            cursor.close()
            QMessageBox.information(self, "Success", f"Updated {old_name} to {new_name} successfully!")
            self.name_input.clear()
        else:
            QMessageBox.warning(self, "Error", "Both old and new name are required!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Dashboard()
    sys.exit(app.exec_())
