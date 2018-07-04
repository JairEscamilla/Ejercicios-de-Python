a = [[9, 12, -44], [16, 7, 14], [23, 61, 84], [-2, -54, 60]]
k = int(input("Ingresar columna a obtener: "))
b = []
print()
for i in range(len(a)):
    b.append(a[i][k])
print(b)
