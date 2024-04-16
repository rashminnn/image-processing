# increasing brightness using loops

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def image_brighten(image, shift):
    h = image.shape[0]
    w = image.shape[1]
    result = np.zeros(image.shape, image.dtype)
    for i in range(0, h):
        for j in range(0, w):
            result[i, j] = image[i, j] + shift
    return result


def image_brighten2(image, shift):
    h = image.shape[0]
    w = image.shape[1]
    result = np.zeros(image.shape, image.dtype)
    for i in range(0, h):
        for j in range(0, w):
            result[i, j] = min(image[i, j] + shift, 255)
    return result


img = cv.imread('images/0001.jpg', cv.IMREAD_GRAYSCALE)
imgb = image_brighten(img, 50)
imgb2 = image_brighten2(img, 50)

fig, ax = plt.subplots(1, 3)
ax[0].imshow(img, cmap='gray', vmin=0, vmax=255)
ax[0].set_title('Original Image')
ax[1].imshow(imgb, cmap='gray', vmin=0, vmax=255)
ax[1].set_title('Increased Brightness')
ax[2].imshow(imgb2, cmap='gray', vmin=0, vmax=255)
ax[2].set_title('Increased Brightness with clipping')
plt.show()
