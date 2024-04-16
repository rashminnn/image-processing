# gamma correction 1
import cv2 as cv
import numpy as np

gamma = 4
f = cv.imread('images/0001.jpg', cv.IMREAD_COLOR)/255

cv.namedWindow('Image', cv.WINDOW_NORMAL)
cv.imshow('Image', f)
cv.waitKey(0)

g = f**gamma
cv.namedWindow('Image', cv.WINDOW_NORMAL)
cv.imshow('Image', g)
cv.waitKey(0)

cv.destroyAllWindows()
