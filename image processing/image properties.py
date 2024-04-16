# Displaying image properties

import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('images/0001.jpg', cv.IMREAD_COLOR)
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
fig, ax = plt.subplots()
ax.imshow(img)
ax.axis('off')
ax.set_title('Original Image')
plt.show()
print(img.shape)
print(img.dtype)
print(img.size)
# show how many dimensions habe this have 3 dimensions row axis , column axis and color axis
print(img.ndim)
