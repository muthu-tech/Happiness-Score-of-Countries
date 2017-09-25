# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 20:30:44 2017

@author: muthu
"""

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import pandas as pd
latLong =pd.read_csv('latlong17.csv')
latLong.set_index(['Country'])

mapObject = Basemap(projection='mill',llcrnrlat=-60,urcrnrlat=75,\
                llcrnrlon=-180,urcrnrlon=180,resolution='c')
mapObject.drawcoastlines()
mapObject.drawcountries()
mapObject.fillcontinents(color='beige',lake_color='lightblue')
ax= plt.subplot(111)
redPoints = []
amberPoints = []
greenPoints = []
for countries,data in latLong.iterrows():
    if data['Happiness Score'] < 4.0:
        tup = (data['Longitude'],data['Latitude'])
        redPoints.append(tup)
    elif data['Happiness Score'] > 4.0 and data['Happiness Score'] < 5.5:
        tup = (data['Longitude'],data['Latitude'])
        amberPoints.append(tup)
    else:
        tup = (data['Longitude'],data['Latitude'])
        greenPoints.append(tup)

for item in redPoints:
    redlons = [point[0] for point in redPoints]
    redlat = [point[1] for point in redPoints]
    redX,redY = mapObject(redlons, redlat)
    ax.plot(redX, redY, 'ro', color='red',markersize=5,alpha=0.1,label='Low happiness score')
for item in greenPoints:
    greenlons = [point[0] for point in greenPoints]
    greenlat = [point[1] for point in greenPoints]
    greenX,greenY = mapObject(greenlons, greenlat)
    ax.plot(greenX, greenY, 'go',color='green', markersize=5,alpha =0.1,label='Most happy')
for item in amberPoints:
    amberlons = [point[0] for point in amberPoints]
    amberlat = [point[1] for point in amberPoints]
    amberX,amberY = mapObject(amberlons, amberlat)
    ax.plot(amberX, amberY, 'bo', color='blue',markersize=5,alpha = 0.1,label ='Moderately happy')    
plt.title('Predicted Happiness Map-2017')
plt.show()