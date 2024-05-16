import ultralytics
import cv2
import argparse
#import onnxruntime as ort

from ultralytics import YOLO
import supervision as sv
import numpy as np

from pprint import pprint
import re
import time
import torch

torch.cuda.set_device(0)

def parse_arguments() ->argparse.Namespace:
    parser = argparse.ArgumentParser(description="Plastic Classification")
    parser.add_argument(
        "--webcam-resolution",
        default=[640,640],
        nargs=2,
        type=int
    )
    args = parser.parse_args()
    return args

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


def main():
    args = parse_arguments()
    frame_width, frame_height = args.webcam_resolution

    try:
        cap = cv2.VideoCapture()
        if not cap.isOpened():
            raise Exception("Error: Could not open camera.")

        cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

        model = YOLO('best 2.pt', task='detect')
        box_annotator = sv.BoxAnnotator(
            thickness=2,
            text_thickness=2,
            text_scale=1
        )

        while True:
            success, frame = cap.read()
            if not success:
                print("Error: Could not read frame.")
                break

            try:
                frame, labels = process_frame(frame, model, box_annotator)
               # cv2.imshow("plastic detection", frame)

                if labels:
                    extract = " ".join(re.findall("[a-zA-Z]+", str(labels[0])))
                    #print(extract)
                    return extract
                    det()

            except Exception as frame_processing_error:
                print(f"Error processing frame: {frame_processing_error}")

            if cv2.waitKey(30) == 27:
                break

    except Exception as main_error:
        print(f"Error: {main_error}")

    finally:
        if 'cap' in locals() and cap.isOpened():
            cap.release()
        cv2.destroyAllWindows()
        
def det(extract):
    print("Inside Main", extract)
    
#detection = main()
#det(detection) 

if __name__ == "__main__":
    main()
