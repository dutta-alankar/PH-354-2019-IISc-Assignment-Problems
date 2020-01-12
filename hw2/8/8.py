#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 14:21:06 2019

@author: alankar
"""

import numpy as np
import matplotlib.pyplot as plt

def derivative(func,x,*args): #function to find the derivative of the polynomial
    h = 1e-4
    derivative = (func(x + h,*args) - func(x-h,*args)) / (2*h)
    return derivative

def NR(func,x0,tol,*args): #Newton Raphson
    x_new = 0
    x_old = x0
    while(np.abs(x_new-x_old)>=tol):
        x_new = x_old - func(x_old,*args)/derivative(func,x_old,*args)
        x_old = x_new
    return x_new

def f(x):
    return 924*x**6-2772*x**5+3150*x**4-1680*x**3+420*x**2-42*x+1

x = np.linspace(0,1,500)
plt.plot(x,f(x))
plt.xlabel(r'$x$',size=18)
plt.ylabel(r'$f(x)=924x^6-2772x^5+3150x^4-1680x^3+420x^2-42x+1$',size=18)
plt.grid()
#plt.savefig('poly.png')
plt.show()

print ('Roots are ')
x0 = [0.03,0.17,0.38,0.62,0.83,0.97]
for i in range(len(x0)):
    print( '%.10f'%NR(f,x0[i],1.e-10))

"""
Output

Roots are 
0.0335761962
0.1693944272
0.3806901845
0.6193098155
0.8306055728
0.9664238038
"""