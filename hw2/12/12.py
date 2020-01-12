#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 11:24:09 2019

@author: alankar
"""
import numpy as np

def NR_sec(func,x0,N_max,*args): #Newton Raphson
    x_new = 0.
    x_old = x0
    counter = 0
    while(counter<N_max):
        counter += 1
        #x_new = x_old[1]-func(x_old[1],*args)*((x_old[1]-x_old[0])/(func(x_old[1],*args)-func(x_old[1],*args)))
        x_new = (x_old[0]*func(x_old[1],*args)-x_old[1]*func(x_old[0],*args))/(func(x_old[1],*args)-func(x_old[0],*args))
        x_old[0] = x_old[1]
        x_old[1] = x_new
    return x_new


def f(x):
    return 5*x**3-7*x**2-40*x+100
"""
def f(x):
    return x**2-9
"""
N = 27
XNp1 = NR_sec(f,[4.,5.],N+1)
XN = NR_sec(f,[4.,5.],N)
XNm1 = NR_sec(f,[4.,5.],N-1)
XNm2 = NR_sec(f,[4.,5.],N-2)

alpha = np.log10(np.abs((XNp1-XN)/(XN-XNm1)))/np.log10(np.abs((XN-XNm1)/(XNm1-XNm2)))
print("Rate of convergence of secant method is %.2f"%alpha)

"""
Output

Rate of convergence of secant method is 1.62
"""