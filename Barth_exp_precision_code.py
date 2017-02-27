# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 10:15:20 2017

@author: dylanbarth
"""
from math import factorial as f
from math import exp as e

def exp(x, n):
    term1 =  (-1.)**n 
    term2 = x**n
    term3 = f(n)
    return term1*(term2/term3)

x = 1.
summation = 0.
for i in range(10):
    summation += exp(x,i)
print "modeled value: e^-" + str(x) + " ~ " + str(summation)
err = ((abs(summation - e(-x)))/(e(-x)))*100.
print "error: " + str(err) + "%"