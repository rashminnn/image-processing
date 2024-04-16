# spetial filtering
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('images/0001.jpg', cv.IMREAD_REDUCED_GRAYSCALE_2)

kernel = np.ones((8, 8), np.float32)/64
kernel_sob = np.array([(-1, -2, -1), (0, 0, 0), (1, 2, 1)])
kernel_hor = np.array([(-1, 0, 1), (-2, 0, 2), (-1, 0, 1)])
sober5 = np.array([(-1, -2, 0, 2, 1), (-2, -3, 0, 3, 2),
                  (-3, -5, 0, 5, 3), (-2, -3, 0, 3, 2), (-1, -2, 0, 2, 1)])

imgc = cv.filter2D(img, -1, kernel)
imgd = cv.filter2D(img, -1, kernel_sob)
imge = cv.filter2D(img, -1, kernel_hor)
imgf = cv.filter2D(img, -1, sober5)

print(kernel_sob)
print(kernel)
print(kernel_hor)
print(sober5)

fig, ax = plt.subplots(1, 5, figsize=(15, 10))
ax[0].imshow(img, cmap='gray', vmin=0, vmax=255)
ax[1].imshow(imgc, cmap='gray', vmin=0, vmax=255)
ax[2].imshow(imgd, cmap='gray', vmin=0, vmax=255)
ax[3].imshow(imge, cmap='gray', vmin=0, vmax=255)
ax[4].imshow(imgf, cmap='gray', vmin=0, vmax=255)

plt.show()
