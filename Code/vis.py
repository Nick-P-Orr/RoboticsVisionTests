print ('Vis.py running.')

import sys
import numpy
import cv2


image = cv2.imread('C:/Users/Nick Orr/Documents/Programming Projects/Robotics Vision/Code/tetris_blocks.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original image', image)
cv2.imshow('Gray image', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()

print ('Vis.py exiting.')
