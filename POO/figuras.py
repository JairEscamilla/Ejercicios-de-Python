class Figura:
    valor1 = None
    valor2 = None
    def __init__(self, valor1, valor2):
        # Se inicializan las variables que son comunes a las clases hijo
        self.valor1 = valor1
        self.valor2 = valor2
    def area(self):
        # Se le asigna un comportamiento generico a la clase padre
        print("El area de la figura no esta definida")

    def perimetro(self):
        print("El perimetro de la figura no esta definida")
# Fin de la clase padre

# NOTE: Inicio de la clase hijo
class Rectangulo(Figura):
    def __init__(self, valor1, valor2):
        super(Rectangulo, self).__init__(valor1, valor2)
    def area(self):
        areaRectangulo = self.valor1 * self.valor2
        print("El area del rectangulo es "+ str(areaRectangulo))
        return areaRectangulo
    def perimetro(self):
        perimetro = 2 * self.valor1 + 2 * self.valor2
        print("El perimetro es "+ str(perimetro))
        return perimetro
# Fin de la clase hijo

# Inicio de la clase hijo

class Triangulo(Figura):
    base = None
    altura = None
    def __init__(self, valor1, valor2, base, altura):
        super(Triangulo, self).__init__(valor1, valor2)
        self.base = base
        self.altura = altura

    def area(self):
        area = (self.base * self.altura)/ 2
        print("El area es", area)
        return area

    def perimetro(self):
        perimetro = (self.valor1 + self.valor2 + self.base)
        print("El perimetro es", perimetro)
        return perimetro


# Creacion de onbjetos
obj1 = Figura(31, 12)
obj2 = Rectangulo(9, 5)
obj3 = Triangulo(10, 8, 5, 6)

print("Clase padre: ")
obj1.perimetro()
obj1.area()


print("Clase hijo: ")
obj2.perimetro()
obj2.area()


print("Clase hijo: ")
obj3.perimetro()
obj3.area()
