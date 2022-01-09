import json

import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap


def test_draw():
    from mpl_toolkits.basemap import Basemap
    import matplotlib.pyplot as plt

    # map = Basemap(projection='cyl',
    # lat_0=56, lon_0=0)
    lon = []
    lat = []
    pricePerm2 = []

    with open('data2.json', encoding='utf8') as json_file:
        dati = json.loads(json_file.read())

    for i in range(len(dati)):  #

        lon.append(dati[i]['coord'][1])
        lat.append(dati[i]['coord'][0])
        pricePerm2.append(float(dati[i]['price1m2'][: - 2])*50)      # remove Eur symbol

        print(i, float(dati[i]['price1m2'][: - 2])*100)

    map = Basemap(projection='lcc', resolution='i',
                  lat_0=57, lon_0=24,
                  width=0.5E6, height=0.6E6)

    map.shadedrelief()
    map.drawcoastlines(color='gray')
    map.drawcountries(color='gray')
    map.drawstates(color='gray')

    area = 50

    map.scatter(lon, lat, latlon=True,
                c=pricePerm2, s=area,
                cmap='Reds', alpha=0.5)

    plt.show()
