import numpy as np
import time
import cv2

cap = cv2.VideoCapture(0)
size = (int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))

fps = 20
fourcc = 0
vout = cv2.VideoWriter()
success = vout.open('output.avi',fourcc,fps,size,True)
ret, frame = cap.read()

frame = cv2.flip(frame, -1)

print("Writing")
counter = 0

# Note that with the timer sleeping for 1 second 50 counters is 2 seconds
# So to up this if we were to get 1 minuet we would need 60 / 2 = x
# x * 50 wich would = 1,500
while(counter < 100):
	vout.write(frame)
	time.sleep(1)
	counter = counter + 1
print("exiting")

cap.release()
vout.release()
cv2.destroyAllWindows()
