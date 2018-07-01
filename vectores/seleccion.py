# Algoritmo de ordenamiento por seleccion
calif = [None]*6
for estudiante in range(6):
    print("Dame las calificaciones: ")
    calif[estudiante]= float(input())

for i in range(6):
    min = 0
    for x in range(i, 6):
        if calif[i]>calif[x]:
            min = calif[i]
            calif[i]=calif[x]
            calif[x]=min


print("El orden es: ")
print(calif)
