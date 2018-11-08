# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 14:33:47 2018

@author: andrease
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

data_sensors = pd.read_csv('Stairs and Jumps.csv')

acc_X = data_sensors['ACCELEROMETER X (m/s²)']
acc_Y = data_sensors['ACCELEROMETER Y (m/s²)']
acc_Z = data_sensors['ACCELEROMETER Z (m/s²)']
LATITUDE = data_sensors['LOCATION Latitude : ']
LONGITUDE = data_sensors['LOCATION Longitude : ']
time = data_sensors['Time since start in ms ']

#Verification of data (Assumption that data is not corrupted)
#Visualization
#With Python

plt.figure(figsize=(20, 20))
#plt.plot(time, acc_X, time, acc_Y, time, acc_Z)

plt.plot(time, acc_Y, 'ro-')
plt.xlabel('Time (ms)')
plt.ylabel('(m/s²)')
plt.title('Accelerometer over Time')
plt.show()
"""
plt.figure(figsize=(10, 10))
plt.plot(time, LATITUDE)
plt.xlabel('Time (ms)')
plt.ylabel('Distance (m)')
plt.title('Distance to Marienplatz')
plt.show()"""
limit = 16
acc_Y = acc_Y[limit:len(acc_Y)-limit]

plt.figure(figsize=(20, 20))
peaks, _ = find_peaks(acc_Y, height=0)
plt.plot(acc_Y)
plt.plot(peaks, acc_Y[peaks], "x")
plt.plot(np.zeros_like(acc_Y), "--", color="gray")
plt.show()
print(len(peaks))
