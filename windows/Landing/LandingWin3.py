import sys
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QMessageBox, QLineEdit, QApplication, QHBoxLayout, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon, QPixmap

# Import necessary modules from the third file
from ultralytics import YOLO
import supervision as sv
import cv2
import re
import torch

torch.cuda.set_device(0)

# ... (other imports)

# Define the process_frame function here (from the third file)
def process_frame(frame, model, box_annotator):
    frame = cv2.resize(frame, (320, 320), interpolation=cv2.INTER_LINEAR)
    result = model(frame, max_det=1)[0]
    detections = sv.Detections.from_yolov8(result)
    labels = [
        f"{model.model.names[class_id]} {confidence:0.2f}"
        for _, confidence, class_id, _
        in detections
    ]
    frame = box_annotator.annotate(scene=frame, detections=detections, labels=labels)
    return frame, labels

# ... (other necessary functions and classes)

class LandingWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # ... (previous code)

        self.timer = QTimer(self)  # Timer for periodic updates
        self.timer.timeout.connect(self.update_plastic_detection)

        # ... (remaining code)

    def clickDetection(self):
        try:
            # Initialize the YOLO model and other necessary components
            model = YOLO('best 2.pt', task='detect')
            box_annotator = sv.BoxAnnotator(
                thickness=2,
                text_thickness=2,
                text_scale=1
            )

            self.timer.start(1000)  # Start the timer with a 1-second interval

        except Exception as initialization_error:
            print(f"Error initializing components: {initialization_error}")

    def update_plastic_detection(self):
        try:
            # Capture a frame from your camera (you may need to adapt this part)
            success, frame = cap.read()
            if not success:
                print("Error: Could not read frame.")
                return

            frame, labels = process_frame(frame, model, box_annotator)
            cv2.imshow("plastic detection", frame)

            if labels:
                extract = " ".join(re.findall("[a-zA-Z]+", str(labels[0])))
                print(extract)

        except Exception as frame_processing_error:
            print(f"Error processing frame: {frame_processing_error}")

    # ... (remaining code)

# ... (remaining code)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = LandingWindow()
    sys.exit(app.exec_())


