from random import randint
vector = []
for i in range(20):
    n = randint(1, 100)
    vector.append(n)
for x in range(len(vector)):
    min = 0
    for y in range(x, len(vector)):
        if vector[x] > vector[y]:
            min = vector[y]
            vector[x] = vector[y]
            vector[y] = min
print(vector)
valor = vector[-2]

primero = 1
ultimo = len(vector)
medio = (primero+ultimo)/2
while primero <= ultimo:
    if vector[medio] < valor:
        primero = medio+1
    elif vector[medio] == valor:
        print(valor, "encontrado")
        primero = 2*ultimo
    else:
        ultimo = medio
        medio = (primero+ultimo)/2
if primero>ultimo:
    print("No se ha encontrado el numero")
