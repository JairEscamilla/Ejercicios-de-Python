# Promedio de calificaciones
suma = 0; notas = [None]*20
print ("Numero de alumnos: ")
n = int(input())
for i in range(n):
    print ("Alumno", i+1, "Nota: ")
    notas[i] = float(input())
for i in range(n):
    suma+= notas[i]
media = suma/n
print("Nota media:", media)
print("Notas superiores: ")
for i in range(n):
    if notas[i] > media:
        print("Alumno numero", i+1)
        print("Nota: ", notas[i])
