import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv

img = cv.imread('images/0001.jpg', cv.IMREAD_COLOR)

assert img is not None

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

th2 = cv.adaptiveThreshold(
    img_gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)

edge = cv.Canny(img_gray, 150, 220)
contours, _ = cv.findContours(edge, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

img_contours = th2.copy()
img_contours = cv.drawContours(img_contours, contours, -1, (0, 255, 0), 2)

fig, ax = plt.subplots(2, 2, figsize=(15, 5))

ax[0, 0].imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
ax[0, 0].set_title('Original Image')
ax[0, 0].set_axis_off()

ax[0, 1].imshow(th2, cmap='gray')
ax[0, 1].set_title('Adaptive Thresholding')
ax[0, 1].set_axis_off()

ax[1, 0].imshow(edge, cmap='gray')
ax[1, 0].set_title('Canny Edge Detection')
ax[1, 0].set_axis_off()

ax[1, 1].imshow(cv.cvtColor(img_contours, cv.COLOR_BGR2RGB))
ax[1, 1].set_title('Contour Detection')
ax[1, 1].set_axis_off()

cv.imshow('Contour Detection', img_contours)
cv.waitKey(0)
cv.destroyAllWindows()
plt.show()
