import cv2
import process_frame
import time

video_capture = cv2.VideoCapture("output.mp4")
CONFIDENCE_LIMIT = 0.8

def draw_label(frame, x, y, w, h, label):

    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return frame

total = 0
count = 0
while (video_capture.isOpened()):

    ret, frame = video_capture.read()
    

    if ret == True:
        start_time = time.time()
        process_frame.process(frame)
        end_time = time.time()
        execution_time = end_time - start_time
        count += 1
        total += execution_time

        # print("Average time taken:", total/count, "seconds")

        cv2.imshow('Feed', frame)

        # Press Q on keyboard to  exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    else: 
        break

# When everything done, release the video capture object
video_capture.release()

# Closes all the frames
cv2.destroyAllWindows()
