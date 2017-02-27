# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 10:10:06 2017

@author: dylanbarth
"""

from math import sqrt
from sys import exit

##################################
# define function for correction # 
##################################
   
def gamma(a):
    return ((sqrt(1-a**2)**(-1)))
    
################################
# ask user for distance (ly)   # 
# and a speed in terms of c    #
# catch if speed is not ^      #
################################
d = input("Enter a distance in light-years: ")
v = input("Enter a speed as a fraction of c (on a scale from [0,1)): ")
if v < 0. or v >= 1.:
    exit("ERROR: Try again with a speed value between 0 and 1")
    
####################################
# calculate time passed from earth #
# and proper time as well          #
####################################
    
earth_t = d/v
prop_t = earth_t*((gamma(v))**(-1.))

#################################
#        return values          # 
#################################

print("\nTravelling at " +str(v)+ "c, it will take " +str(earth_t)+ " earth years to reach your destination " +str(d)+" light years away")
print("However, due to time dialation, the passenger who is travelling will experience a mere " +str(prop_t)+ " years")

#################################
#       Answers: output         # 
#################################

"""
Travelling at 0.9c, it will take 11.1111111111 earth years to reach your destination 10 light years away
However, due to time dialation, the passenger who is travelling will experience a mere 4.84322104838 years

Travelling at 0.98c, it will take 10.2040816327 earth years to reach your destination 10 light years away
However, due to time dialation, the passenger who is travelling will experience a mere 2.03058660634 years

Travelling at 0.999c, it will take 10.01001001 earth years to reach your destination 10 light years away
However, due to time dialation, the passenger who is travelling will experience a mere 0.44754932745 years

"""