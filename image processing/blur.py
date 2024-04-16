import cv2 as cv

img = cv.imread('images/noise.jpg', cv.IMREAD_COLOR)
k = 11
img_blur = cv.blur(img, (k, k))
gaussian = cv.GaussianBlur(img, (k, k), 5)
median = cv.medianBlur(img, k)

cv.imshow('original', img)
cv.imshow('blur', img_blur)
cv.imshow('gaussian', gaussian)
cv.imshow('median', median)
cv.waitKey(0)
cv.destroyAllWindows()
k
