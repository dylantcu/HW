# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 09:41:16 2017

@author: dylanbarth
"""

import numpy
from matplotlib import pyplot as p
#initial conditions
theta_0 = 92.
omega_0 = 0.
length = .1
#swtich params
diff_method = "LF" # "RK"|"LF"|null
     #RK produces the RungeKutta diff eq solution, and LF the leapfrog
gif_method = 0 # 0|1
    #0 turns the gif maker off, 1 on.
#steps and sizes
start = 0.
end =  20.
N = 5000
h = (end-start)/N
#set up arrays for various computations
tdata = numpy.arange(start,end,h)
rdata = []
thetadata = []
omegadata = []
t_gifdata = []
x_gifdata = []
y_gifdata = []
l_ygifdata = []
l_xgifdata = []
r_0 = numpy.array([theta_0,omega_0])
rarray = []


def vector(r,t):
    theta = r[0]
    omega = r[1]
    ftheta = omega
    fomega = (-9.81)/(length) * numpy.sin(theta*(numpy.pi / 180.))
    return numpy.array([ftheta,fomega],float)

#solve diff eq by Runge Kutta method
if diff_method == "RK":
    print("RK")
    for t in tdata:
        thetadata.append(r_0[0])
        omegadata.append(r_0[1])
        k1 = h*vector(r_0,t)    
        k2 = h*vector(r_0 + .5*k1,t + .5*h)
        k3 = h*vector(r_0 + .5*k2,t + .5*h)
        k4 = h*vector(r_0 + k3,t + h)
        r_0 += (k1 + k2 + k3 + k4)/6
#solve diff eq by Leap Frog Method
if diff_method == "LF": #doesnt work every time
    print("LF")
    for t in tdata:
        thetadata.append(r_0[0])
        omegadata.append(r_0[1])
        if(t==tdata[0]):
            k1 = h*vector(r_0,t) 
            k2 = h*vector(r_0 + .5*k1,t + .5*h)
            r_0 += (k2)
        else:
            k1 = h*vector(r_0,t) 
            k2 = h*vector(r_0 + k1,t + h)
            r_0 += (k2)
        
#Get x,y coords for bob, line, and time for gif
j = 0 #indexing variable
if gif_method == 1:    
    for i in range(len(tdata)):
        if i%30==0:
            t_gifdata.append(tdata[i])
            x = length*numpy.sin(thetadata[i]*(numpy.pi / 180.))
            y = (-1.)*length*numpy.cos(thetadata[i]*(numpy.pi / 180.))
            x_gifdata.append(x)
            y_gifdata.append(y)
            l_ygifdata.append(0.0)
            l_ygifdata.append(y)
            l_xgifdata.append(0.0)
            l_xgifdata.append(x)
            p.xlim(-.06,.06)
            p.ylim(-.1,0.)
            p.title("Pendulum Over Time in Real Space")
            p.ylabel("height of bob (m)")
            p.xlabel("horizontal distance of bob (m)")
            p.plot(l_xgifdata[j:j+2],l_ygifdata[j:j+2],linewidth=3)
            p.plot(x_gifdata, y_gifdata, 'o', ms=15)
            p.savefig("gif_frames/" + str(j/2) + "pend.png")
            j += 2
#plot  
if gif_method==0:
    print min(thetadata[2500:])
    p.title("Angle of NonLinear Pendulum Over Time")
    p.xlabel("Time (s)")
    p.ylabel("Angle of Pendulum Arm (degrees)")
    p.plot(tdata,thetadata)
    p.savefig(diff_method + "Pendulum.png")
    p.show()