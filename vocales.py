'"Programa que cuenta las vocales de una frase"'
frase = "El perro corre despacio"
base = "aeiouAEIOU"
c = 0
for i in frase: # Para cada caracter de la frase
    if i in base: # Checa si el caracter esta en la palabra
        c+= 1
print "La frase tiene", c, "vocales"
