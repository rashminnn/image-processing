# increasing the brightness using opencv

import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('images/0001.jpg', cv.IMREAD_GRAYSCALE)
imgb = img+100
imgc = cv.add(img, 100)

fig, ax = plt.subplots(1, 3)
ax[0].imshow(img, cmap='gray')
ax[0].set_title('Original')
ax[1].imshow(imgb, cmap='gray')
ax[1].set_title('Increased Brightness')
ax[2].imshow(imgc, cmap='gray')
ax[2].set_title('Increased Brightness')
plt.show()
