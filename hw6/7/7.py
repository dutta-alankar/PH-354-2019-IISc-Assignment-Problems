#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 10:08:28 2019

@author: alankar
"""

import numpy as np
import matplotlib.pyplot as plt
import RK4

def f(t,x,m,k,F): #F is an array of functions of time
    pos = [x[i] for i in range(0,len(x),2)]
    vel = [x[i] for i in range(1,len(x),2)]
    acc = [(k/m)*(pos[i+1]-pos[i])+F[i](t) for i in range (0,len(pos)-1)]
    acc.append((k/m)*(pos[len(pos)-2]-pos[len(pos)-1])+F[len(pos)-1](t))
    vector = np.zeros((2*len(pos),1))
    counter = 0
    for i in range(0,2*len(pos),2):
        vector[i] = vel[counter]
        vector[i+1] = acc[counter]
        counter += 1
    return vector

N = 5
omega = 2
m = 1
k = 6
F = [lambda t:0 for i in range(0,N)]
F[0] = lambda t: np.cos(omega*t)

t = np.linspace(0,20,10000)
x0 = [1,-1,2,8,3,-4,4,3,5,6] #x1, v1, x2, v2, ...... 
soln = RK4.RK4(f,x0,t,m,k,F)

plt.figure(figsize=(13,10))
for i in range(0,N):
    plt.plot(t,soln[2*i],label=r'Body %d'%(i+1))
plt.grid()
plt.ylabel(r'Position',size=18)
plt.xlabel(r'Time',size=20)
plt.title(r'Coupled oscillator', size=21)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.legend(loc='best',prop={'size': 18})
plt.savefig('7_1.png')
plt.show()