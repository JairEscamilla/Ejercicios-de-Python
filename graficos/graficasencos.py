from numpy import linspace, pi, sin, cos
from matplotlib.pyplot import plot, show, xlim, ylim
from matplotlib.pyplot import legend, xticks
x = linspace(-pi, pi, 256)
y = sin(x)
z = cos(x)
plot(x, y, label = "seno")
plot(x, z, label = "coseno")
legend(loc = "upper left")
ylim(-2, 2)
show()
