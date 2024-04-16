import cv2 as cv

img = cv.imread('images/xb.jpg', cv.IMREAD_COLOR)
img2 = cv.cvtColor(img, cv.COLOR_BGR2HSV)
img3 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img4 = cv.cvtColor(img, cv.COLOR_BGR2HLS)

cv.imshow('image', img)
cv.imshow('image2', img2)
cv.imshow('image3', img3)
cv.imshow('image4', img4)
cv.waitKey(0)
