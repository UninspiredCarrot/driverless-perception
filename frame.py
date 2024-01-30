import cv2
import process_frame
import time

frame = cv2.imread("media/test/6.jpg")

start_time = time.time()
frame = process_frame.process(frame)
end_time = time.time()
execution_time = end_time - start_time

cv2.imshow('Feed', frame)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()