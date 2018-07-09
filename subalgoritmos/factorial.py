def factorial(n):
    fact = 1 # Se declaran las variables y se inicializa fact a 1
    for k in range(2, n+1):
        fact = fact*k
    return fact
# NOTE: Programa principal
numero = int(input("Ingresar numero entero: "))
factor = factorial(numero)
# Se despliega el factorial
print("El factorial es", factor)
