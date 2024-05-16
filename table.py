import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem

class TableExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Table Example')
        self.setGeometry(100, 100, 600, 400)

        self.initUI()

    def initUI(self):
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(5)  # Number of rows
        self.tableWidget.setColumnCount(3)  # Number of columns

        self.tableWidget.setHorizontalHeaderLabels(['Column 1', 'Column 2', 'Column 3'])

        for row in range(5):
            for col in range(3):
                item = QTableWidgetItem(f'Row {row+1}, Col {col+1}')
                self.tableWidget.setItem(row, col, item)

        self.setCentralWidget(self.tableWidget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TableExample()
    window.show()
    sys.exit(app.exec_())
