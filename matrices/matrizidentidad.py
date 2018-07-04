'"Matriz identidad de 4*4"'
# Una matriz identidad es aquella en la que los elementos de la diagonal
# princiál es = 1.  Los elementos sonaquellos donde los indices son iguales.
# Es decir a[K][k]
i = [[0 for k in range(4)] for j in range(4)] # Se genera la matriz de 0

# Los elementos de la diagonal principal se hacen la unidad.
for k in range(4):
    i[k][k]= 1

# Para desplegar la Matriz
for k in range(4):
    print() # Para salto de renglon
    for j in range(4):
        print(i[k][j], end=", ")
print()
