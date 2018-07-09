def factorial(n):
    fact = 1
    if n > 1:
        fact = n*factorial(n-1)
    else:
        fact = 1
    return fact
# NOTE: Programa principal
numero = int(input("Ingresar numero entero: "))
factor = factorial(numero)
# Se despliega el factorial
print("El factorial es", factor)
