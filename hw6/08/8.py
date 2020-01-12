#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 10:45:57 2019

@author: alankar
"""

import numpy as np
import matplotlib.pyplot as plt
import RK4
import time

#Relation of code units with SI units
UNIT_LENGTH = 1.496e11 #AU -> m
UNIT_VELOCITY = 1e3 #kms^-1 -> ms^-1
UNIT_DENSITY = 1 # kgm^-3

#In Code units
G = 6.67408e-11/(UNIT_LENGTH**3*((UNIT_DENSITY*UNIT_LENGTH**3)**(-1))*((UNIT_LENGTH/UNIT_VELOCITY)**(-2)))

def f(t,x,M): 
    x, x1, y, x2 = x
    r = np.sqrt(x**2+y**2)
    xdot = x1
    ydot = x2
    x1dot = -G*M * x/r**3
    x2dot = -G*M * y/r**3
    return np.array([[xdot,x1dot,ydot,x2dot]]).T

t = np.linspace(0,24,1000000) #Time in code units
x0 = [4e12/UNIT_LENGTH,0,0,500/UNIT_VELOCITY] #x, vx, y, vy
Msun = 2e30/(UNIT_DENSITY*UNIT_LENGTH**3)
elapsed = time.time()
soln = RK4.RK4(f,x0,t,Msun)
elapsed = time.time() - elapsed
print('RK4 Integrator took %.2f seconds'%elapsed)

plt.figure(figsize=(13,10))
plt.plot(soln[0],soln[2])
plt.grid()
plt.ylabel(r'y (AU)',size=18)
plt.xlabel(r'x (AU)',size=20)
plt.title(r'Trajectory of the point mass (h=%.2e)'%abs(t[1]-t[0]), size=21)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.savefig('8_1.png')
plt.show()

"""
Output:

RK4 Integrator took 104.17 seconds
    
"""

t = np.linspace(0,24,100) #Time in code units
x0 = [4e12/UNIT_LENGTH,0,0,500/UNIT_VELOCITY] #x, vx, y, vy
Msun = 2e30/(UNIT_DENSITY*UNIT_LENGTH**3)
delta = (1e3/(365*24*60**2))/UNIT_VELOCITY # 1 km/yr
elapsed = time.time()
t, soln = RK4.RK4_adaptive(f,x0,t,delta,Msun)
elapsed = time.time() - elapsed
print('Adaptive RK4 Integrator took %.2f seconds'%elapsed)

plt.figure(figsize=(13,10))
plt.plot(soln[0],soln[2])
plt.plot(soln[0],soln[2],'o',color='red',markersize=2)
#plt.plot(soln[0],soln[2], color='green', marker='o', linestyle='dashed',linewidth=2, markersize=5)
plt.grid()
plt.ylabel(r'y (AU)',size=18)
plt.xlabel(r'x (AU)',size=20)
plt.title(r'Trajectory of the point mass (Adaptive RK4)', size=21)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.savefig('8_2.png')
plt.show()

"""
Output:

Adaptive RK4 Integrator took 0.45 seconds
    
"""