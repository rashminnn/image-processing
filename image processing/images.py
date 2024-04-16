import cv2 as cv
import numpy as np

img = cv.imread('images/IMG_3443.jpg')


def rescale(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


img = rescale(img, 0.75)

cv.imshow('Image', img)
cv.waitKey(0)
