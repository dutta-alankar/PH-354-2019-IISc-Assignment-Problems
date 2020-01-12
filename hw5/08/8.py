#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 01:30:20 2019

@author: alankar
"""

import numpy as np
import matplotlib.pyplot as plt


def MCMC_SA(func,x0,steps,limit,T = 1,*args):
    #Gaussian jumping distribution is assumed
    kB = 1
    pos = np.zeros(steps+1,dtype=np.float64)
    pos[0] = x0
    xold = x0
    xnew = x0
    Eold = func(xold,*args)
    delT = -10/steps
    for i in range(steps):
        counter = 0
        while (not(xnew>=limit[0] and xnew<=limit[1]) or counter==0):
            counter += 1
            delta = np.random.normal(loc=0.,scale=1.,size=1)[0]
            xnew = xold+delta
        Enew = func(xnew,*args)
        alpha = np.exp(-(Enew-Eold)/(kB*T))
        u = np.random.uniform(low=0.,high=1.,size=1)
        if (u>alpha): #reject
            xnew = xold
            pos[i+1] = xold
            Enew=Eold
        else: #accept
            pos[i+1] = xnew
            Eold=Enew
            xold = xnew
        while (T+delT<=0): delT/=2
        T += delT
    return pos


f = lambda x:x**2-np.cos(4*np.pi*x)
steps = int(1.e6)
walker = MCMC_SA(f,8.,steps,[-15.,15.])
burn_in = int((10/100)*steps)
x = np.average(walker[burn_in:])
error = np.std(walker[burn_in:])

plt.figure(figsize=(13,10))
plt.plot(np.arange(0,steps+1,1),walker)
plt.grid()
plt.xlabel(r'MCMC step',size=18)
plt.ylabel(r'Walker position',size=20)
plt.title(r'Global Minima search by Simulated Annealing', size=21)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.savefig('8_1.png')
plt.show()
print('Minima at: %.1f'%x)
print('Error estimate: %.2e'%error)

f = lambda x:np.cos(x)+np.cos(np.sqrt(2)*x)+np.cos(np.sqrt(3)*x)
steps = int(1.e6)
walker = MCMC_SA(f,25.,steps,[0.,50.])
burn_in = int((10/100)*steps)
x = np.average(walker[burn_in:])
error = np.std(walker[burn_in:])

plt.figure(figsize=(13,10))
plt.plot(np.arange(0,steps+1,1),walker)
plt.grid()
plt.xlabel(r'MCMC step',size=18)
plt.ylabel(r'Walker position',size=20)
plt.title(r'Global Minima search by Simulated Annealing', size=21)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.savefig('8_2.png')
plt.show()
print('Minima at: %.1f'%x)
print('Error estimate: %.2e'%error)

"""
Output:
    
Minima at: 0.0
Error estimate: 7.86e-05

￼
Minima at: 16.0
Error estimate: 1.01e-04

"""