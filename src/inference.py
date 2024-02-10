from ultralytics import YOLO
import os

path = os.path.dirname(os.path.abspath(__file__)) + '/model.pt'
model = YOLO(path)

classes = {
   "0": "yellow_cone",
   "1": "blue_cone",
   "2": "orange_cone",
   "3": "large_orange_cone",
   "4": "unknown_cone"
}

def infer(image):

    results = model(image)
    results_list = []

    for i in range(len(results[0].boxes.cls)):
        results_list.append({
            "class": classes[str(int(results[0].boxes.cls[i].item()))],
            "confidence": results[0].boxes.conf[i].item(),
            "xywh": [int(x) for x in results[0].boxes.xywh[i].tolist()]})

    return results_list
