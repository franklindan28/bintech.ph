import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QProgressBar
from PyQt5.QtCore import Qt, QTimer

class LoadingScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Loading Screen")
        self.setGeometry(100, 100, 300, 150)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setGeometry(50, 50, 200, 20)
        
        self.label = QLabel(self)
        self.label.setGeometry(50, 80, 200, 20)

        self.progress = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(50)

    def update_progress(self):
        self.progress += 1
        self.progress_bar.setValue(self.progress)
        self.label.setText(f"Loading... {self.progress}%")
        
        if self.progress >= 100:
            self.timer.stop()
            self.label.setText("Loading Complete")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoadingScreen()
    window.show()
    sys.exit(app.exec_())
