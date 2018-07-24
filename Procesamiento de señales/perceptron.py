# Neurona: Objeto de conco entradas, cada entrada
# con su matriz de pesos
# Cuenta con dos funciones, una para activar
# hacia adelante, feedforward
# la otra funcion actualiza los pesos cuando se esta
# generamdo aprendizaje backpropagation
class Neurona():
    def __init__(self):
        self._entradas = []
        self._pesos = []
        self._salida = 0.0
    def actualiza_pesos(self, nvos_pesos):
        for i, elemento in enumerate(nvos_pesos):
            self._pesos.append(elemento)
    def actualiza_entradas(self, nvos_pesos):
        for i, elemento in enumerate(nvos_pesos):
            self._entradas.append(elemento)
    # ****************************************************
    # calcula el resultado de la función
    # y obtiene la salida como una
    # combinación lineal de las entradas y los pesos.
    # *****************************************************
    def calcula(self):
        for a, b in zip(self._entradas, self._pesos):
            self._salida = self._salida + a * b
            # self._salida = self._salida + self._bias
            return self._salida

mi_neurona = Neurona()
nuevos_pesos = [0.3, 0.4, 0.5, 0.1, 0.9]
mi_entrada = [1.0, 1.0, 1.0, 0.0, 0.0]
mi_neurona.actualiza_pesos(nuevos_pesos)
mi_neurona.actualiza_entradas(mi_entrada)
print("Hola, el resultado es ")
print(mi_neurona.calcula())
