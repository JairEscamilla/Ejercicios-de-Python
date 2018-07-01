# Algortimo de ordenamiento de burbuja
precio = []
for articulo in range(10):
    print("Dame el precio del articulo: ")
    n= float(input())
    precio.append(n)

hay_cambio = True

while hay_cambio:
    hay_cambio = False
    for articulo in range(len(precio)-1):
        if precio[articulo] > precio[articulo+1]:
            temp = precio[articulo]
            precio[articulo] = precio[articulo+1]
            precio[articulo+1] = temp
            hay_cambio =  True
print("El vector ordenado es: ")
for articulo in range(10):
    print(precio[articulo])
