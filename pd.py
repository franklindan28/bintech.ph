import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QImage, QPixmap, QPainter, QColor, QFont
from PyQt5.QtCore import Qt, QTimer
import cv2
from ultralytics import YOLO
import supervision as sv
import re

class PlasticClassificationApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.frame_width, self.frame_height = 640, 640
        self.cap = cv2.VideoCapture()
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.frame_width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.frame_height)

        self.model = YOLO('best 2.pt', task='detect')
        self.box_annotator = sv.BoxAnnotator(thickness=2, text_thickness=2, text_scale=1)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)

        self.start_button = QPushButton('Start', self)
        self.start_button.clicked.connect(self.start_classification)

        self.stop_button = QPushButton('Stop', self)
        self.stop_button.clicked.connect(self.stop_classification)

        self.quit_button = QPushButton('Quit', self)
        self.quit_button.clicked.connect(self.quit_application)

        self.layout = QVBoxLayout(self.central_widget)
        self.layout.addWidget(self.image_label)
        self.layout.addWidget(self.start_button)
        self.layout.addWidget(self.stop_button)
        self.layout.addWidget(self.quit_button)

        self.is_running = False
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(30)

    def start_classification(self):
        self.is_running = True

    def stop_classification(self):
        self.is_running = False

    def quit_application(self):
        self.is_running = False
        self.cap.release()
        self.close()

    def update(self):
        if self.is_running:
            success, frame = self.cap.read()
            if success:
                frame, labels = self.process_frame(frame)
                self.display_frame(frame, labels)
                if labels:
                    extract = " ".join(re.findall("[a-zA-Z]+", str(labels[0])))
                    print(extract)
            else:
                print("Error: Could not read frame.")

    def process_frame(self, frame):
        frame = cv2.resize(frame, (320, 320), interpolation=cv2.INTER_LINEAR)
        result = self.model(frame, max_det=1)[0]
        detections = sv.Detections.from_yolov8(result)
        labels = [
            f"{self.model.model.names[class_id]} {confidence:0.2f}"
            for _, confidence, class_id, _
            in detections
        ]
        frame = self.box_annotator.annotate(scene=frame, detections=detections, labels=labels)
        return frame, labels

    def display_frame(self, frame, labels):
        painter = QPainter()
        painter.begin(frame)
        painter.setPen(QColor(255, 0, 0))

        font = QFont()
        font.setPointSize(16)
        painter.setFont(font)

        for label in labels:
            painter.drawText(10, 30, label)

        painter.end()

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        height, width, channel = frame.shape
        bytes_per_line = 3 * width
        q_image = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(q_image)
        self.image_label.setPixmap(pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = PlasticClassificationApp()
    main_window.show()
    sys.exit(app.exec_())
