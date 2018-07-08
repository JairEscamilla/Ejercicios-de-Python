'"Algoritmo que genera una matriz triangular"'
op = int(input("Tipo de matriz (1: inferior, 2: superior)=> "))
x = int(input("Ingresa las filas=> "))
y = int(input("Ingresa las columnas=> "))
matriz = [[0 for i in range(y)] for j in range(x)]
for i in range(x):
    matriz[i][i] = 1
print(matriz)
