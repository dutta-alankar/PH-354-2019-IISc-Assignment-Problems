#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 15:25:22 2019

@author: alankar
"""

import numpy as np
import matplotlib.pyplot as plt

def simpson(func, n,*args): #Integrate from args[0] to args[1]
    h=(args[1]-args[0])/n
    k=0.0
    t=args[0] + h
    for i in range(1,int(n/2) + 1):
        k += 4*func(t,*args[2:])
        t += 2*h

    t = args[0] + 2*h
    for i in range(1,int(n/2)):
        k += 2*func(t,*args[2:])
        t += 2*h
    return (h/3)*(func(args[0],*args[2:])+func(args[1],*args[2:])+k)

f = lambda t:np.exp(-t**2)

x = np.arange(0,5,0.1)
E = simpson(f,100,0.,x)

plt.figure(figsize=(13,10))
plt.plot(x,E)
plt.grid()
plt.xlabel(r'$x$',size=22)
plt.ylabel(r'$E(x)=\int_0^x \exp (-t^2) dt$',size=22)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.savefig('3.png')
plt.show()