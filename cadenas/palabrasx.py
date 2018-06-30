print("Escriba 4 palabras: ")
palabras= []
for i in range(4):
    n = str(input())
    palabras.append(n)
for y in range(4):
    n = len(palabras[y])
    for x in range(n):
        print("*")
    print(n)
