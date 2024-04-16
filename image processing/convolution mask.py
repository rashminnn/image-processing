# convolution mask

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread('images/0001.jpg', cv.IMREAD_ANYCOLOR)
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img = cv.GaussianBlur(img, (13, 13), 0)
edges = cv.Laplacian(img, -1, ksize=5, scale=1, delta=0,
                     borderType=cv.BORDER_DEFAULT)
abs_dst = cv.convertScaleAbs(edges)
output = [img, abs_dst]
titles = ['Original', 'Passed through HPF']

for i in range(2):
    plt.subplot(1, 2, i + 1)
    plt.imshow(output[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()
