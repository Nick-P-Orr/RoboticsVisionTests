print ('Vis.py running.')

import sys
import numpy as np
import cv2
import argparse


cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    blur = cv2.GaussianBlur(frame, (5,5), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    
    lower_white = np.array([80,0,30])
    upper_white = np.array([160,150,160])

    mask = cv2.inRange(hsv, lower_white, upper_white)

    kernel = np.ones((5,5),np.uint8)
    mask = cv2.erode(mask, kernel, iterations = 4)
    mask = cv2.dilate(mask, kernel, iterations = 3)
    
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
    cv2.drawContours(frame, contours, -1, (0, 0, 255), 1)

    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(1)
    if key == 27:
        break


cap.release()
print ('Vis.py exiting.')
