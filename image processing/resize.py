# resize an Image

import cv2 as cv

img = cv.imread("images/0001.jpg", cv.IMREAD_ANYCOLOR)
assert img is not None

img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
img = cv.resize(img, (1280, 720), interpolation=cv.INTER_AREA)
cv.imshow("img", img)
cv.waitKey(0)
cv.destroyAllWindows()
