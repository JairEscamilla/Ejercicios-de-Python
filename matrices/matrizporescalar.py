# Multiplicacion de una matriz por escalar rij = k * aij
a = [[2, -1, 7, 3], [12, -26, 4, -8], [-4, -5, 6, 7]]
k = 5
# Matriz resultado
R = [[None for i in range(4)] for j in range(3)]
norenglones = len(a)
nocolumnas = len(a[1])

for renglones in range(norenglones):
    for columnas in range(nocolumnas):
        R[renglones][columnas] = k*a[renglones][columnas]

for r in range(norenglones):
    print() # Salto de renglon
    for c in range(nocolumnas):
        print(R[r][c], end= "")
