# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 14:33:47 2018

@author: andrease
"""

import pandas as pd

#from mpl_toolkits import mplot3d
#import matplotlib
import numpy as np
import matplotlib.pyplot as plt

data_sensors = pd.read_csv('Sensor_record.csv')

acc_X = data_sensors['ACCELEROMETER X']
acc_Y = data_sensors['ACCELEROMETER Y']
acc_Z = data_sensors['ACCELEROMETER Z']
LATITUDE = data_sensors['LOCATION Latitude : ']
LONGITUDE = data_sensors['LOCATION Longitude : ']
time = data_sensors['Time']

DESIRED_LAT = 48.1373932
DESIRED_LONG = 11.5732598

DISTANCE = np.sqrt((DESIRED_LAT-LATITUDE)**2 + (DESIRED_LONG-LONGITUDE)**2)

print(data_sensors.head())

#Verification of data (Assumption that data is not corrupted)
#Visualization
#With Python

plt.figure(figsize=(10, 10))
plt.plot(time, acc_X, time, acc_Y, time, acc_Z)
plt.xlabel('Time (ms)')
plt.ylabel('(m/s²)')
plt.title('Accelerometer over Time')
plt.show()

plt.figure(figsize=(10, 10))
plt.plot(time, LATITUDE)
plt.xlabel('Time (ms)')
plt.ylabel('Distance (m)')
plt.title('Distance to Marienplatz')
plt.show()