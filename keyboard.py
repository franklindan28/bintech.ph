import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit

class VirtualKeyboard(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Virtual Keyboard')
        self.setGeometry(50, 500, 500, 300)

        # Create QLineEdit to display text
        self.text_edit = QLineEdit(self)
        self.text_edit.setFocusPolicy(3)  # NoFocus

        # Create buttons for each letter
        layout = QVBoxLayout()
        buttons_layout = QVBoxLayout()
        row_layout = None
        buttons = "QWERTYUIOPASDFGHJKLZXCVBNM"

        for i, char in enumerate(buttons):
            if i % 6 == 0:
                row_layout = QHBoxLayout()
                buttons_layout.addLayout(row_layout)
            button = QPushButton(char, self)
            button.clicked.connect(self.create_button_click_handler(char))
            row_layout.addWidget(button)

        layout.addWidget(self.text_edit)
        layout.addLayout(buttons_layout)
        self.setLayout(layout)

        # Hide the keyboard initially
        self.hide()

    def on_button_click(self, char):
        current_text = self.text_edit.text()
        self.text_edit.setText(current_text + char)

    def create_button_click_handler(self, char):
        def handler():
            current_text = self.text_edit.text()
            self.text_edit.setText(current_text + char)
        return handler

    def showEvent(self, event):
        # Show the keyboard when the window is shown
        self.text_edit.setFocus()

    def hideEvent(self, event):
        # Hide the keyboard when the window is hidden
        self.hide()
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VirtualKeyboard()
    window.show()
    sys.exit(app.exec_())
