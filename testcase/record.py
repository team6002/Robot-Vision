import numpy as np
import time
import cv2

print("Writing Video")
cap = cv2.VideoCapture(0)
out = cv2.VideoWriter('output.avi', 0, 20.0, (640,480))

time.sleep(20)

print("Releasing Video")
out.release()
