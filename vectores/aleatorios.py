import random
x = [None]*10
min = 50; max= 100
for i in range(10):
    x[i]= min+max*random.random()%(max-min+1)
    print (x[i])
