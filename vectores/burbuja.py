from random import randint
vector = []
for i in range(15):
    n = randint(1, 100)
    vector.append(n)
for x in range(len(vector)):
    for y in range(len(vector)-1):
        if vector[y] > vector[y+1]:
            aux = vector[y+1]
            vector[y] = vector[y+1]
            vector[y] = aux
print(vector)
