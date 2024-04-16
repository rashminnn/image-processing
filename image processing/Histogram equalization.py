# Histogram equalization

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('images/0001.jpg', cv.IMREAD_GRAYSCALE)
hist, bins = np.histogram(img.ravel(), 256, [0, 256])
cdf = hist.cumsum()
cdf_normalized = cdf*hist.max()/cdf.max()

plt.plot(cdf_normalized, color='b')
plt.hist(img.flatten(), 256, [0, 256], color='r')
plt.xlim([0, 256])
plt.legend(('cdf', 'histogram'), loc='upper left')
plt.title('Histogram of the origina image')
plt.show()

equ = cv.equalizeHist(img)
hist, bins = np.histogram(equ.ravel(), 256, [0, 256])
cdf = hist.cumsum()
cdf_normalized = cdf*hist.max()/cdf.max()

plt.plot(cdf_normalized, color='b')
plt.hist(equ.flatten(), 256, [0, 256], color='r')
plt.xlim([0, 256])
plt.legend(('cdf', 'histogram'), loc='upper left')
plt.title('Histogram of the equalized image')
plt.title('Histogram of the equalized image')
plt.show()

res = np.hstack((img, equ))
plt.axis('off')
plt.imshow(img, cmap='gray')
plt.imshow(res, cmap='gray')
