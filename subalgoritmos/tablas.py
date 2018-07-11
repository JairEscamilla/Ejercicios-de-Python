def leer():
    n = int(input("Numero: "))
    return n
def generar(n):
    array = []
    for i in range(1, 11, 1):
        array.append(n*i)
    return array
def imprime(n, array):
    for i in range(len(array)):
        print(n,"*",i,"=", array[i])
n = leer()
array = generar(n)
imprime(n, array)
