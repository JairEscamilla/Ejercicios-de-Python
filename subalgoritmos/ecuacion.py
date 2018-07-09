'"Algoritmo que resuelve una ecuacion de segundo grado"'
import math
def discriminante(a1, b1, c1):
    # NOTE: Esta funcion calcula la raiz cuadrada del discriminante
    d = math.sqrt(b1*b1-4*a1*c1)
    return d
# NOTE: PROGRAMA PRINCIPAL

# Se reciben los coeficientes
a = float(input("Dame a: "))
b = float(input("Dame b: "))
c = float(input("Dame c: "))
# Se calcula el discriminante
d1 = discriminante(a, b, c)

# Se calculan las raices y se despliegan
x1 = (-b+d1)/2*a
x2 = (-b-d1)/2*a
print("x1=", x1)
print("x2=", x2)
