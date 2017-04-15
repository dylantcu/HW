# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 22:05:51 2017

@author: dylanbarth
"""
import numpy as np
from matplotlib import pyplot as p
#initial conditions
rho_proj =10.5*1000. #kg/m3
r = 0.1 #meters
theta = 52. #degrees to the horizontal
y_0 = 13. #m above the origin fired from
x_0 = 0. #m right of origin fired from
v_0 = 100. #m/s velocity fired at originally
rho_air = 1.18 #kg/m3
c = .47 #coefficient of drag
g = -9.81 #gravity
coeff = 0.#np.pi*(r**2)*rho_air*c/((8./3)*rho_proj*(np.pi*(r**3))) #replace 0 for no drag force
v = np.array([x_0,y_0,v_0*np.cos(theta*(np.pi/180)),v_0*np.sin(theta*(np.pi/180))]) #v for vector

#more initial conditions
start = 0. #time start (should be 0)
end =  30. #time end (s)
N = 5000 #number of points simulated
h = (end-start)/N
tdata = np.arange(start,end,h)
xdata = []
ydata = []
gif = 0 #0 if off, 1 if on

#a vector function that calculates poisition, velocity, acceleration.
#the function outputs an array made to be used for runge kutta 
def r(v,t):
    dx_dt = v[2]
    dy_dt =  v[3]
    vx = dx_dt
    vy = dy_dt
    d2x_dt2 = (-1)*coeff*dx_dt*(np.sqrt((dx_dt**2)+(dy_dt**2)))
    d2y_dt2 = g - (-1)*coeff*dy_dt*(np.sqrt((dx_dt**2)+(dy_dt**2)))
    return np.array([vx,vy,d2x_dt2,d2y_dt2])
    
#Runge Kutta process for air resistance
for t in tdata:
    xdata.append(v[0])
    ydata.append(v[1])
    k1 = h*r(v,t)    
    k2 = h*r(v + .5*k1,t + .5*h)
    k3 = h*r(v + .5*k2,t + .5*h)
    k4 = h*r(v + k3,t + h)
    v += (k1 + k2 + k3 + k4)/6
for t in range(len(tdata)):
    if ydata[t] < 0:
        print xdata[t-1]
        break;

#graph
if gif == 0:
    p.title("Trajectory of Canonball")
    p.xlabel("X Distance (m)")
    p.ylabel("Y Height (m)")
    p.ylim(0,max(ydata)*1.10)
    p.xlim(0,max(xdata)*1.10)
    p.plot(xdata,ydata, label="Pb Cannonball")   
    p.show()     
if gif == 1:
    for t in range(len(tdata)):
        if(t % 30==0.):
            p.title("Trajectory of Canonball")
            p.xlabel("X Distance (m)")
            p.ylabel("Y Height (m)")
            p.ylim(0,max(ydata)*1.10)
            p.xlim(0,max(xdata)*1.10)
            p.plot(xdata[:t],ydata[:t])
            p.plot(xdata[t],ydata[t],'o', ms=15)
            p.savefig("midterm/gifframes/" + str(t) + "frame.png")
            p.show() 
    p.title("Trajectory of Canonball")
    p.xlabel("X Distance (m)")
    p.ylabel("Y Height (m)")
    p.ylim(0,max(ydata)*1.10)
    p.xlim(0,max(xdata)*1.10)
    p.plot(xdata[:],ydata[:])
    p.plot(xdata[-1],ydata[-1],'o', ms=15)
    p.show()             

   
