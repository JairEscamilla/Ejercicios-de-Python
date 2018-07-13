from random import randint
array = []
for i in range(10):
    array.append(randint(0, 10))
with open("aleatorio.dat", "w") as archivo:
    for i in array:
        archivo.write(str(i))
        archivo.write("\n")
print("El proceso se ha terminado")
