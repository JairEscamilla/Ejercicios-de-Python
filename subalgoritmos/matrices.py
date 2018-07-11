def inicializa():
    array = [[0 for i in range(2)] for x in range(3)]
    return array
def cambia(array):
    from random import randint
    for i in range(3):
        for j in range(2):
            array[i][j] = randint(1, 9)
    return array
def transpuesta(array):
    transpuesta = [[0 for i in range(3)] for x in range(2)]
    for i in range(3):
        for j in range(2):
            transpuesta[j][i] = array[i][j]
    return transpuesta
def mostrar(matriz):
    for renglon in matriz:
        print()
        for columna in renglon:
            print(columna, end="")
array = inicializa()
array = cambia(array)
transpuesta = transpuesta(array)
mostrar(transpuesta)
print()
