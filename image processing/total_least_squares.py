import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# generate noisy data
n = 20  # number of points
x = np.random.randn(n)
y = np.random.randn(1)*x  # line with zero intercept
y = y + 0.1*np.random.randn(n)  # add noisy points

# total least squares estimation

x = np.stack((x, y), axis=1)
l, v = np.linalg.eig(x.T@x)
idx = l.argsort()[::-1]  # sort eigen values largest to smallest
u11 = v[:, idx[-1]]  # smallest eigen value
u12 = np.array((u11[1], -u11[0]))  # rotate normal vector by 90

plt.plot(x, y, 'bo')
plt.plot([np.min(x[:, 0]), np.max(x[:, 0])],
         [np.min(x[:, 0]) * u12[1] / u12[0],
          np.max(x[:, 0]) * u12[1] / u12[0]],
         color='red')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Total Least Squares Line')
plt.grid(True)
plt.show()
