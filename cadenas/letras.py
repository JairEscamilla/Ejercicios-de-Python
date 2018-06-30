cadena = str(input("Ingresar la palabra: "))
letras = []
veces = []
for i in cadena:
    if not(i in letras):
        letras.append(i)
        v = cadena.count(i)
        veces.append(v)

for y in range(len(letras)):
    print ("La letra", letras[y], "aparece", veces[y], "veces")
