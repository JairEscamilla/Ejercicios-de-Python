import csv
import pprint
archivo = open("datosExcel.csv", "r")
tabla = []
for renglon in csv.reader(archivo):
    tabla.append(renglon)
archivo.close()
pprint.pprint(tabla)
renglon = [0.0]*len(tabla[0])
renglon[0] = "Promedios"
for c in range(1, len(renglon)):
    s = 0
    for r in range(1, len(tabla)):
        s+= float(tabla[r][c])
    renglon[c] = s/3
    print(renglon)

salida = open("promedio_anual.csv", "w")
for k in range(0, len(tabla[0])):
    salida.write(str(tabla[0][k]))
    salida.write(",")
    salida.write("\n")
    salida.write(str(renglon))
salida.close()
