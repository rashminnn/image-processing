import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

im = np.zeros((6, 8, 3), dtype=np.uint8)
im[2, 3] = [0, 0, 255]
im[1, 2] = [255, 0, 0]
im[4, 2] = [0, 255, 0]
fig, ax = plt.subplots()
ax.imshow(im, cmap='gray', vmin=0, vmax=255)
ax.xaxis.tick_top()
plt.show()
