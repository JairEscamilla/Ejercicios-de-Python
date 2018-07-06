a = [[4, 8, 2], [2, -2, -1], [6, 7, 3]]
b = [[-1, 10, 4], [12, 0, -8], [-26, 20, 24]]
c = [[-1, 10, 4], [12, 0, -8], [-26, -20, 24]]
res = [[0 for i in range(3)] for x in range(3)]
for i in range(3):
    for j in range(3):
        for k in range(3):
            res[i][j]+= a[i][k]*b[k][j]

print(res)
