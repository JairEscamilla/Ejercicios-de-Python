from matplotlib.pyplot import *
figure(1, figsize = (6, 6))
fracs = [15, 30, 40, 5, 10]
pie(fracs, autopct = "%2.1i%%")
title("Grafica de pie")
show()
