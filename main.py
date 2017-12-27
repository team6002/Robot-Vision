import json
import cv2

# HSV color thresholds for YELLOW
THRESHOLD_LOW = (15, 210, 20);
THRESHOLD_HIGH = (35, 255, 255);

# Webcam parameters (your desired resolution)
CAMERA_WIDTH = 320
CAMERA_HEIGHT = 240

# Minimum required radius of enclosing circle of contour
MIN_RADIUS = 2

# Initialize camera and get actual resolution
cam = cv2.VideoCapture(0)
# cam.set(cv2.CV_CAP_PROP_FRAME_WIDTH, CAMERA_WIDTH)
# cam.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, CAMERA_HEIGHT)
# camWidth = cam.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
# camHeight = cam.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)
cam.set(CAMERA_WIDTH, CAMERA_HEIGHT)

print("Camera initialized: (" + str(CAMERA_WIDTH) + ", " + str(CAMERA_HEIGHT) + ")")

# Main loop
while True:

    # Get image from camera
    ret_val, img = cam.read()

    # Blur image to remove noise
    img_filter = cv2.GaussianBlur(img.copy(), (3, 3), 0)

    # Convert image from BGR to HSV
    img_filter = cv2.cvtColor(img_filter, cv2.COLOR_BGR2HSV)

    # Set pixels to white if in color range, others to black (binary bitmap)
    img_binary = cv2.inRange(img_filter.copy(), THRESHOLD_LOW, THRESHOLD_HIGH)

    # Dilate image to make white blobs larger
    img_binary = cv2.dilate(img_binary, None, iterations = 1)

    # Find center of object using contours instead of blob detection. From:
    # http://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/
    img_contours = img_binary.copy()
    contours = cv2.findContours(img_contours, cv2.RETR_EXTERNAL, \
        cv2.CHAIN_APPROX_SIMPLE)[-2]

    # Find the largest contour and use it to compute the min enclosing circle
    center = None
    radius = 0
    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        if M["m00"] > 0:
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            if radius < MIN_RADIUS:
                center = None

    # Print out the location and size (radius) of the largest detected contour
    if center != None:
        print(str(center) + " " + str(radius))

    # Draw a green circle around the largest enclosed contour
    if center != None:
        cv2.circle(img, center, int(round(radius)), (0, 255, 0))

    # Store Data
    data = {
        'Raidus' : radius,
        'Center' : center
    }

    # Writing JSON data
    with open('data.json', 'w') as f:
         json.dump(data, f)

    # Show image windows
    cv2.imshow('webcam', img)
    # cv2.imshow('binary', img_binary)
    # cv2.imshow('contours', img_contours)
    cv2.waitKey(1)
