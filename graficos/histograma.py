from matplotlib.pyplot import *
from numpy.random import normal
numeros = normal(size = 1000)
hist(numeros)
title("Grafica de histograma")
show()
