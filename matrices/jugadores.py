'"Algoritmo que maneja los datos de 10 jugadores"'
datos = []

# Llenamos primero la matriz de datos
for i in range(10):
    datos.append([])
    for j in range(5):
        print("Ingresar datos del jugador numero", i+1,": ")
        data = str(input())
        datos[i].append(data)
# a) Pasen una edad seleccionada por el usuario
edad = str(input("Ingresar la edad para seleccionar jugadores: "))
altura = str(input("Ingresar la altura para seleccionar jugadores: "))
peso = str(input("Ingresar la peso para seleccionar jugadores: "))
cont = 0
cont1 = 0
cont2 = 0
for renglon in datos:
    if renglon[1] > edad:
        cont+= 1
    if renglon[2] > altura:
        cont1+= 1
    if renglon[3] > altura:
        cont2+= 1
print("Hay", cont, "jugadores que sobrepasan la edad")
print("Hay", cont1, "jugadores que sobrepasan la altura")
print("Hay", cont2, "jugadores que sobrepasan el peso")
