#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 12:15:06 2019

@author: alankar
"""

import numpy as np
import matplotlib.pyplot as plt
import RK4

def f(t,x,alpha,beta,gamma,delta):
    x, y = x
    xdot = alpha*x-beta*x*y
    ydot = gamma*x*y - delta*y
    return np.array([[xdot,ydot]]).T

t = np.linspace(0,30,100000)
x0 = [2,2]
pop = RK4.RK4(f,x0,t,1,0.5,0.5,2.)

plt.figure(figsize=(13,10))
plt.plot(t,pop[0],label = 'Prey Population')
plt.grid()
plt.ylabel(r'Population',size=18)
plt.xlabel(r'time',size=20)
plt.title(r'Lotka Volterra Model', size=21)

plt.plot(t,pop[1],label='Predator Population')
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.legend(loc='best',prop={'size': 18})
plt.savefig('2_1.png')
plt.show()

plt.figure(figsize=(13,10))
plt.plot(pop[0],pop[1],label='Initial Population\nPredator: %d Prey: %d'%(int(x0[1]),int(x0[0])))
plt.grid()
plt.ylabel(r'Prey Population',size=18)
plt.xlabel(r'Predator Population',size=20)
plt.title(r'Lotka Volterra Model Phase Diagram', size=21)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.legend(loc='best',prop={'size': 18})
plt.savefig('2_2.png')
plt.show()

