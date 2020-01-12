#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 19:11:24 2019

@author: alankar
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x*(x-1)

def derv(func,x, delta=1.e-2):
    return (func(x+delta)-func(x))/delta

def fprime(x):
    return 2*x-1

print("f(x)=x(x-1)\nAt x=1,")
print("Numerical derivative (Forward Difference): %f"%derv(f,1))
print("Analytical Derviative: %f"%fprime(1))
print("Relative Error: %e"%np.abs((derv(f,1)-fprime(1))/fprime(1)))
print("This arises as a truncation error as an approximation for the derivative using Forward difference.")

y = []
for delta in np.array([2,4,6,8,10,12,14]):
    y.append(np.abs((derv(f,1,delta=1/10**delta)-fprime(1))/fprime(1)))
    
plt.plot(-np.array([2,4,6,8,10,12,14]),np.log10(y))
plt.xlabel(r'$\log_{10}(h)$', size=20)
plt.ylabel(r'$\log_{10}\left(\left|\frac{f^{(1)}_{analytic}-f^{(1)}_{numerical}}{f^{(1)}_{analytic}}\right|\right)$', size=20)
plt.title('Relative Error as a function of step size',size=20)
plt.grid()
#plt.savefig('error.jpg')
plt.show()

"""
Output
f(x)=x(x-1)
At x=1,
Numerical derivative (Forward Difference): 1.010000
Analytical Derviative: 1.000000
Relative Error: 1.000000e-02
This arises as a truncation error as an approximation for the derivative using Forward difference.
"""