# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 00:32:11 2017

@author: dylanbarth
"""

import numpy as np
from matplotlib import pyplot as p
import math

a = input("Enter a quadratic term: ")
b = input("Enter a linear term: ")
c = input("Enter a constant term: ")

x1 = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
x2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
print "\nsolutions: " + str(x1) + "," +  str(x2)


x3 = (2*c)/(-b + math.sqrt(b**2 - 4*a*c))
x4 = (2*c)/(-b - math.sqrt(b**2 - 4*a*c))
print "'alternative' solutions: "+str(x3) + "," +  str(x4)

"""
solutions: -9.99989424599e-07,-999999.999999
'alternative' solutions: -1000010.57551,-1e-06

because b**2 and 4ac have such drstic differences, the error takes hold and 
really messes things up.
"""
### I have no idea how i'm supposed to accurately calculate this.