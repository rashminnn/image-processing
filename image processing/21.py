import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

im = np.ones((300, 400), dtype=np.uint8) * 255
im[:, 150:250] = 0

mean = 0
sigma = 0.05
noise = np.random.normal(mean, sigma, im.shape)
im = im.astype(float) / 255.0

im = cv.add(im, noise) * 255
im = cv.normalize(im, None, 0, 255, cv.NORM_MINMAX)
im = im.astype(np.uint8)

f = im[150, :]
kernel = np.array([-1, 0, 1])
fx = cv.filter2D(f, cv.CV_32F, kernel)

g = cv.getGaussianKernel(11, 5., cv.CV_64F)
fgf = cv.filter2D(f, cv.CV_32F, g)
fgfx = cv.filter2D(fgf, cv.CV_32F, kernel)

fig, ax = plt.subplots(4, figsize=(10, 10))
ax[0].imshow(im, cmap='gray')
ax[1].plot(f)
ax[2].plot(fx)
ax[3].plot(fgfx)

plt.show()
