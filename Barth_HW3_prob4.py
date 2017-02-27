# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 11:07:00 2017

@author: dylanbarth
"""
import numpy as np
from matplotlib import pyplot as p
from scipy import integrate

def f(t):
    return np.exp(t**2)

def integrate_f(yarray, xarray):
    return integrate.simps(yarray, xarray)

Low_bnd = 0.
Up_bnd = 3.
step_sz = 0.1

xdata = np.linspace(Low_bnd, Up_bnd, num=(Up_bnd-Low_bnd)/step_sz)
ydata = []
for i in xdata:
    ydata.append(f(i))

##print integrate_f(ydata, xdata)

y_idata = []
for i in range(len(xdata)):
    if i>1:
        y_idata.append(integrate_f(ydata[:i],xdata[:i]))
    else:
        y_idata.append(0.)
p.plot(xdata, y_idata)
p.title("Integral Value Over X")
p.ylabel("E(X)")
p.xlabel("X")
p.savefig("Integral.png")
p.show()