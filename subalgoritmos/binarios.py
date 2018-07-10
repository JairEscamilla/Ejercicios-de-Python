'"Algoritmo para convertir de decimal a binario"'
def leer(): # Lee el numero
    print("Dame el numero a convertir: ")
    numero = int(input())
    return numero
def dividir(numero): # NOTE: Realiza las divisiones
    binario = []
    cociente = numero
    while cociente > 0:
        residuo = cociente%2
        cociente = cociente//2
        binario.append(residuo)
    return binario
def desplegar(binario):
    binario = list(reversed(binario))
    print("El resultado es", binario)
# NOTE: PROGRAMA PRINCIPAL
numero = leer()
binario = dividir(numero)
desplegar(binario)
