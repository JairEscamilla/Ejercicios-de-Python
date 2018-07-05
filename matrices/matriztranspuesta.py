a = [[-1, 0, -10], [3, 4, 0.5], [6, -23, 8], [7, 3, 9]]
a_transp = [[None, None, None, None], [None, None, None, None], [None, None, None, None]]
# Se genera la transpuesta
for j in range(len(a)):
    for k in range(len(a[0])):
        a_transp[k][j] = a[j][k]

# Se despliega la transpuesta
for j in range(len(a_transp)):
    print()
    for k in range(len(a_transp[0])):
        print(a_transp[j][k], end=", ")
