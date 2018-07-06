'"Suma y resta de matrices"'
a = [[1, 0, 2], [2, 3, -1], [-1, 0, 3]]
b = [[1, 2, 3], [7, 4, -2], [6, -10, -5]]
suma = [[0 for i in range(3)] for i in range(3)]
resta = [[0 for i in range(3)] for i in range(3)]
for i in range(3):
    for j in range(3):
        suma[i][j] = a[i][j]+b[i][j]

print(a,"+",b,"=",suma)

for i in range(3):
    for j in range(3):
        resta[i][j] = a[i][j]-b[i][j]

print(a,"-",b,"=",resta)
