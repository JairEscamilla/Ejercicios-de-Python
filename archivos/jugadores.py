archivo = open("jugadores2.txt", "w")
datos = ["Peres \t 12\n", "Mario \t 13\n"]
archivo.writelines(datos)
a = 3.2316
archivo.write("%s" %a)
archivo.close()
