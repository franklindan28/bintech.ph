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

#torch.cuda.set_device(0)
'''
def parse_arguments() ->argparse.Namespace:
    parser = argparse.ArgumentParser(description="Plastic Classification")
    parser.add_argument(
        "--webcam-resolution",
        default=[640,640],
        nargs=2,
        type=int`123-
    )
    args = parser.parse_args()
    return args'''

def main():
    my_text= ""
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)

    model = YOLO('best.pt', task='detect')
   
    box_annotator = sv.BoxAnnotator(
        thickness=2,                                                                      
        text_thickness=2,
        text_scale=1
    )
    
    if cap.isOpened():
        success, img = cap.read()
        print(success)
        if success:
            while True:                                                                                             
                success, frame = cap.read()
                frame = cv2.resize(frame, (320,320),interpolation=cv2.INTER_LINEAR)
        
                #pprint(dir(model(frame)[0]))
                result = model(frame,max_det=1)[0]
                detections=sv.Detections.from_yolov8(result)
                labels = [
                    f"{model.model.names[class_id]} {confidence:0.2f}"
                    for _, confidence, class_id, _
                    in detections
                    ]

                frame = box_annotator.annotate(scene=frame, detections=detections, labels = labels)
                cv2.imshow("plastic detection", frame)
                if labels:
                    extract = " ".join(re.findall("[a-zA-Z]+", str(labels[0])))
                    my_text = extract
                    print(extract)
                else:
                    print("No detections")
                if (cv2.waitKey(30) == 27):
                    break	
        else:
            print("cannot capture frames")
        
    else:
        print("cannot open camera")
        
    print(my_text)
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

