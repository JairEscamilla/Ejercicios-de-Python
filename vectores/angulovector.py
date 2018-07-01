from math import *
x = [3, 4, 5]
y = [-2, -1, 6]
res = [(x[i]*y[i]) for i in range(len(x))]
xy = 0
for i in range(len(x)):
    xy += res[i]
magx = 0
magy = 0
for d in range(len(x)):
    magx+= pow(x[d], 2)
    magy+= pow(y[d], 2)

mx = sqrt(magx)
my = sqrt(magy)

tetha = acos((xy)/(mx*my))
print("El angulo formado por los vectores es", tetha, "grados")
