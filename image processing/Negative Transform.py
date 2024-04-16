# Negative Transform

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

transform = np.arange(255, -1, -1).astype(np.uint8)
print(transform.shape)
fig, ax = plt.subplots()
ax.plot(transform)
ax.set_xlabel(r'Input, $f(\mathbf{x})$)')
ax.set_ylabel(r'Output, $T(f(\mathbf{x}))$')
ax.set_title('intensity Transformation')
ax.set_xlim(0, 255)
ax.set_ylim(0, 255)
ax.set_aspect('equal')
plt.show()
img_orig = cv.imread('images/0001.jpg', cv.IMREAD_GRAYSCALE)
cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.imshow('image', img_orig)
cv.waitKey(0)
img_transform = cv.LUT(img_orig, transform)
cv.namedWindow('image_transform', cv.WINDOW_NORMAL)
cv.imshow('image_transform', img_transform)
cv.waitKey(0)
cv.destroyAllWindows()
