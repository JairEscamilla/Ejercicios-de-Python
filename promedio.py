no_est = int(input("Numero de alumnos: "))
no_califs = int(input("Numero de calificaciones por alumno: "))
for cont_est in range(no_est):
    print "Nombre"
    nombre = raw_input()
    cont = 1
    sum = 0.0
    while cont <= 6:
        calif = float(input("Dame la calificacion"))
        sum = sum + calif
        cont += 1
    promedio = sum/3.0
    print "El promedio de",nombre, "es", promedio
