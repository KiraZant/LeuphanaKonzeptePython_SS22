import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d.axes3d import Axes3D  # noqa

# Funktion erstellen
x, y = np.meshgrid(np.linspace(-4, 4, 1000), np.linspace(-8, 8, 1000))
z = -np.power(x, 3) + np.power(y, 2) + 12 * x - 6 * y - 5

fig = plt.figure(figsize=(8, 4))

ax1 = fig.add_subplot(1, 2, 1, projection='3d')
p = ax1.plot_surface(x, y, z, rstride=4, cstride=4, linewidth=0, cmap='inferno')
ax1.view_init(azim=-60, elev=30)
ax1.set(xlabel='x', ylabel='y')

ax2 = fig.add_subplot(1, 2, 2)
CS = ax2.contour(x, y, z, 20, cmap='coolwarm_r')  # colormaps()
ax2.clabel(CS, inline=1)
ax2.set(xlabel='x', ylabel='y')
ax2.grid(True)
plt.show()
