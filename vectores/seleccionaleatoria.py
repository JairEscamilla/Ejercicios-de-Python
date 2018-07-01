from random import randint
vector = []
for i in range(20):
    n = randint(1, 100)
    vector.append(n)
for x in range(len(vector)):
    min = 0
    for y in range(x, len(vector)):
        if vector[x] > vector[y]:
            min = vector[y]
            vector[x] = vector[y]
            vector[y] = min
print(vector)
