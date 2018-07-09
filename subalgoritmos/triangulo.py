'"Algoritmo que obtiene el perimetro de un triangulo con las coordenadas de sus vertices"'
from math import sqrt
def dist(p1, p2):
    distancia = ((p1[0]-p2[0])**2+(p1[1])-p2[1]**2)**0.5
    return distancia
def leer_coordenadas(i):
    p = []
    print("Dame las coordenadas de x del punto", i)
    x = float(input())
    p.append(x)
    print("Dame las coordenadas de y del punto", i)
    y = float(input())
    p.append(y)
    return p
# NOTE: PROGRAMA PRINCIPAL
A = leer_coordenadas(1)
B = leer_coordenadas(2)
C = leer_coordenadas(3)
perimetro = dist(A, B) + dist(B, C) + dist(C, A)
print("El perimetro es", perimetro)
