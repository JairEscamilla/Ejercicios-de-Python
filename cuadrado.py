'"Algoritmo que dibuja un cuadrado con las dimensiones dadas"'
n = int(input("Escribe la dimension n>= 2=> "))
# Escribe la primera linea de asteriscos
for i in range(n):
    print "*",
print ""
# Dibuja las partes laterales
for x in range(n-2):
    for y in range(n):
        if y == 0 or y == n-1:
            print "*",
        else:
            print " ",
    print ""

# Dibuja el lado inferior
for d in range(n):
    print "*",
