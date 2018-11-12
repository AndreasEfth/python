# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 14:33:45 2018
Feature extraction and activity detection using AndroSensor.
All mobile senosr data is collected using AndroSensor mobiel app.
Data is imported and visualozed using pandas and matplolib libearies.
Feature isextracted using sliding window and activity is evaluated.

Feature Extracted from 'stairs_n_jumps.csv':
        1. Number of stairs 
        2. Detect the blue light indicator
        
@author: rahulm99
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks

def peak_counter(lower_bound, upper_bound, column, threshold):
    ''' Calculate peak points within given range and threshold.
        Works as sliding window function to select the range.
        In:
            lower_bound: integer lower limit in range
            upper_bound: integer upper bound in limit
            column: string value for column
            threshold: integer value to eliminate lower values
        Return:
            Number of peaks in given range
    '''
    filtered_data = DATA_FIELD[column].iloc[lower_bound:upper_bound]
    peak, _ = find_peaks(filtered_data, height=threshold)
    num_peak = len(peak)
    return num_peak

#import the sensor data from .csv file
DATA_FIELD = pd.read_csv('Sensor_record_AndroSensor.csv')

ACC_X = DATA_FIELD['ACCELEROMETER X']
ACC_Y = DATA_FIELD['ACCELEROMETER Y']
ACC_Z = DATA_FIELD['ACCELEROMETER Z']

#New column is added in dataframe, contains RMS value of accelerometer of all three axis.
DATA_FIELD['ACC_RMS'] = np.sqrt(DATA_FIELD['ACCELEROMETER X'] **2 + DATA_FIELD['ACCELEROMETER Y'] ** 2 + DATA_FIELD['ACCELEROMETER Z'] **2)
plt.plot(DATA_FIELD.index, DATA_FIELD['ACC_RMS'])
plt.show()

print("Number of steps : ", peak_counter(900, 1500, 'ACC_RMS', 16))

LIGHT = DATA_FIELD['LIGHT']
plt.plot(DATA_FIELD.index, DATA_FIELD['LIGHT'])
plt.show()

print(DATA_FIELD['Time'].iloc[2000]/1000)
print("Ligh is low for 200 seconds that means darkness around the mobile.")
print("Turn ON the blue light filter")

print("test Anggy")