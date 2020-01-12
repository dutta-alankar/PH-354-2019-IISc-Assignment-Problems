#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 21:22:51 2019

@author: alankar
"""

#import numpy as np
#import matplotlib.pyplot as plt

def simpson(func, a, b, n,*args):
    h=(b-a)/n
    k=0.0
    x=a + h
    for i in range(1,int(n/2) + 1):
        k += 4*func(x,*args)
        x += 2*h

    x = a + 2*h
    for i in range(1,int(n/2)):
        k += 2*func(x,*args)
        x += 2*h
    return (h/3)*(func(a,*args)+func(b,*args)+k)

def trapezoidal(func, a, b, n,*args):
    h = float(b - a) / n
    s = 0.0
    s += func(a,*args)/2.0
    for i in range(1, n):
        s += func(a + i*h,*args)
    s += func(b,*args)/2.0
    return s * h


f = lambda x:x**4-2*x+1

print('\n\nTRAPEZOIDAL RULE:')
n = 10
print('Slices = %d'%n)
I1 = trapezoidal(f,0,2,n)

n = 20
I2 = trapezoidal(f,0,2,n)

print('Fractional error estimate: %e'%abs((I2-I1)/I2))

"""
The results vary from the actual esult comparison of problem 2 for N=10 
because of the truncation error associated with both I1 and I2.
I2 is closer to actual value but still off by the truncation error (which is smaller than I1)
"""