import math
# NOTE: Inicio de clase
class Estadistica:
    def media(self, lista):
        '"Se verifica que cada elemento de la lista sea de tipo int o float"'
        if all((isinstance(x, int) or isinstance(x, float)) for x in lista) == True:
            acumulado = 0
            for x in lista:
                acumulado = acumulado + x
            return acumulado/len(lista)
        else:
            print("La funcion solamente admite numeros")
            return 0
    def desviacionEstandar(self, lista):
        if all((isinstance(x, int) or isinstance(x, float)) for x in lista) == True:
            acumulado = 0
            media = self.media(lista)
            for x in lista:
                acumulado = acumulado + ((x - media)**2)
            return math.sqrt(acumulado/len(lista))
        else:
            print("La funcion solamente admite numeros")
            return 0
# Fin de la clase
# NOTE: Creacion de objetos
operacion = Estadistica()
# Manipulacion de las funciones de los objetos
lista = [9, 3, 8, 8, 5.6, 9, 8, 9, 18, 1.442677]
print("Lista: "+", ".join(str(x) for x in lista))
print("Media: "+ str(operacion.media(lista)))
print("Desviacion estandar: "+ str(operacion.desviacionEstandar(lista)))
