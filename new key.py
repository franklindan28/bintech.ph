import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QHBoxLayout

class VirtualKeyboard(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Virtual Keyboard')
        layout = QVBoxLayout()

        self.text_edit = QLineEdit()
        layout.addWidget(self.text_edit)

        keyboard_layout = [
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
            ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
            ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
            ['Shift', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Backspace'],
            ['Space', 'Enter']
        ]

        for row in keyboard_layout:
            row_layout = QHBoxLayout()
            for key in row:
                button = QPushButton(key)
                if key == 'Space':
                    button.setFixedSize(150, 30)
                elif key == 'Enter':
                    button.setFixedSize(150, 30)
                else:
                    button.setFixedSize(30, 30)
                button.clicked.connect(self.buttonClicked)
                row_layout.addWidget(button)
            layout.addLayout(row_layout)

        self.setLayout(layout)

    def buttonClicked(self):
        button = self.sender()
        key = button.text()

        if key == 'Backspace':
            self.text_edit.backspace()
        elif key == 'Space':
            self.text_edit.insert(' ')
        elif key == 'Enter':
            self.text_edit.insert('\n')
        else:
            self.text_edit.insert(key)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VirtualKeyboard()
    window.show()
    sys.exit(app.exec_())
