'"Algoritmo que obtiene el valor de sen (x) con la serie de Taylor"'
from math import *
def factorial(n):
    fact = 1 # Inicializamos el valor del factorial
    for i in range(n):
        fact = fact*i
    return fact
# NOTE: PROGRAMA PRINCIPAL
# Se escribe el valor de x
x = float(input("Valor de x: "))
s = 0.0 # Inicializacion de la sumatoria
for i in range(1, 11):
    s+= pow(-1.0, i)*pow(x, (2*i+1))/factorial(2*i+1)
print(s)
