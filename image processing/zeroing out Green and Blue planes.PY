# zeroing out Green and Blue planes

import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np


img = cv.imread("images/0001.jpg", cv.IMREAD_ANYCOLOR)
assert img is not None

img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(img)
plt.title("Original Image")
plt.xticks([]), plt.yticks([])
plt.show()

img[:, :, 0:2] = 0
plt.imshow(img)
plt.title("Zeroed out Green and Blue planes")
plt.xticks([]), plt.yticks([])
plt.show()
