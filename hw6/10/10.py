#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 19:29:29 2019

@author: alankar
"""

import numpy as np
import matplotlib.pyplot as plt
import RK4
import verlet as VLET

#Relation of code units with SI units
UNIT_LENGTH = 1.496e11 #AU -> m
UNIT_VELOCITY = 1e3 #kms^-1 -> ms^-1
UNIT_DENSITY = 1e3 # kgm^-3

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

t = np.linspace(0,1.0,100) #Time in code units
x0 = [1.4710e11/UNIT_LENGTH,0,0,3.0287e4/UNIT_VELOCITY] #x, vx, y, vy
Msun = 1.9891e30/(UNIT_DENSITY*UNIT_LENGTH**3)
delta = (1e3/(365*24*60**2))/UNIT_VELOCITY # 1 km/yr
t,soln = RK4.RK4_adaptive(f,x0,t,delta,Msun)


plt.figure(figsize=(10,10))
plt.plot(soln[0],soln[2])
plt.grid()
plt.ylabel(r'y (AU)',size=18)
plt.xlabel(r'x (AU)',size=20)
plt.title(r'Trajectory of the Earth (Adaptive RK4)', size=21)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.savefig('10_1.png')
plt.show()

t = np.linspace(0,0.6,100000) #Time in code units
soln = VLET.VLET(f,x0,t,Msun)

plt.figure(figsize=(10,10))
plt.plot(soln[0],soln[2])
plt.grid()
plt.ylabel(r'y (AU)',size=18)
plt.xlabel(r'x (AU)',size=20)
plt.title(r'Trajectory of the Earth (Verlet)', size=21)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.savefig('10_2.png')
plt.show()

sampling = 1/(t[1]-t[0])
period = 1/(np.argmax(np.abs(np.fft.fft(soln[0]))[:len(t)//2])*sampling/len(t))

Mearth = 5.9722e24/(UNIT_DENSITY*UNIT_LENGTH**3)
U = -G*Msun*Mearth/np.sqrt(soln[0]**2+soln[2]**2)
T = (1/2)*Mearth*(soln[1]**2+soln[3]**2)
E = T+U
joule = (UNIT_DENSITY*UNIT_LENGTH**3)*UNIT_LENGTH**2*(UNIT_LENGTH/UNIT_VELOCITY)**(-2)
E *= joule
T *= joule
U *= joule
t *= (UNIT_LENGTH/UNIT_VELOCITY)/(24*60**2) #days
period *= (UNIT_LENGTH/UNIT_VELOCITY)/(24*60**2) #days

print('Orbital period is about %.2f days'%period)

plt.figure(figsize=(13,10))
plt.plot(t,U,label='Gravitational Potential Energy')
plt.plot(t,T,label='Kinetic Energy')
plt.plot(t,E,label='Total Energy')
plt.grid()
plt.ylabel(r'Energy (Joule)',size=18)
plt.xlabel(r't (days)',size=20)
plt.title(r'Energy of the System', size=21)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.legend(loc='best',prop={'size': 18})
plt.savefig('10_3.png')
plt.show()

"""
Output:
    
   Orbital period is about 346.30 days
    
"""