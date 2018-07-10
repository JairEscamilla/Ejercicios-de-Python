'"Algoritmo que obtiene las cotizaciones de dolar y euro"'
def mayor(n, x):
    mayor = 0 # Se inicializa el mayor
    for k in range(n):
        if x[k] > mayor:
            mayor = x[k]
    return mayor
def promedio(n, x):
    suma = 0 # Se inicializa la sumatoria
    for k in range(n):
        suma = suma+x[k]
    promedio = suma/n
    return promedio
# NOTE: PROGRAMA PRINCIPAL
# Vector de los dias de la semana
semana = ["lunes", "martes", "miercoles", "jueves", "viernes"]
# Inicializacion de las cotizaciones del dolar y euro
moneda = [[], []]
for k in range(2):
    for dia in range(5):
        if k == 0:
            print("Cotizacion del dolar del dia", dia)
        else:
            print("Cotizacion del euro del dia", dia)
        moneda[k]+= [float(input())]
n = 5
prom_dolar = promedio(n, moneda[0])
prom_euro = promedio(n, moneda[1])
mayor_dolar = mayor(n, moneda[0])
mayor_euro = mayor(n, moneda[1])
# Se agregan los resultados a la matriz
moneda[0].append(prom_dolar)
moneda[0].append(mayor_dolar)
moneda[1].append(prom_euro)
moneda[1].append(mayor_euro)

# Despliega el encabezado de salida
letrero = ["L", "Ma", "Mi", "J", "V", "Prom", "Mayor"]
for k in range(7):
    print(letrero[k], "\t", end= "")

# Despliega las cotizaciones
for k in range(2):
    print()
    for j in range(7):
        print(moneda[k][j], "\t", end= "")
