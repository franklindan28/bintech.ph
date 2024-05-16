import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QMovie, QIcon

class SlideshowWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowTitle("Landing Page")
        self.setWindowIcon(QIcon("Images/bintech logo.png"))
        self.setStyleSheet("background-color : #FFFAF3")

        self.current_slide = 0
        self.slides = [
            "Images/WELCOME TO.gif"
        ]
        
        self.init_ui()
        self.showFullScreen()

    def init_ui(self):
        # Create QLabel to display slideshow images
        self.slide_label = QLabel(self)
        self.slide_label.setAlignment(Qt.AlignCenter)
        self.slide_label.setScaledContents(True)  # Fit contents to label size
        self.show_slide()

        # Set up a timer to switch slides every 3 seconds
        self.slide_timer = QTimer()
        self.slide_timer.timeout.connect(self.next_slide)
        self.slide_timer.start(3000)

    def show_slide(self):
        movie = QMovie(self.slides[self.current_slide])
        movie.setScaledSize(self.size())  # Set movie size to window size
        movie.setCacheMode(QMovie.CacheAll)  # Cache entire movie in memory for smoother playback
       # movie.setPlaybackMode(QMovie.PlayOnce)  # Play GIF once
        movie.RatioMode(Qt.IgnoreAspectRatio)  # Ignore aspect ratio while scaling
        self.slide_label.setMovie(movie)
        movie.start()

    def next_slide(self):
        self.current_slide = (self.current_slide + 1) % len(self.slides)
        self.show_slide()

    def mousePressEvent(self, event):
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
