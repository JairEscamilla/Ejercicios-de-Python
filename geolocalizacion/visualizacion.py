from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
# Latitud y longitud de varios puntos de interes
# Mexico, Argentina, NYC
lat = [19.4326009, -34.9964962, 40.7410861]
lon = [-99.1333415, -64.9672816, -73.9896297241625]
# Se inicializa la dimension de la figura
plt.figure(figsize = (16, 12))
eq_map = Basemap(projection = 'robin',
                 lon_0 = 0,
                 resolution = 'h',
                 area_thresh = 1000.0,
                 llcrnrlat = 56,
                 urcrnrlon = -134.25,
                 urcrnrlat = 57.75)
# Se dibujan las lineas costeras y paises
eq_map.drawcoastlines()
eq_map.drawcountries()
# Se define el color de los paises
eq_map.fillcontinents(color = '#e6e6ff')
eq_map.drawmapboundary()
# Se dibujan los meridianos y paralelos
eq_map.drawmeridians(np.arange(0, 360, 30))
eq_map.drawparallels(np.arange(-90, 90, 30))
'"Se dibuja cada uno de los puntos utilizando la instruccion zip"'
for lon, lat in zip(lon, lat):
    x, y = eq_map(lon, lat)
    eq_map.plot(x, y, "ro", markersize = 17, alpha = 0.8)
# Se salva la imagen en formato png de alta resolucion
plt.savefig("visualizacionDatos.png", bbox_inches = "tight", dpi = 100)
