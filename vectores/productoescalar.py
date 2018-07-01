x = [5, 8, 9, 1, 7, 7, 8, 6]
y = [8, 7, 6, 4, 2, 3, 4, 3]
res = [(x[i]*y[i]) for i in range(len(x))]
sum = 0
for u in range(len(x)):
    sum+= res[u]
print("El resultado es", sum)
