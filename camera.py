# working code for using camera for object dertection purposes
# used yolo v8 model for object dertection 
# classifying 2 objects
# 1.scratched paint
# 2.crack 

from ultralytics import YOLO
import cv2
import time

model = YOLO('/home/jaswanth/projects/Wall-Crack-Detection/models/objectDetection/best.pt')

cap = cv2.VideoCapture(0)

detection_interval = 1

tracker = None
object_detected = False

last_detection_time = time.time()

ret = True
while ret:
    ret, frame = cap.read()

    if ret:

        current_time = time.time()
        if current_time - last_detection_time >= detection_interval:
            last_detection_time = current_time
            results = model.track(frame, persist=True)
            frame_ = results[0].plot()
            cv2.imshow('frame', frame_)
        if object_detected:
            print("Object detected")
            object_detected = False

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break