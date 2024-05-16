import subprocess
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.text_edit = QLineEdit(self)
        self.button1 = QPushButton('Show Onboard')
        
        layout.addWidget(self.button1)
        self.setLayout(layout)

        self.button1.clicked.connect(self.showOnboard)

    def showOnboard(self):
        try:
            # Launch onboard as a subprocess
            subprocess.Popen(['onboard'])
        except FileNotFoundError:
            print("Onboard is not installed or not available in the system")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
