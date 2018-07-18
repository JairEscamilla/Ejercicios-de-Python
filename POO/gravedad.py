class Conversion:
    gravedad = 0
    conversion = 0
    def __init__(self, gravedad):
        if not(type(gravedad) == int):
            print("Los datos deben ser de tipo numerico")
        else:
            self.gravedad = gravedad
    def conversion(self):
        self.conversion = self.gravedad/6.0
        print("La conversion es " + str(self.conversion))

obj = Conversion(150)
obj.conversion()
