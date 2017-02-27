# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 14:22:49 2017

@author: dylanbarth
"""
import math


#user types an integer
#set first bit of binary to positive by default (sign)
#create a list
#create a string output
usr_int = input("Type an Integer: \n")
sign = '0'
list = []
output = '0'

#check if input is negative
#if negative, change first bit to 1
#change sign of input to process normally
if usr_int < 0:
    sign = '1'
    usr_int = usr_int*(-1)

#until usr_int is 0 divide by 2 and store remainder
#this will compute the binary representation of the number
#each digit is stored backwards in the list
while usr_int != 0:
    list.append(usr_int%2)
    usr_int = math.floor(usr_int / 2)
    
#multiply each digit to the right placement
#that is, just so we can add them all together to get one final number
for i in range(len(list)):
    list[i] = list[i]*(10**i)

#reverse the list
list = list[::-1]
#get output ready, sum all elements 
#slice the decimals off if any
#put into string
output = str(int(sum(list)))
print("The binary representation is: ")
#print the first bit (sign) concatenated with output
print sign + output