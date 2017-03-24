# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 11:07:47 2017

@author: dylanbarth
"""

import fitsio as f
from matplotlib import pyplot as p
import numpy as np
import scipy.optimize as o

#get data from fits table
data = f.FITS('/Users/dylanbarth/Desktop/Academic Papers/Cosc/Computational Physics/allStar-l30e.2.fits')
cut = data[1].where('GLAT > -1 && GLAT < 1 && GLON > 3 && GLON < 10')
subset = data[1][cut]

#define a function to determine if outliers
def isOutlier(value, dataset):
    if((value < -999)):
        return True
    else:
        return False
        
#define functions to be fit
def line(t,a,b):
    return t*a +b
def quad(t,a,b,c):
    return a*(t**2) + b*t + c
    
#initial parameters    
param_guess_l = np.array([-1,1])    
param_guess_q = np.array([1,1,1])    
tdata = np.linspace(-1.5,0.5,100)    
    
#create arrays for masked values
FE_H  = []
O_FE = []
lindata = []
quaddata = []

#mask bad values
for i in range(len(subset[:]['FE_H'])):
    if(isOutlier(subset[:]['FE_H'][i], subset[:]['FE_H'])==False):
        if(isOutlier(subset[:]['O_FE'][i], subset[:]['O_FE'])==False):
            FE_H.append(subset[:]['FE_H'][i])
            O_FE.append(subset[:]['O_FE'][i])
    
#optimize functions and make param arrays    
param_fit_l, pcov_l = o.curve_fit(line,FE_H,O_FE,p0=param_guess_l)
param_fit_q, pcov_q = o.curve_fit(quad,FE_H,O_FE,p0=param_guess_q)
print param_fit_l, param_fit_q

#get data for fit lines
for i in tdata:
    lindata.append(line(i, param_fit_l[0],param_fit_l[1]))
    quaddata.append(quad(i, param_fit_q[0],param_fit_q[1],param_fit_q[2]))

#graph
p.xlabel("FE_H")
p.ylabel("O_FE")
p.title("FE_H vs O_FE")
p.plot(FE_H,O_FE, '.')
p.plot(tdata,lindata)
p.plot(tdata,quaddata)
p.show()