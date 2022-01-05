import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap



def test_draw():
    from mpl_toolkits.basemap import Basemap
    import matplotlib.pyplot as plt

    #map = Basemap(projection='cyl',
                  #lat_0=56, lon_0=0)

    map = Basemap(projection='lcc', resolution='i',
                lat_0=57, lon_0=24,
                width=0.5E6, height=0.6E6)

    map.shadedrelief()
    map.drawcoastlines(color='gray')
    map.drawcountries(color='gray')
    map.drawstates(color='gray')


    lon = [25.03262 ,21.5635991]
    lat = [56.362693, 57.3903918]

    price = [500,600]
    area = [300,400]

    map.scatter(lon, lat, latlon=True,
              c=price, s=area,
              cmap='Reds', alpha=0.5)



    plt.show()