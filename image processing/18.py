import cv2 as cv
import numpy as np

gamma = 4
f = cv.imread('images/0001.jpg', cv.IMREAD_GRAYSCALE)

cv.namedWindow('Image',  cv.WINDOW_AUTOSIZE)
cv.imshow('Image', f)
cv.waitKey(0)

t = np.array([(i/255.0)**(gamma)*255 for i in np.arange(0, 256)]
             ).astype(np.uint8)

g = cv.LUT(f, t)

cv.namedWindow('Image',  cv.WINDOW_AUTOSIZE)
cv.imshow('Image', g)
cv.waitKey(0)

cv.destroyAllWindows()
