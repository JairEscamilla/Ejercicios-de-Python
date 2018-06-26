'"Algoritmo para calculo de interes"'
capital = input("Capital: ")
tasa = input("Tasa: ")
n = input("Numero de meses: ")
# interes simple
int_simple = capital*n*tasa
# interes compuesto
int_compuesto = capital*pow(1+tasa, n)
print "Interes simple: ", int_simple
print "Interes compuesto: ", int_compuesto
