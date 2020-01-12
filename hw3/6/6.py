#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 21:41:08 2019

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

f = lambda x:x**4-2*x+1

print('\n\nSIMPSON RULE:')
n = 10
print('Slices = %d'%n)
I1 = simpson(f,0,2,n)

n = 20
I2 = simpson(f,0,2,n)

print('Fractional error estimate: %e'%abs((I2-I1)/I2))

"""
The results vary from the actual esult comparison of problem 2 for N=10 
because of the truncation error associated with both I1 and I2.
I2 is closer to actual value but still off by the truncation error (which is smaller than I1)
"""