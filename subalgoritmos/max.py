'"Maximo comun divisor"'
a = int(input("Numero mayor: "))
b = int(input("Numero menor: "))
for k in range(b, 1, -1):
    if a%k == 0 and b%k == 0:
        print("El maximo comun divisor es", k)
        break
