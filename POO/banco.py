# Inicio de la clase
class CuentaBancaria:
    # Variables de clase
    saldo = None
    nombre = None
    # Constructor de la clase
    def __init__(self, saldo, nombre):
        # Revisar si las variables de entrada son del tipo especifico
        if (type(saldo) == int or type(saldo) == float and isinstance(nombre, str)):
            self.saldo = saldo
            self.nombre = nombre
            self.mostrarInformacion()
        # Si no son del tipo especifico, se ponen valores por default
        else:
            self.saldo = 0
            self.nombre = "Desconocido"
            self.mostrarInformacion()
    '"Despliega la representacion de la cuenta bancaria como una cadena"'
    def mostrarInformacion(self):
        print(self.nombre+" cuenta con: " + str(self.saldo) + " de saldo")

    def deposito(self, cantidad):
        if type(cantidad) == int or type(cantidad) == float:
            print("Deposito de " + self.nombre + " por: " + str(cantidad))
            # Incrementar la cantidad de saldo
            self._calcularSaldo(cantidad)
            self.mostrarInformacion()

    def retiro(self, cantidad):
        if type(cantidad) == int or type(cantidad) == float:
            print("Retiro de " + self.nombre + " por: " + str(cantidad))
            cantidadRetirar = cantidad
            if cantidadRetirar > self.saldo:
                print(self.nombre + " no hay saldo suficiente")
            else:
                # Reducir la cantidad del saldo de la cuenta
                self._calcularSaldo(self.saldo - cantidadRetirar)
                self.mostrarInformacion()
        else:
            print("Retiro de " + self.nombre + " por " + str(cantidad))
            print("Las cantidades deben de ser numeros.")

    def _calcularSaldo(self, cantidad):
        # Obtener el saldo asociado a la cuenta
        self.saldo = cantidad
# Fin de la clase

# NOTE: Creacion de objetos
objeto1 = CuentaBancaria(12, "Pedro")
objeto2 = CuentaBancaria(125, "Juan")
# Manipulacion de las funciones de los objetos
objeto2.retiro(89)
objeto1.retiro(12000)
objeto1.deposito("mil doscientos")
