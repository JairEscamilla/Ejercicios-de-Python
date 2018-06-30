print("Escriba 4 palabras: ")
palabras= []
for i in range(4):
    n = str(input())
    palabras.append(n)

for y in range(4):
    a = "*"*len(palabras[y])
    print(palabras[y]+" "+a)
