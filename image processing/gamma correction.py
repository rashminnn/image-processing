# gamma correction

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img_org = cv.imread('images/0001.jpg', cv.IMREAD_COLOR)
gamma = 2

table = np.array([((i / 255.0) ** (1 / gamma)) *
                 255 for i in np.arange(0, 256)]).astype("uint8")

img_gamma = cv.LUT(img_org, table)
img_org = cv.cvtColor(img_org, cv.COLOR_BGR2RGB)
img_gamma = cv.cvtColor(img_gamma, cv.COLOR_BGR2RGB)
f, axarr = plt.subplots(3, 2)
axarr[0, 0].imshow(img_org)
axarr[0, 1].imshow(img_gamma)
color = ('b', 'g', 'r')
for i, c in enumerate(color):
    hist_org = cv.calcHist([img_org], [i], None, [256], [0, 256])
    axarr[1, 0].plot(hist_org, color=c)
    hist_gamma = cv.calcHist([img_gamma], [i], None, [256], [0, 256])
    axarr[1, 1].plot(hist_gamma, color=c)

axarr[2, 0].plot(table)
axarr[2, 0].set_xlim([0, 256])

plt.show()
