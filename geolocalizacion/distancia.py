'"Se importa dentro del programa el modulo de geopy para acceder al algoritmo vicenty o great_circle"'
from geopy.distance import vincenty
from geopy.distance import great_circle
'"Se generan 2 objetos con las cooredenadas de Argentina y Mexico en formato de tupla"'
Argentina = (-34.9964962, -64.9672816)
Mexico = (19.4326009, -99.1333415)
# Se imprime la distancia en millas usando vincenty
print("Distancia entre Mexico y Argentina (vincenty)-> "+str(vincenty(Argentina, Mexico).miles))
# Se imprime la distancia en millas usando great_circle
print("Distancia entre Mexico y Argentina (great_circle)-> "+str(great_circle(Argentina, Mexico).miles))
