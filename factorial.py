fact = 1
n = int(input("Dame el valor entero: "))
# Se inicia el calculo del factorial
for i in range(2, n+1):
    fact*= i
print "El factorial es", fact
