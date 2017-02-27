# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 01:02:14 2017

@author: dylanbarth
"""
import numpy as np
from matplotlib import pyplot as p

def f(x):
    return (x**4)*(np.exp(x))/((np.exp(x)-1)**2)

def cv(T):
    N = 1000 #sample points
    V = 1000. #cubic cm
    rho = 6.022e28 #cubic cm
    Theta = 428. #K
    Boltz = 1.380e-23 #J/K
    constant = 9*V*rho*Theta*Boltz * (T/Theta)**3        
    #integrate
    upper_lim = Theta/T
    lower_lim = 0.
    h = (upper_lim-lower_lim)/N
    s = .5*lower_lim + .5*upper_lim
    for k in range(1,N):
        s+=f(lower_lim+k*h)
    return constant*s
    
T_data = range(5,501)
cv_data = []
for i in T_data:
    cv_data.append(cv(i))

p.title("Heat Capacity vs Temperature")   
p.ylabel("Heat Capacity") 
p.xlabel("Temperature (K)")

p.plot(T_data, cv_data)
p.savefig("HCvsT.png")
p.show()