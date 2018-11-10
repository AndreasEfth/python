# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 14:33:47 2018

@author: andrease
"""

from math import radians, cos, sin, asin, sqrt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a_val = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c_val = 2 * asin(sqrt(a_val))
    r_val = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c_val * r_val

#from mpl_toolkits import mplot3d
#import matplotlib

#DATA = pd.read_csv('Work_Romansplatz.csv')
DATA = pd.read_csv('Work_Romansplatz.csv', sep=';', header=1)
#Better way of retrieving DATA from csv

SOUND = DATA['SOUND LEVEL (dB)']
LIGHT = DATA['LIGHT (lux)']
LATITUDE = DATA['LOCATION Latitude : ']
LONGITUDE = DATA['LOCATION Longitude : ']
TIME = DATA['Time since start in ms ']

EXPLAIN = ['The softest sound a person can hear with normal hearing',
           'A normal breathing', 'Whispering at 5 feet', 'A soft whisper',
           'Rainfall', 'A normal conversation', 'Shouting in ear!', 'A thunder!']

#Calculating distance to Romanplatz (destination)
DESIRED_LAT = 48.15536
DESIRED_LONG = 11.51205

DISTANCES = []
COUNT = 0
while True:
    if COUNT < len(LATITUDE):
        DISTANCES.append(haversine(DESIRED_LONG, DESIRED_LAT, LONGITUDE[COUNT], LATITUDE[COUNT]))
        COUNT = COUNT + 1
    else:
        break

plt.figure(figsize=(10, 10))
plt.plot(TIME/1000/60, DISTANCES)
plt.xlabel('Time (min)')
plt.ylabel('Distance (km)')
plt.title('Distance to Romanplatz')
plt.show()

FLAG = False
for DIST in DISTANCES:
    if DIST < 0.01:
        FLAG = True
        break
if FLAG:
    print("\nCongratulations! You have reached your destination.\n\n")

#Explaining dB levels
print("----------------------------------------------------\n")
print("The overall noise level is {:3.2f}dB, which is like: ".format(np.mean(SOUND)))
if np.mean(SOUND) < 7:
    print("\t", EXPLAIN[0])
elif np.mean(SOUND) < 15:
    print("\t\t", EXPLAIN[1])
elif np.mean(SOUND) < 25:
    print("\t\t", EXPLAIN[2])
elif np.mean(SOUND) < 35:
    print("\t\t", EXPLAIN[3])
elif np.mean(SOUND) < 55:
    print("\t\t", EXPLAIN[4])
elif np.mean(SOUND) < 80:
    print("\t\t", EXPLAIN[5])
elif np.mean(SOUND) < 115:
    print("\t\t", EXPLAIN[6])
else:
    print("\t\t", EXPLAIN[7])

print("\nMaximum: {:3.2f}dB.".format(np.max(SOUND)))
print("Minimum: {:3.2f}dB.\n\n".format(np.min(SOUND)))
print("----------------------------------------------------\n")
#What else should I do with the Light
PEAKS, _ = find_peaks(LIGHT, height=1000)
plt.figure(figsize=(10, 10))
plt.plot(TIME/1000/60, LIGHT)
plt.xlabel('Time (min)')
plt.ylabel('Luminosity (lux)')
plt.title('Overall Luminocity fluctuation')
plt.show()

print("You used your phone {} times in {:3.2f} minutes.".format(len(PEAKS), max(TIME/1000/60)))
