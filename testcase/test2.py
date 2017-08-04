import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
video = cv2.VideoWriter('test.avi', 0, 32, (640,360), 1)

ret, img = cap.read()
video.write(img)
print("Writing")
time.sleep(20)
print("Releasing")
video.release()
cap.release()

