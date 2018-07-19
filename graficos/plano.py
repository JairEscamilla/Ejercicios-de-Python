from pylab import *
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.pyplot import show

fig = figure()
ax = Axes3D(fig)
x = arange(-4, 4, 0.25)
y = arange(-4, 4, 0.25)
x, y = meshgrid(x, y)
R = sqrt(abs(x**3) + y**2)
z = sin(R)
ax.plot_surface(x, y, z, rstride = 1 , cstride = 1, cmap = cm.hot)
ax.contourf(x, y, z, zdir = "z", offset = -2, cmap = cm.hot)
ax.set_zlim(-2, 2)
show()
