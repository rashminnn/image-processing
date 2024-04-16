# color planes in open cv

import cv2 as cv
import matplotlib.pyplot as plt


img = cv.imread("images/0001.jpg", cv.IMREAD_COLOR)
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

b, g, r = cv.split(img)

fig, ax = plt.subplots(1, 3)
ax[0].imshow(r)
ax[1].imshow(g)
ax[2].imshow(b)
plt.show()
