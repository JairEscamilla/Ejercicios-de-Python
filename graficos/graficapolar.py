from numpy import pi, arange, linspace
from matplotlib.pyplot import subplot, plot, show, grid, title
teta = arange(0, 3, 0.01) # Se generan los valores de tetha
r = 2*pi*teta # Se calcula r para cada valor de tetha
subplot(111, polar = True )
plot(r, teta, color ="r", linewidth = 3)
grid(True)
title("Grafica polar de r = 2$\pi\\theta$")
show()
