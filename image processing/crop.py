import cv2 as cv

img = cv.imread('images/0001.jpg')
cv.imshow('image', img)
print(img.shape)
cropped = img[0:1500, 800:2200]
cv.imshow('cropped', cropped)
cv.waitKey(0)
cv.destroyAllWindows()
