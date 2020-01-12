#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 18:53:31 2019

@author: alankar
"""

import numpy as np
import matplotlib.pyplot as plt
import RK4
import leapfrog as LF

def f(t,x): 
    x, y = x
    xdot = y
    ydot = y**2 - x - 5
    return np.array([[xdot,ydot]]).T

t = np.arange(0,50,0.001)
x0 = [1,0]
soln = RK4.RK4(f,x0,t)

plt.figure(figsize=(13,10))
plt.plot(t,soln[0])
plt.grid()
plt.ylabel(r'x',size=18)
plt.xlabel(r't',size=20)
plt.title(r'Solution (RK4)', size=21)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.savefig('9_1.png')
plt.show()

soln = LF.LF(f,x0,t)

plt.figure(figsize=(13,10))
plt.plot(t,soln[0])
plt.grid()
plt.ylabel(r'x',size=18)
plt.xlabel(r't',size=20)
plt.title(r'Solution (Leapfrog)', size=21)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.savefig('9_2.png')
plt.show()
