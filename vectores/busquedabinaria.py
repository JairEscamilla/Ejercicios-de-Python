n = int(input("Dame el numero de elementos en la lista: "))
print("Dame los valores: ")
vector = []
for c in range(n+1):
    num = int(input())
    vector.append(num)

numero_buscado = int(input("Dame el valor a buscar"))
primero = 1
ultimo = n
medio = (primero+ultimo)/2

while primero <= ultimo:
    if vector[int(medio)] < numero_buscado:
        primero = medio+1
    elif vector[int(medio)] == numero_buscado:
        print(numero_buscado,"encontrado en la posicion", medio)
        primero = 2*ultimo
    else:
        ultimo = medio
        medio = (primero+ultimo)/2

if primero>ultimo:
    print("Numero no encontrado en la lista")
