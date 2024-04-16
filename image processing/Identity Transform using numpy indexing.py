# Identity Transform using numpy indexing

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

transform = np.arange(0, 256).astype(np.uint8)
fig, ax = plt.subplots()
ax.plot(transform)
ax.set_xlabel(r'Input, $f(\mathbf{x})$)')
ax.set_ylabel(r'Output, $T(f(\mathbf{x}))$')
ax.set_title('intensity Transformation')
ax.set_xlim(0, 255)
ax.set_ylim(0, 255)
ax.set_aspect('equal')
plt.show()

img_original = cv.imread('images/0001.jpg', cv.IMREAD_GRAYSCALE)
print(img_original.shape)
cv.namedWindow('original', cv.WINDOW_NORMAL)
cv.imshow('original', img_original)
cv.waitKey(0)
img_transformed = transform[img_original]
cv.namedWindow('transformed', cv.WINDOW_NORMAL)
cv.imshow('transformed', img_transformed)
cv.waitKey(0)
cv.destroyAllWindows()
