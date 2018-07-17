# NOTE: Inicio de la clase
class OperacionMatrices:
    def _verificarMatriz(self, matriz):
        '"Se verifica que cada fila de la matriz sea una lista"'
        if type(matriz) == list and len(matriz) > 0:
            '"Se verifica que exista la misma cantidad de elementos por fila en la matriz"'
            if len(set(len(x) for x in matriz)) != 1:
                return False
            for x in matriz:
                if type(x) == list and len(x) > 0:
                    '"Se verifica que todos los elementos sean de tipo entero o flotante en la matriz"'
                    if all((isinstance(valor, int) or isinstance(valor, float)) for valor in x) != True:
                        return False
                else:
                    return False
            return True
        else:
            return False

    def _verificarSuma(self, matriz1, matriz2):
        # Se verifica que ambas estructuras sean matrices
        if (self._verificarMatriz(matriz1) != True) or (self._verificarMatriz(matriz2) != True):
            return False
        else:
            '"Se verifica que las matricessean de la misma dimension"'
            if len(matriz1) != len(matriz2):
                return False
            else:
                '"Se verifica que ambas matrices tengan la misma cantidad de elementos por fila"'
                for x, y in zip(matriz1, matriz2):
                    if len(x) != len(y):
                        return False
        return False

    def _verificarMultiplicacion(self, matriz1, matriz2):
        # Se verifica que ambas estructuras sean matrices
        if (self._verificarMatriz(matriz1) != True) or (self._verificarMatriz(matriz2) != True):
            return False
        else:
            '"Se verifica que el numero de columnas de la matriz 1 sea igual al numero de renglones de la matriz 2"'
            if len(matriz1[0]) == len(matriz2):
                return True
            else:
                return False
    # Metodo que implementa la suma de matrices
    def sumaMatrices(self, matriz1, matriz2):
        # Se verifica que ambas estructuras sean matrices
        if self._verificarSuma(matriz1, matriz2) == False:
            print("No se puede reailzar la operacion con matrices")
            return []
        else:
            resultado = []
            for x in range(len(matriz1)):
                resultado.appen([])
                for y in range(len(matriz2[0])):
                    resultado[x].append(matriz1[x][y] + matriz2[x][y])
            return resultado

    # Metodo que implementa la multiplicacion de matrices
    def multiplicacionMatrices(self, matriz1, matriz2):
        if self._verificarMultiplicacion(matriz1, matriz2) ==  False:
            print("No se puede realizar la operacion con matrices")
            return []
        else:
            resultado = []
            for x in range(len(matriz1)):
                resultado.append([])
                for y in range(len(matriz2[0])):
                    res = 0
                    for z in range(len(matriz2)):
                        res = res + matriz1[x][z]*matriz2[z][y]
                resultado[x].append(res)
            return resultado

operaciones = OperacionMatrices()
lista1 = [[3, 2, 1, 9], [-1, -3, 0, 8], [5, 7, 8, 7]]
print("Matriz1: ")
print(lista1)
lista2 = [[9, 0, 1, 3], [-1, 7, 1, 4], [6, 4, 1, 6]]
print("Matriz2: ")
print(lista2)
lista3 = [[3, 2, 1], [-1, -3, 0], [5, 7, 8]]
print("Matriz3: ")
print(lista3)
lista4 = [[9, 0, 1], [-1, 7, 1], [6, 4, 1]]
print("Matriz4: ")
print(lista4)

print("Suma de la matriz 1 y 2: ")
print(operaciones.sumaMatrices(lista1, lista2))


print("Multiplicacion de la matriz 3 y 4: ")
print(operaciones.multiplicacionMatrices(lista3, lista4))

print("Multiplicacion de la matriz 1 y 4: ")
print(operaciones.multiplicacionMatrices(lista1, lista4))
