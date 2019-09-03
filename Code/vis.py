print ('Vis.py running.')

import sys
import numpy as np
import cv2
import argparse


im = cv2.imread('C:/Users/Nick Orr/Documents/Programming Projects/RoboticsVisionTests/Images/RocketPanelStraight84in.jpg')
hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)

lower_green = np.array([0,0,170])
upper_green = np.array([250,200,255])

#lower_green = np.array([10,0,250])
#upper_green = np.array([170,30,255])

mask = cv2.inRange(hsv,lower_green, upper_green)
res = cv2.bitwise_and(im,im, mask = mask)

res = cv2.medianBlur(res,5)
res = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY);

cv2.imshow('im',im)
cv2.imshow('mask',mask)
cv2.imshow('res',res)

lower_grey = np.array([0,0,245])
upper_grey = np.array([255,255,255])

mask2 = cv2.inRange(hsv,lower_grey, upper_grey)
res2 = cv2.bitwise_and(res,res, mask = mask2)

kernel = np.ones((2,2),np.uint8)

res2 = cv2.erode(res2, kernel, iterations = 3)
res2 = cv2.dilate(res2, kernel, iterations = 1)
res2 = cv2.erode(res2, kernel, iterations = 2)
res2 = cv2.dilate(res2, kernel, iterations = 2)

kernel = np.ones((5,5),np.uint8)

res2 = cv2.dilate(res2, kernel, iterations = 1)
res2 = cv2.erode(res2, kernel, iterations = 2)
res2 = cv2.dilate(res2, kernel, iterations = 2)





cv2.imshow('mask2',mask2)
cv2.imshow('res2',res2)

cv2.waitKey(0)
cv2.destroyAllWindows()

print ('Vis.py exiting.')
