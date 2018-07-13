from math import sqrt
def leer_coeficientes():
    list = []
    with open("coeficientes.dat", "r") as coeficientes:
        for i in coeficientes:
            val = int(i)
            list.append(val)
    return list
def calcula(lista):
    print (lista)
    a = lista[0]
    b = lista[1]
    c = lista[2]
    d = lambda a, b, c: ((b*b))-(4*a*c)
    discriminante = d(a, b, c)
    if discriminante > 0:
        return 1
    elif discriminante == 0:
        return 0
    else:
        return -1
def mayor(a, b, discriminante):
    x1 = ((-b)-sqrt(discriminante))/2*a
    x2 = ((-b)+sqrt(discriminante))/2*a
    resultados = []
    resultados.append(x1)
    resultados.append(x2)
    return resultados
def igual(a, b):
    x = (-b)/2*a
    return x
def menor():
    return "No tiene solucion"
def despliega(resultado):
    print("El resultado es", resultado)
    with open("raices.dat", "w") as resultados:
        resultados.write("Raices de la ecuacion de segundo grado con coeficientes a, b, c")
        resultados.write("\n")
        resultados.write(str(resultado))
    print("Se ha escito en el archivo")
coeficientes = leer_coeficientes()
discriminante = calcula(coeficientes)
d = lambda a, b, c: ((b*b))-(4*a*c)
dis = d(coeficientes[0], coeficientes[1], coeficientes[2])
if discriminante == 1:
    resultado = mayor(coeficientes[0], coeficientes[1], dis)
elif discriminante == 0:
    resultado = mayor(coeficientes[0], coeficientes[1])
else:
    resultado = menor()

despliega(resultado)
