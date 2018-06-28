a= int(input("Ingresar a=> "))
b= int(input("Ingresar b=> "))
if a > b:
    print ("El mayor es a")
else:
    sum = 0
    for i in range(a, b):
        sum+= i
    print (sum)
