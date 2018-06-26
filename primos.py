from math import *
# Dado un numero entero positivo, determinar si es primo
n = int(input("Ingresar numero: "))
divisor = 2 # Se inicia en 2 y llegara hasta la raiz de n
while divisor <= sqrt(n):
    cociente = n/divisor # Verifica con cada divisor posible
    if n == cociente *divisor:
        divisor = n + 1 # Se termina porque fue divisible
    else:
        divisor = divisor + 1 # Tal vez sea primo, verificar el siguiente
if divisor > n:
    print "No es primo"
else:
    print "Es primo"
