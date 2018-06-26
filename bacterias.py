'"Algoritmo que calcula la poblacion de una colonia de bacterias"'
# Se calcula el numero de dias en que la poblacion de una colonia de bacterias se duplica

nd = 1
mo = 10
mmax = int(input("Ingresa la cantidad maxima: "))
while mo <= mmax:
    mo = 2*mo
    if mo <= mmax:
        nd+= 2
print "El numero de dias es:", nd
print "La poblacion es:", mo
