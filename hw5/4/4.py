#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 15:18:57 2019

@author: alankar
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2,1000)
f = lambda x:np.sin(1/(x*(2-x)))**2

plt.figure(figsize=(13,10))
plt.plot(x,f(x))
plt.grid()
plt.xlabel(r'$x$',size=18)
plt.ylabel(r'$f(x)$',size=20)
plt.title(r'Integrand', size=21)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.savefig('4.png')
plt.show()

N = int(1e4)
x = np.random.uniform(low=0,high=2.0,size=N)
y = np.random.uniform(low=0.,high=1.0,size=N)
A = 2.*1.
I = (np.count_nonzero(np.array(y<=f(x),dtype=np.int32))/N)*A
error = np.sqrt(I*(A-I)/N)
print('Monte Carlo Hit-Miss Algorithm')
print('Integral: %f'%I)
print('Error: %e'%error)

print()
I = ((2.-0.)/N)*np.sum(f(x))
varf = (1/N)*np.sum(f(x)**2)-(I/(2.-0.))**2
error = (2.-0.)*np.sqrt(varf/N)
print('Monte Carlo Mean Value Algorithm')
print('Integral: %f'%I)
print('Error: %e'%error)


"""
Output:
    
Monte Carlo Hit-Miss Algorithm
Integral: 1.456000
Error: 8.899798e-03

Monte Carlo Mean Value Algorithm
Integral: 1.453037
Error: 5.308131e-03
"""