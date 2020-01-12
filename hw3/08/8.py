#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 12:27:27 2019

@author: alankar
"""

import numpy as np


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


f = lambda x:np.sin(np.sqrt(100*x))**2

tol = 1e-6

n = 1
I_old = 0
I_new = simpson(f,0,1,n)

print('SIMPSON INTEGRATION: ')
while (abs(I_new-I_old)>tol):
    n *= 2
    print('Slices = %d'%n)
    I_old = I_new
    I_new = simpson(f,0,1,n)
    print('I = %.7f'%I_new)
    print('Fractional error estimate: %e'%abs((I_new-I_old)/I_new))