import numpy as np
import cv2

#Loading image in gray scale
img = cv2.imread('image.jpg',0)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


