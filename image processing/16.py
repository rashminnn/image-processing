import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
gamma = [0.2, 0.5, 1, 2, 5]
for g in gamma:
    table = np.array(
        [(i/255.0)**g*255 for i in np.arange(0, 256)]).astype('uint8')
    ax.plot(table, label=r'$\gamma = {g}'.format(g=g))
ax.legend(loc='best')
ax.set_xlim(0, 255)
ax.set_ylim(0, 255)
ax.set_aspect('equal')
ax.set_xlabel('Input , $f(\mathbf{x})')
ax.set_ylabel('Output , $\mathrm{T}[f(\mathbf{x})]$')
ax.set_title('Gamma Correction')
plt.show()
