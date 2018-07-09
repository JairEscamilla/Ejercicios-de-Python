'"Funciones en Python"'
def primo(numero):
    # Dado un numero entero positivo, determina si es primo o no
    # INICIO
    from math import sqrt
    es_primo = True # Suponemos que es primo
    divisor = 2 # NOTE: Se iniciara el recorrido desde 2 y llegara hasta la raiz cuadrada del numero a menos que antes se encuentre un divisor exacto
    while divisor <= sqrt(numero) and es_primo:
        cociente = numero//divisor # NOTE: Division entera
        if cociente*divisor==numero:
            es_primo = False # No es primo
        else:
            divisor+= 1 # Se sigue buscando
    return(es_primo)

n = int(input("Ingresa un numero entero: "))
es_primo = primo(n) # NOTE: Checamos si el numero es primo o no
if es_primo:
    print("Si es primo")
else:
    print("No es primo") 
