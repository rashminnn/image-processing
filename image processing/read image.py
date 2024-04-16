# Displaying with matplotlib
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('images/0001.jpg', cv.IMREAD_COLOR)
img1 = cv.cvtColor(img, cv.COLOR_BGR2RGB)
fig, ax = plt.subplots(1, 2)
ax[0].imshow(img)
ax[0].set_title('Rashmin without converting to RGB')
ax[0].axis('off')
ax[1].imshow(img1)
ax[1].set_title('Rashmin with converting to RGB')
ax[1].axis('off')
plt.show()
