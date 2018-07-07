from random import *
matriz = [[0 for i in range(4)] for x in range(4)]
for k in range(4):
    matriz[k][k] = randint(0, 100)
for renglon in matriz:
    print()
    for columna in renglon:
        print(columna, end=", ")
print()
