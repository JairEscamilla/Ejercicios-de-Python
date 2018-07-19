'"Se importa dentro del programa el modulo de geopy para acceder a OpenStreetMap Nominatim"'
from geopy.geocoders import Nominatim
# Se genera un objeto de la clase Nominatim
geolocator = Nominatim()
# Se crea un string con el lugar a buscar
place = "Universidad Iberoamericana"
# Se utiliza la funcion geocode del objeto para obtener la latitud y longitud
location = geolocator.geocode(place)
# Se imprime la informacion obtenida
print("lugar: "+place+" coordenadas: "+str(location.latitude)+", "+str(location.longitude))
