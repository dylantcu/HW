# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 17:53:51 2017

@author: dylanbarth
"""
from sys import exit

################################
# define the conditions for a5 # 
################################

def whats_a5(Z,A):
    if A % 2 == 1:
        a5 = 0
    elif Z % 2 == 0:
        a5 = 12.0
    else:
        a5 = -12.0
    return a5

#####################################
# ask user for atomic number, mass  #
# check if int, if not ABANDON SHIP # 
#####################################

Z = input("Choose an element by typing an atomic number: ")
if (float(Z)).is_integer()==False:
    exit("Atomic number must be an integer")
A = input("Type a mass number for your element: ")
if (float(A)).is_integer()==False:
    exit("Atomic mass must be an integer")

################################
# set constants. including a5  # 
################################
    
a1 = 15.67
a2 = 17.23
a3 = .75
a4 = 93.2
a5 = whats_a5(Z,A)

#################################
# Use Semi-Empirical Formula to # 
# calculate binding energy(MeV) #
#################################

B = a1*A
B += -a2*(A**(2./3))
B += -a3*(Z**2)/(A**(1./3))
B += -(a4/A)*((A-2*Z)**2)
B += -a5*(A**(-1./2))

################################
# return values                # 
################################

print("\nThe total binding energy is: " +str(B)+ " MeV")
print("The binding energy per nucleon is: " +str(B/A)+ " MeV per nucleon")

################################
# ANSWERS: output from code    # 
################################

"""
    A: 58, Z: 28
The total binding energy is: 490.784252413 MeV
The binding energy per nucleon is: 8.46179745539 MeV per nucleon
    A: 59, Z: 28
The total binding energy is: 498.144677546 MeV
The binding energy per nucleon is: 8.44313012789 MeV per nucleon
    A: 58, Z: 27
The total binding energy is: 485.309348976 MeV
The binding energy per nucleon is: 8.36740256855 MeV per nucleon

"""