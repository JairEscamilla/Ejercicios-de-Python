# Se importa el modulo time
import time
from geopy.geocoders import Nominatim
# Se genera un objeto de la clase Nominatim
geolocator = Nominatim()
# Se crea una lista de lugares a buscar
places = ["Mexico", "Buenos Aires Argentina", "Indios Verdes", "Universidad Iberoamericana", "Colonia Jorge Negrete"]
for x in places:
    location = geolocator.geocode(x, timeout = 10)
    # Se imprime la informacion obtenida
    print("lugar: " + x + " coordenadas: " + str(location.latitude) + ", " + str(location.longitude))
    time.sleep(1)
