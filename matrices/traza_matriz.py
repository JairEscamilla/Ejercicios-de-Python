'"Algoritmo que genera una matriz triangular"'
from random import randint
x = int(input("Ingresa las filas=> "))
y = int(input("Ingresa las columnas=> "))
matriz = [[0 for i in range(y)] for j in range(x)] # Genera la matriz
for i in range(x):
    matriz[i][i] = randint(0, 9) # Llenamos la diagonal principal
sum = 0
for j in range(x):
    for k in range(y):
        if j == k:
            sum+= matriz[j][k]
print("La matriz es: ")
for renglon in matriz:
    print()
    for columna in renglon:
        print(columna, end=", ")
print()
print()
print("La sumatoria es ", sum)
