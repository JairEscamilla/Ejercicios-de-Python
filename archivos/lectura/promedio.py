archivo = open("enteros.dat")
suma = 0
cuenta = 0
for renglon in archivo:
    dato = int(renglon)
    suma+= dato
    cuenta+= 1
promedio = float(suma/cuenta)
archivo.close()
print("Promedio-> ", promedio)
