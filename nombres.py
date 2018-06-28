nombres = []
nombre = "default"
while True:
    nombre = str(input("Ingresar nombre: "))
    if nombre in nombres:
        break
    nombres.append(nombre)
