import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

def drawContent():
    # Extract the data we're interested in
    lat = [34.052235, 37.773972]
    lon = [-118.243683,-122.431297]
    population = [500, 300]
    area = [10, 6]

    # 1. Draw the map background
    fig = plt.figure(figsize=(8, 8))
    m = Basemap(projection='lcc', resolution='h',
                lat_0=37.5, lon_0=-119,
                width=1E6, height=1.2E6)
    m.shadedrelief()
    m.drawcoastlines(color='gray')
    m.drawcountries(color='gray')
    m.drawstates(color='gray')

    plt.show()



    # 2. scatter city data, with color reflecting population
    # and size reflecting area
    m.scatter(lon, lat, latlon=True,
              c=np.log10(population), s=area,
              cmap='Reds', alpha=0.5)

    # 3. create colorbar and legend
    plt.colorbar(label=r'$\log_{10}({\rm population})$')
    plt.clim(3, 7)

    # make legend with dummy points
    for a in [100, 300, 500]:
        plt.scatter([], [], c='k', alpha=0.5, s=a,
                    label=str(a) + ' km$^2$')
    plt.legend(scatterpoints=1, frameon=False,
               labelspacing=1, loc='lower left')

    lat = 57.3903918
    lon = 21.5635991

    x, y = map(lon, lat)

    plt.text(x, y, 'Ventspils', fontsize=12, fontweight='bold',
             ha='left', va='center', color='k',
             bbox=dict(facecolor='b', alpha=0.2))

    map.plot(x, y, marker='D', color='r')


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