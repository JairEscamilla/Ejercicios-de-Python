'"Reconoce palindromos"'
def lectura():
    frase = input("Dame la frase sin espacios: ")
    lista = []
    for k in range(len(frase)):
        lista.append(frase[k])
    print(lista)
    return lista
def checar(lista):
    max = len(lista)
    frase = list(reversed(lista))

    # Inicializa el indice del ciclo y el contador
    numero = 0
    contador = 0
    while numero+1 <= max/2:
        if frase[numero] == lista[numero]:
            contador+= 1
        numero+= 1

    if contador == max//2:
        print("La frase si es palindromo")
    else:
        print("La frase no es palindromo")
# NOTE: PROGRAMA PRINCIPAL
lista = lectura()
checar(lista)
