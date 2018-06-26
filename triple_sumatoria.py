'"Algoritmo para resolver una triple sumatoria"'
s = 0 # Se inicializa el valor
# Se inician los ciclos anidados
for i in range(11):
    for j in range(5, 10):
        for k in range(-1, 8):
            s+= i*j*k
s+= 23
print s
