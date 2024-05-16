import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QProgressBar

class ProgressBinChart(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Progress Bin Chart')
        self.setGeometry(100, 100, 200, 400)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.progress_bars = []

        for i in range(5):
            progress_bar = QProgressBar()
            progress_bar.setRange(0, 100)
            progress_bar.setValue(0)
            layout.addWidget(progress_bar)
            self.progress_bars.append(progress_bar)

        self.update_progress(30, 40, 60, 80, 20)  # Example data

    def update_progress(self, *values):
        for progress_bar, value in zip(self.progress_bars, values):
            progress_bar.setValue(value)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ProgressBinChart()
    window.show()
    sys.exit(app.exec_())
