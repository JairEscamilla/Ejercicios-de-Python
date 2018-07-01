from math import sqrt
x = [2, -4, 6, -3, -9]
y = [(x[i])**2 for i in range(len(x))]
sum = 0
for i in range(len(x)):
    sum+= y[i]
print(sqrt(sum))
