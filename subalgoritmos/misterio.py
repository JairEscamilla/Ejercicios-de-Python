def misterio(n):
    t = 0
    for i in range(1, 4):
        m = n*i
        print(n, "x", i, "son", m)
        t = t+m
    return t
# NOTE: PROGRAMA PRINCIPAL
num = int(input("Numero: "))
print("El resultado es", misterio(num))
