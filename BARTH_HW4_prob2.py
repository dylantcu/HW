# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 00:45:26 2017

@author: dylanbarth
"""
#
#   This program is faulty, the pfunc method should compute the inverse sample
#   However, it seems that when I computed inv(f(x)), I made a mistake, because
#   it returns values well over 1.0 (even though the inverse is relatively simple.)
#
import numpy
import random
def f(x):
    return (x**(-1./2))/(numpy.exp(x) + 1)

def pfunc():
#    unif = random.uniform(0,1)
    x = 1./(4*((random.uniform(0,1))**2))
    return x

def w(x):
    return x**(1./2)


N = 1000000
integral = 0.

for i in range(N):
    xi = pfunc()
    #if i%100000==0:
    #    print xi
    integral += (f(xi)/w(xi))

integral = integral*(1./N)*(2./3)
print integral