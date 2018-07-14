# Inicio de la clase
class Hola:
    # Atributos de la clase
    Nombre = ""
    Apellido = ""
    def __init__(self, nombre, apellido):
        # Referencia a un atributo de la clase (self.Nombre)
        print("Constructor de la clase")
        self.Nombre = nombre
        self.Apellido = apellido
    def saludar(self):
        print("Hola "+self.Nombre+" "+self.Apellido)
    # Fin de la clase

# Creacion de un objeto asociado a la clase
primerObjeto = Hola("Juan", "Perez")
# Uso de un metodo asociado
primerObjeto.saludar()
