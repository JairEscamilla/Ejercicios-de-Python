dos = []
cuatro = []
x = lambda i: 2*i
y = lambda i: 4*i
for i in range(1, 11):
    dos.append(x(i))
    cuatro.append(y(i))
print("Las tablas son:\n", dos, "\n", cuatro)
