def recibir():
    n = int(input("Ingresar numero: "))
    return n
def checar(n):
    if n % 2 == 0:
        return True
    else:
        return False
def buscar(n):
    primos = []
    num = 1
    sum = 0
    numeros = []
    # NOTE: Obtenemos los numeros primos
    while sum <= 4*n:
        c = 0
        contador = 0
        num+= 1
        while c <= num:
            c+= 1
            if num%c == 0:
                contador+= 1
        if contador == 2:
            sum+= num
            primos.append(num)
    # NOTE: Comenzamos a hacer la busqueda
    for i in range(len(primos)):
        for j in range(len(primos)):
            if primos[i]+primos[j] == n:
                numeros.append(primos[i])
                numeros.append(primos[j])
                break
            else:
                continue
        if len(numeros) > 0:
            break
    return numeros
numero = recibir()
revision = checar(numero)
if revision:
    n = buscar(numero)
    print("Los numeros son", n[0], "y", n[1])
else:
    print("El numero no es par")
