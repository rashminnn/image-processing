# Histrograms and histrogram equalization(Greyscale)

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('images/0001.jpg', cv.IMREAD_GRAYSCALE)
hist = cv.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist)
plt.xlim([0, 256])
plt.show()

# Histogram of a color image


img = cv.imread('images/0001.jpg', cv.IMREAD_COLOR)
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])
plt.show()

# list = [255, 250, 192, 210, 111]
# for i, nu in enumerate(list):
#     print(i, nu)
