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
#extract = ''
var_data = ''
def main():
    global var_data
    #global extract
    #LandingWindow.close()
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)

    model = YOLO('best 2.pt', task='detect')
   
    box_annotator = sv.BoxAnnotator(
        thickness=2,                                                                      
        text_thickness=2,
        text_scale=1
    )
    
    if cap.isOpened():
        success, img = cap.read()
        print(success)
        if success:

            result_detect = []

            while(len(result_detect) != 10):                                                                                             
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
                    time.sleep(0.5)
                    extract = " ".join(re.findall("[a-zA-Z]+", str(labels[0])))
                    var_data = extract
                    result_detect.append(var_data)
                    #print(var_data)
                    print(get_data())
                    
                else:
                    print("No detections")
                if (cv2.waitKey(30) == 27):
                    break	
            
            print(f"Result: {result_detect}")
            final_res = find_most_frequent_max_string(result_detect)
            print(f"Final Result: {final_res}")
        else:
            print("cannot capture frames")
        
    else:
        print("cannot open camera")
    
    cap.release()
    cv2.destroyAllWindows()

def get_data():
    my_data = var_data
    return my_data

def find_most_frequent_max_string(arr):
        if not arr:
            return None

        # Step 1: Count each string in the array using a dictionary
        count = {}
        for string in arr:
            if string in count:
                count[string] += 1
            else:
                count[string] = 1

        # Step 2: Determine the highest frequency
        max_count = 0
        most_frequent_strings = []
        for string, freq in count.items():
            if freq > max_count:
                max_count = freq
                most_frequent_strings = [string]
            elif freq == max_count:
                most_frequent_strings.append(string)

        # Step 3: Get the highest (alphabetically) string among those with the highest frequency
        most_frequent_max_string = max(most_frequent_strings)

        return most_frequent_max_string

if __name__ == "__main__":
    main()

