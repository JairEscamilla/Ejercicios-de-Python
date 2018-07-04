a = [[3, 2, 1], [-1, -3, 0], [5, 7, 8]]
b = [[9, 0, 1], [-1, 7, 1], [6, 4, 1]]
c = [[0 for i in range(3)] for j in range(3)]
for k in range(len(a)):
    for x in range(len(b[0])):
        for t in range(len(b)):
            c[k][x] += a[k][t]*b[t][x]
print(c)        
