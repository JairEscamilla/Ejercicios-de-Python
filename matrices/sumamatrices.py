a = [[7, 3], [2, -6], [6, 7]]
b = [[1, 2], [9, -5], [-4, 7]]
# Inicializa la matriz resultado de dimensiones 3*2
c = [[0, 0], [0, 0], [0, 0]]
for k in range(len(a)): # Itera los renglones
    for j in range(len(a[0])): # Itera las columnas
        c[k][j] = a[k][j] + b[k][j]

print(c) # Despliega el resultado        
