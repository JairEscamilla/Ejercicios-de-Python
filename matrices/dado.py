import random
tabla = []
min = 1
max = 6
for r in range(3):
    tabla.append([])
    for t in range(6):
        tabla[r].append(random.randint(min, max))

# Se despliega la tabla de tiros
for k in range(3):
    print(tabla[k])

for r in range(3):
    tabla[r].append(0)
    for t in range(5):
        tabla[r][5] = tabla[r][5]+tabla[r][t]

vez = [0, 0, 0, 0]
for r in range(3):
    for t in range(5):
        if tabla[r][t] == 6:
            vez[r] = vez[r]+1
for r in range(3):
    if vez[r] == 1:
        print("El jugador", r+1, "obtuvo 6", vez[r], "vez")
    elif vez[r] >= 2:
        print("El jugador", r+1, "obtuvo 6", vez[r], "veces")
    else:
        print("El jugador", r+1, "no obtuvo 6")
    print("Su suma de puntos fue", tabla[r][5])
    print()
