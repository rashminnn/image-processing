# open with opencv's  HIGHGUI
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('images/0001.jpg', cv.IMREAD_COLOR)
cv.namedWindow('image', cv.WINDOW_AUTOSIZE)
cv.imshow('Rashmin', img)
cv.waitKey(0)
cv.destroyAllWindows()
