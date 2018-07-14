# Inicio de la clase
class NumeroComplejo:
    # Atributos de la clase
    ParteReal = 0
    ParteImaginaria = 0
    # Metodos de la clase
    # Constructor de la clase
    def __init__(self, real, imaginaria):
        self.ParteReal = real
        self.ParteImaginaria = imaginaria
    # Imprimir numero complejo
    def imprimirNumero(self):
        print(str(self.ParteReal)+" +i *", str(self.ParteImaginaria))
    # Cambiar la parte real (setter)
    def cambiarParteReal(self, real):
        self.ParteReal = real
    # Obtener la parte real (getter)
    def obtenerParteReal(self):
        return self.ParteReal
    # Cambiar la parte imaginaria (setter)
    def cambiarParteImaginaria(self, imaginaria):
        self.ParteImaginaria = imaginaria
    # Obtener la parte imaginaria (getter)
    def obtenerParteImaginaria(self):
        return self.ParteImaginaria

    # Fin de la clase

# Creacion de un objeto asociado a la clase
primeroNumero = NumeroComplejo(12.0, 4.0)
print("Numero complejo")
# Uso de un metodo asociado al objeto
primeroNumero.imprimirNumero()
