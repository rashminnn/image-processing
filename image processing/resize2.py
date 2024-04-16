import cv2 as cv

img = cv.imread('images/0001.jpg')
im2 = cv.resize(img, (1920, 1080))
print(img.shape)
print(im2.shape)
cv.imshow("mutti", img)
cv.imshow('resize', im2)
cv.waitKey(0)
cv.destroyAllWindows()
