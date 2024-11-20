import requests
import cv2
import numpy as np
import imutils
from STM_connect import STMconnect
from color_Detection import colorDetection
from path_Finding import a_star

# CONFIGURATION
url = "http://192.168.187.221:8080/shot.jpg"
carDiameter = 23  # cm
goalPosition = (20, 20)

# COLORS
blueLow = np.array([-9, 144, 182])  # HSV
blueUp = np.array([51, 204, 242])  # HSV
greenLow = np.array([40, 100, 100])  # HSV
greenUp = np.array([70, 255, 255])  # HSV

# VIDEO STREAMING
while True:
    videoResponse = requests.get(url)
    videoArr = np.array(bytearray(videoResponse.content), dtype=np.uint8)
    video = cv2.imdecode(videoArr, -1)
    video = imutils.resize(video, width=1000, height=800)

    hsv = cv2.cvtColor(video, cv2.COLOR_BGR2HSV)

    # MASKING
    maskObstacle = cv2.inRange(hsv, blueLow, blueUp)
    maskCar = cv2.inRange(hsv, greenLow, greenUp)

    # FINDING CAR
    carPosition = None
    for contour in cv2.findContours(maskCar, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]:
        if cv2.contourArea(contour) > 20:
            x, y, w, h = cv2.boundingRect(contour)
            carPosition = (y + h // 2, x + w // 2)

    # Run pathfinding
    if carPosition:
        obstacle_map = np.zeros((128, 128), dtype=np.uint8)
        for contour in cv2.findContours(maskObstacle, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]:
            if cv2.contourArea(contour) > 50:
                x, y, w, h = cv2.boundingRect(contour)
                obstacle_map[y:y + h, x:x + w] = 1
        path = a_star(obstacle_map, carPosition, goalPosition)

    # DISPLAY
    cv2.imshow("Video Feed", video)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
