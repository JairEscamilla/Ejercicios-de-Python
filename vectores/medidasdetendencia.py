# Varianza y desviacion estandar
suma = 0
vector = [None]*5
from math import sqrt
var = 0
desv = 0
# Lee el vector y realiza la suma
for cont in range(5):
    print ("Dame un elemento: ")
    vector[cont]= int(input())
    # Realiza la suma
    suma+= vector[cont]

# Calcula el promedio
pr = suma/5
# Calcula la varianza
for k in range(5):
    var = var+pow(vector[k]-pr, 2)
    var = var/5
    # Calcula la desviacion estandar
    desv = sqrt(var)
print ("Varianza, Desv. Est")
print (var, desv)
