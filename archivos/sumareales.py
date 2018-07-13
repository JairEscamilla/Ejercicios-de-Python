import csv
suma = 0
lista = []
with open("reales.txt", "r") as numeros:
    for renglon in numeros:
        dato = float(renglon)
        lista.append(dato)
        suma+= dato
    lista.append(suma)
with open("suma.dat", "w") as suma:
    suma.write(str(lista))
print("Hemos terminado")

# NOTE: PASAMOS A CSV
id = open("suma.csv", "w")
write = csv.writer(id)
write.writerow(lista)
id.close()
print("Segundo proceso terminado")
