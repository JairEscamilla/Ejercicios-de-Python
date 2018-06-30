from random import randint
nombre = str(input("Hola, ¿Como te llamas? "))
print ("Muy bien", nombre, "adivina el numero entre 1 y 20")
n = randint(1, 20)
d = int(input())
cont = 1
while d != n:
    cont+= 1
    if d<n:
        print ("Tu numero es muy bajo")
    else:
        print ("Tu numero es muy alto")
    d = int(input("Dame otro numero: "))
print ("Buen trabajo", nombre, "acertaste en", cont, "intentos")
