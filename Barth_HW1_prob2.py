# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 18:08:32 2017

@author: dylanbarth
"""

from math import pi
#G = gravitational constant
#M = mass of earth
#R = radius of earth in m
G = 6.67*(10**-11) #m^3 kg^-1 s^-2
M = 5.97*(10**24) #kg
R = 6371*1000 #m
#T is the orbit time in seconds
T = input("Enter an Orbit Time in seconds:\n")
#h computes the height in meters from the outer edge of earth 
h = ((G*M*(T**2))/(4*(pi**2)))**(1.0/3) - R

print "\nYour satellite must be " + str(h) + "m" 
print "or " + str(h/1000) + "km from the outer edge of Earth"