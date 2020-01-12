#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 15:41:38 2019

@author: alankar
"""

import numpy as np

def NR_sec(func,x0,tol,verbose,*args): #Newton Raphson
    x_new = 0.
    x_old = x0
    counter = 0
    while(np.abs(x_new-x_old[0])>=tol):
        counter += 1
        #x_new = x_old[1]-func(x_old[1],*args)*((x_old[1]-x_old[0])/(func(x_old[1],*args)-func(x_old[1],*args)))
        x_new = (x_old[0]*func(x_old[1],*args)-x_old[1]*func(x_old[0],*args))/(func(x_old[1],*args)-func(x_old[0],*args))
        x_old[0] = x_old[1]
        x_old[1] = x_new
    if (verbose==True): print("Converged in %d steps"%counter)
    return x_new

omega = 2.662e-6
R = 3.844e8
Mm = 7.348e22
Me = 5.974e24
G = 6.674e-11

def lagr1(r):
    r *= 1e8 #in units of 10^8 m
    return -(omega**2*r)-((G*Me)/r**2)+((G*Mm)/(R-r)**2)

print('Distance of Earth-Moon L1 from earth')
print("r = %.2e AU"%(NR_sec(lagr1,np.array([3.4,3.6]),1e-6,False)*1e8/1.496e+11)) # agrees with the value of L1 for Earth-Moon system available on literature

"""
Output

Distance of Earth-Moon L1 from earth
r = 2.37e-03 AU
"""