# Inicio de la clase padre Operacion
class Operacion:
    # Atributos de la clase
    valor1 = 0
    valor2 = 0
    # Metodos de la clase
    # Constructor de la clase
    def __init__(self, numero1, numero2):
        self.valor1 = numero1
        self.valor2 = numero2
    # Obtener valor 1 getter
    def obtenerValor1(self):
        return self.valor1
    # Obtener valor 2
    def obtenerValor2(self):
        return self.valor2
    # Cambiar valor 1
    def cambiarValor1(self, numero):
        self.valor1 = numero
    # cambiar valor 2
    def cambiarValor2(self, numero):
        self.valor2 = numero
    def imprimirValor(self, numero):
        print(numero)
# Fin de la clase

# Inicio de la clase suma
class Suma(Operacion):
    '"Se llama al Constructor de la clase padre para inicializar los numeros"'
    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2)
    '"Se agregar un metoso nuevo a la clase suma (que no esta en la clase padre)"'
    def sumar(self):
        self.imprimirValor(self.valor1 + self.valor2)
# Fin de la clase suma


# Creacion del objeto de la clase hijo
suma1 = Suma(10, 5)
print("Operando 1 de la suma")
suma1.imprimirValor(suma1.obtenerValor1())
print("Operando 2 de la suma")
suma1.imprimirValor(suma1.obtenerValor2())
print("Resultado de la suma => ")
suma1.sumar()

class Multiplicacion(Operacion):
    """docstring for Multiplicacion."""
    def __init__(self, numero1, numero2):
        super().__init__(numero1, numero2)
    def multiplicar(self):
        self.imprimirValor(self.valor1*self.valor2)

    # Se sobreescribe un metodo de la clase padre
    def imprimirValor(self, numero):
        print("El numero es->"+str(numero))
# Fin de la clase hijo

multiplicacion = Multiplicacion(10, 5)
multiplicacion.imprimirValor(multiplicacion.obtenerValor1())
multiplicacion.imprimirValor(multiplicacion.obtenerValor2())
print("Resultado de la multiplicacion: ")
multiplicacion.multiplicar()
