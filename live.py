import cv2
import numpy
from triangulation import get_depth, get_latitude
import window_matching
import both_yolo
from inference import infer

video_capture = cv2.VideoCapture("output.mp4")
CONFIDENCE_LIMIT = 0.8

def draw_label(frame, x, y, w, h, label):

    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return frame
    
id = 0
while (video_capture.isOpened()):

    ret, frame = video_capture.read()
    frame_height, frame_width, _ = frame.shape

    left_frame = frame[:, :frame_width//2]
    right_frame = frame[:, frame_width//2:]

    if ret == True:
        results = infer(left_frame)
        for result in results:
            class_ = result["class"]
            xl, y, width, height = result["xywh"]
            confidence = result["confidence"]
            if confidence > 0.8:
                draw_label(frame, xl, y, width, height, f"{class_}")

                # Window Matching 
                # xr1 = window_matching.get_right_point(left_frame, right_frame, xl, y, width, height, grayscale=False)

                # YOLO on Both Images
                xr = both_yolo.get_right_point(result, right_frame, id)
                
                depth = get_depth(xl, xr)
                latitude = get_latitude(xl, depth)
                draw_label(frame, frame_width//2 + xr, y, width, height, f"x: {round(depth, 2)}m, y: {round(latitude, 2)}m")


        cv2.imshow('Feed', frame)

        # Press Q on keyboard to  exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    else: 
        break
    id += 1

# When everything done, release the video capture object
video_capture.release()

# Closes all the frames
cv2.destroyAllWindows()
