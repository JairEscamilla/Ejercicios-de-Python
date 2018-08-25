def neurona(entrada, peso): # Valores de entradas y valores de peso
    c = 0 # Conteo
    multiplicados = [] # Buffer
    for entrada1 in entrada:
        analisis1 = entrada*peso[c]
        multiplicados.append(analisis1)
        c+= 1
    suma = 0
    for i in multiplicados:
        suma+= i
    peso = math.tanh(suma)
    if suma == len(entrada):
        return suma
    return peso
