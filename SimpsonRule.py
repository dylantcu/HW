# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 09:30:51 2017

@author: dylanbarth
"""

###################################
#   Define values of variables    #
###################################
N = 10 #Number of steps
a = 0.  #Starting x value
b = 2.  #Ending x value
h = (b-a)/N

###################################
#   Define function to integrate  #
###################################
def f(x):
    return (x**4 - 2*x + 1)

###################################
# Split integration into thirds   #
# Then compute each to sum them   #
###################################
first_third = (f(a) + f(b) )*(h/3)

second_third = 0.
for k in range(1,N,2):
    second_third += f(a + k*h)
second_third = second_third*4*(h/3)

last_third = 0.
for k in range(2,N,2):
    last_third += f(a + k*h)
last_third = last_third*2*(h/3)

###################################
#   sum the three terms and print #
###################################
summation = first_third + second_third + last_third
print("The integral from " + str(a) + " to " + str(b) + " is: " + str(summation))