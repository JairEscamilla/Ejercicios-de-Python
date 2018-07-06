'"Multiplicacion de matrices"'
a = [[1, 0, 2], [2, 3, -1], [-1, 0, 3]]
b = [[1, 2, 3], [7, 4, -2], [6, -10, -5]]
c = [[0 for i in range(3)] for y in range(3)]
d = [[0 for i in range(3)] for y in range(3)]
for i in range(3):
    for j in range(3):
        for k in range(3):
            c[i][j]+= a[i][k]*b[k][j]
print("A*B=", c)

for i in range(3):
    for j in range(3):
        for k in range(3):
            d[i][j]+= b[i][k]*a[k][j]
print("B*A=", d)
