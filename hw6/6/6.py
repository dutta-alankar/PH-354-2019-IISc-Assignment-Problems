#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 09:38:46 2019

@author: alankar
"""

import numpy as np
import matplotlib.pyplot as plt
import RK4

G = 1
def f(t,x,M,L): #Quadratic drag model
    x, x1, y, x2 = x
    r = np.sqrt(x**2+y**2)
    denom = r**2*np.sqrt(r**2+(L/2)**2)
    xdot = x1
    ydot = x2
    x1dot = -G*M * x/denom
    x2dot = -G*M * y/denom
    return np.array([[xdot,x1dot,ydot,x2dot]]).T

t = np.linspace(0,10,100000)
x0 = [1,0,0,1] #x, vx, y, vy
M = 10
L = 2
soln = RK4.RK4(f,x0,t,M,L)

plt.figure(figsize=(13,10))
plt.plot(soln[0],soln[2])
plt.grid()
plt.ylabel(r'y',size=18)
plt.xlabel(r'x',size=20)
plt.title(r'Trajectory of the point mass', size=21)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.savefig('6_1.png')
plt.show()