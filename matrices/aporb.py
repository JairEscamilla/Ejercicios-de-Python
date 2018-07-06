a = [[2, 1, 0], [9, -4, 11], [16, 5, -8]]
b = [[10], [-3], [17]]
res = [[0], [0], [0]]
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            res[i][j]+= a[i][k]*b[k][j]
print(res)
