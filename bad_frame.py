import cv2
from triangulation import get_depth, get_latitude
import bad_window_matching
from inference import infer
import sort

CONFIDENCE_LIMIT = 0.8

def draw_label(frame, x, y, w, h, label):

    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return frame
    
id = 0


frame = cv2.imread("media/out.png")
frame_height, frame_width, _ = frame.shape

left_frame = frame[:, :frame_width//2]
right_frame = frame[:, frame_width//2:]

results = infer(left_frame)
results = [x for x in results if x['class'] == "yellow_cone"]
results = sort.sort(results)
for result in results:
    xl, y, width, height = result["xywh"]
    confidence = result["confidence"]
    draw_label(frame, xl, y, width, height, f"{id}")

    # Window Matching 
    xr = bad_window_matching.get_right_point(left_frame, right_frame, xl, y, width, height)

    # YOLO on Both Images
    # xr = both_yolo.get_right_point(result, right_frame, id)
    
    depth = get_depth(xl, xr)
    latitude = get_latitude(xl, depth)
    draw_label(frame, frame_width//2 + xr, y, width, height, f"x: {round(depth, 2)}m, y: {round(latitude, 2)}m")
    print(id, sort.get_area(result), f"x: {round(depth, 2)}m, y: {round(latitude, 2)}m")
    id += 1


cv2.imshow('Feed', frame)

# Press Q on keyboard to  exit
if cv2.waitKey(0) & 0xFF == ord('q'):

    # Closes all the frames
    cv2.destroyAllWindows()