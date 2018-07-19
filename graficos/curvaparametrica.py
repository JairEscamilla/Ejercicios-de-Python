from mpl_toolkits.mplot3d import Axes3D
from matplotlib.pyplot import title, figure, show, plot, legend
from numpy import *
a = figure()
a.gca(projection = "3d")
teta = linspace(-4 * pi, 4 * pi, 100)
r = linspace(0, pi, 100)
z = r
x = r * sin(teta)
y = r * cos(teta)
plot(x, y, z, label = "Curva parametrica")
legend()
show()
