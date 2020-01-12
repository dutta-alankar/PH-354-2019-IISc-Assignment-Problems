#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:34:02 2019

@author: alankar
"""

import numpy as np
import matplotlib.pyplot as plt
import RK4

def f(t,x,sigma,r,b):
    x, y, z = x
    xdot = sigma*(y-x)
    ydot = r*x - y - x*z
    zdot = x*y - b*z
    return np.array([[xdot,ydot,zdot]]).T

t = np.linspace(0,50,100000)
x0 = [0,1,0]
soln = RK4.RK4(f,x0,t,10,28,8/3)

plt.figure(figsize=(13,10))
plt.plot(t,soln[1],label=r'$(\sigma,r,b)=(10,28,\frac{8}{3}$)')
plt.grid()
plt.ylabel(r'y',size=18)
plt.xlabel(r'time',size=20)
plt.title(r'Lorenz Equation', size=21)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.legend(loc='best',prop={'size': 18})
plt.savefig('3_1.png')
plt.show()

plt.figure(figsize=(13,10))
plt.plot(soln[0],soln[2],label='Initial Condition\n(x,y,z)=(%.1f,%.1f,%.1f)'%(x0[0],x0[1],x0[2]))
plt.grid()
plt.ylabel(r'z',size=18)
plt.xlabel(r'x',size=20)
plt.title(r'Lorenz Equation Phase Diagram', size=21)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.legend(loc='best',prop={'size': 18})
plt.savefig('3_2.png')
plt.show()
