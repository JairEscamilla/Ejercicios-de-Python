'"Algoritmo que genera una matriz triangular"'
from random import randint
op = int(input("Tipo de matriz (1: inferior, 2: superior)=> "))
x = int(input("Ingresa las filas=> "))
y = int(input("Ingresa las columnas=> "))
matriz = [[0 for i in range(y)] for j in range(x)] # Genera la matriz
for i in range(x): # Llenamos la diagonal principal
    matriz[i][i] = randint(1, 9)
if op == 1:
    for i in range(x):
        pos = i
        for j in range(y):
            if j > pos:
                matriz[i][j] = randint(1, 9)
else:
    for i in range(x):
        pos = i
        for j in range(y):
            if j < pos:
                matriz[i][j] = randint(1, 9)
print()
print("La matriz resultante es: ")
for renglon in matriz:
    print()
    for columna in renglon:
        print(columna, end=", ")
print()
print()
