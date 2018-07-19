from pylab import *
xmax = 2.0
xmin = -xmax
NX = 5
ymax = 2.0
ymin = -ymax
NY = 5
# Componentes vectoriales y puntos
x = linspace(xmin, xmax, NX)
y = linspace(ymin, ymax, NY)
X, Y = meshgrid(x, y)
S2 = X**2 + Y**2 # Este es el radio al cuadrado

# Campo magnetico
Bx = -Y/(S2 +0.001)
By = +X/(S2 +0.001)

figure()
QP = quiver(X, Y, Bx, By)
quiverkey(QP, 0.85, 0.85, 1.0, "Campo magnetico")

# Limites de los ejes
dx = (xmax - xmin)/(NX-1)
dy = (ymax - ymin)/(NX-1)
axis([xmin - dx, xmax + dx, ymin - dy, ymax + dy])
title("Campo magnetico de un alambre con corriente")
xlabel("x (cm)")
ylabel("y (cm)")
show()
