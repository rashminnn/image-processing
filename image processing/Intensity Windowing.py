# Intensity Windowing

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

c = np.array([(100, 50), (150, 200)])
t1 = np.linspace(0, c[0, 1], c[0, 0]+1).astype(np.uint8)
print(len(t1))
t2 = np.linspace(c[0, 1]+1, c[1, 1], c[1, 0]-c[0, 0]).astype(np.uint8)
print(len(t2))
t3 = np.linspace(c[1, 1]+1, 255, 255-c[1, 0]).astype(np.uint8)
print(len(t3))

transform = np.concatenate((t1, t2), axis=0).astype(np.uint8)
transform = np.concatenate((transform, t3), axis=0).astype(np.uint8)
print(len(transform))

fig, ax = plt.subplots()
ax.plot(transform)
ax.set_xlabel(r'Input, $f(\mathbf{x})$)')
ax.set_ylabel(r'Output, $T(f(\mathbf{x}))$')
ax.set_title('intensity Transformation')
ax.set_xlim(0, 255)
ax.set_ylim(0, 255)
ax.set_aspect('equal')
plt.show()

img_orig = cv.imread('images/kella.jpg', cv.IMREAD_GRAYSCALE)
cv.namedWindow('image')
cv.imshow('image', img_orig)
cv.waitKey(0)
img_trans = cv.LUT(img_orig, transform)
cv.namedWindow('image_trans')
cv.imshow('image_trans', img_trans)
cv.waitKey(0)
cv.destroyAllWindows()
