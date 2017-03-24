# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 09:04:31 2017

@author: dylanbarth
"""

import scipy.optimize as opt
import matplotlib.pyplot as p
import numpy as np

#initialized parameters
amp_guess = 25.
phase_guess = 10.
offset_guess = 20.
guess_params = np.zeros([3])
guess_params[0]=amp_guess
guess_params[1]=phase_guess
guess_params[2]=offset_guess

#set up arrays
tdata = np.linspace(1995, 2015, 1000)
data = np.loadtxt("munich_temperatures_average_with_bad_data.txt", dtype = float)
ydata = []
data_masked = []
tdata_masked = []

#function that returns true if value falls outside 2 std devs
def isOutlier(value, data):
    if (value > np.mean(data) + 2*np.std(data)) or (value < np.mean(data) - 2*np.std(data)):
        return True
    else:
        return False
        
#function to fit
def F(t, a, b, c):
    return a * np.cos(2*np.pi*t + b) + c

#mask bad data
data_masked.append(data[0,1])
tdata_masked.append(data[0,0])
for i in range(len(data) -1):
    if(isOutlier(data[i+1:i+2,1], data[:,1])==False):
        data_masked.append(data[i+1,1])
        tdata_masked.append(data[i+1,0])
    #else:
        #print("outside range")

#fit the curve and output params
param_out,pcov = opt.curve_fit(F, tdata_masked, data_masked, p0=guess_params)

#add the new data to ydata for graphing
for i in tdata:
    ydata.append(F(i, param_out[0], param_out[1], param_out[2]))

#graph
p.title("Temperatures in Munich")
p.xlabel("Year")
p.ylabel("Temperature in Celsus")
p.xlim(1995,2013)
p.plot(tdata_masked, data_masked, label="Data")
p.plot(tdata, ydata, '#e02b81', linewidth=3, label="Fit")
p.legend()
p.show()

