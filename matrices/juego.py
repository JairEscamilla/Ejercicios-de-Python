matriz = [["Perro", "Gato"], ["Perico", "Gallo"], ["Lobo", "Perro"], ["Gato", "Perico"], ["Gallo", "Lobo"]]
num = 0
repeat = True
intentos = 0
while repeat:
    print("Ingresa las coordenadas(1): ")
    x1 = int(input())
    y1 = int(input())
    print("Ingresa las coordenadas(2): ")
    x2 = int(input())
    y2 = int(input())
    if matriz[x1][y1] == matriz[x2][y2]:
        print("Lo has logrado, encontraste un par!")
        num+= 1
        print("Encuentra el siguiente par")
    else:
        print("Has fallado): Intentalo de nuevo")

    if num >= 5:
        repeat = False
    intentos+= 1
print("El juego se ha terminado despues de", intentos, "intentos")
