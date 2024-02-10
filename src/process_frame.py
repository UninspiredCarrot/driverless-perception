import cv2
import triangulation
import window_matching
from inference import infer
import sort
import zed_opencv_native

CONFIDENCE_LIMIT = 0.8

def draw_label(frame, x, y, w, h, label):

    cv2.rectangle(frame, (x-w//2, y-h//2), (x + w//2, y + h//2), (0, 255, 0), 2)
    cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return frame


def process(frame): 
    

    frame = zed_opencv_native.process(frame)

    frame_height, frame_width, _ = frame.shape

    left_frame = frame[:, :frame_width//2]
    right_frame = frame[:, frame_width//2:]

    all_results = infer(left_frame)
    all_results = [x for x in all_results if x['confidence'] >= 0.8]
    cone_types = ["blue_cone", "yellow_cone", "orange_cone"]
    for cone_type in cone_types:
        results = [x for x in all_results if x["class"] == cone_type]
        results = sort.sort(results)

        previous_disparity = left_frame.shape[1]
        for result in results:
            xl, y, width, height = result["xywh"]
            confidence = result["confidence"]
            draw_label(frame, xl, y, width, height, f"conf: {confidence}")

            # Window Matching 
            xr = window_matching.get_right_point(left_frame, right_frame, xl, y, width, height, previous_disparity)

            # YOLO on Both Images
            # xr = both_yolo.get_right_point(result, right_frame, id)
            
            depth = triangulation.get_depth(xl, xr, left_frame.shape[1])
            latitude = triangulation.get_latitude(xl, depth, left_frame.shape[1])
            draw_label(frame, frame_width//2 + xr, y, width, height, f"x: {round(depth, 2)}m, y: {round(latitude, 2)}m")
            previous_disparity = xl-xr
            print(depth, latitude, left_frame.shape[1])
    return frame


