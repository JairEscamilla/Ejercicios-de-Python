import csv
a = [[1, 2, 3], ["cafe", "azucar", "crema"], [12.50, 18.01, 16.54]]
iden = open("ejemplo2.csv", "w")
escribir = csv.writer(iden)
for renglon in a:
    escribir.writerow(renglon)
iden.close()
