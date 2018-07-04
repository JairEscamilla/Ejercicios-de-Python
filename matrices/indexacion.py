'"Genera una matriz de n*m"'
a = [] # Se establece el array
m = 5
n = 4
for i in range(m):
    a.append([]) # Se genera un renglon
    for j in range(n):
        a[i].append(None) # Genera cada uno de los elementos

for k in range(m):
    print() # Salto de de renglon
    for j in range(n):
        print(a[k][j], ", ")
