import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, QTimer

class SlideshowWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.current_slide = 0
        self.slides = [
            "Images/WELCOME TO.gif",
            "Images/WELCOME TO.gif"
        ]
        
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Slideshow")
        
        # Create a central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create QLabel to display slideshow images
        self.slide_label = QLabel()
        layout.addWidget(self.slide_label)
        
        # Show the initial slide
        self.show_slide()

        # Set up a timer to switch slides every 3 seconds
        self.slide_timer = QTimer()
        self.slide_timer.timeout.connect(self.next_slide)
        self.slide_timer.start(3000)

        # Connect the mouse click event to switch to login system
        central_widget.mousePressEvent = self.switch_to_login

        self.show()

    def show_slide(self):
        pixmap = QPixmap(self.slides[self.current_slide])
        self.slide_label.setPixmap(pixmap)
        self.slide_label.setAlignment(Qt.AlignCenter)

    def next_slide(self):
        self.current_slide = (self.current_slide + 1) % len(self.slides)
        self.show_slide()

    def switch_to_login(self, event):
        # Implement the login system here
        print("Switching to login system...")
        # For now, simply close the slideshow window
        self.close()

def main():
    app = QApplication(sys.argv)
    window = SlideshowWindow()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
