import csv
print("\n Transformada Discreta de Fourier \n de una señal. ")
nombre = input("\ nombre de archivo de salida (sin extension) =>")
f = open(nombre + ".csv", "w")
obj = csv.writer(f, delimiter = ' ', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
obj.writerow (abs(resultado[im]))
f.close()
