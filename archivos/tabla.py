datos = [[1.2, 3.0, -7,45],
         [-8.3, 6, 17.563],
         [98.78, -12.5, -46.2332],
         [2, -567.2, 8.43],
         [1, 0, 1.2013]]
tabla = open("tabla.dat", "w")
for renglon in datos:
    for columna in renglon:
        tabla.write("%14.8f" %columna)
    tabla.write("\n")
tabla.close()
