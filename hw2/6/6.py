#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 20:17:21 2019

@author: alankar
"""

import numpy as np
import scipy.constants as const
import matplotlib.pyplot as plt

def I(wav,T):
    wavelength = np.copy(wav)
    wavelength *= 1e-9 #in nm
    T *= 1e3   #in 10^3 K
    return (2*np.pi*const.h*const.c**2*wavelength**(-5))/(np.exp(const.h*const.c/(wavelength*const.k*T))-1)

def dfdl(wav,T,delta):
    return (I(wav+delta,T)-I(wav-delta,T))/(2*delta)

def bisection(f,a,b,tol,*args):
    c = 0.
    while(np.abs((b-a)/2)>=tol):
        c = (a+b)/2
        if (f(c,*args)*f(a,*args)>=0): a = c
        else: b = c
    return (a+b)/2

T = np.linspace(4,6,100)
lambda_max = np.zeros(len(T))
for i in range(len(T)):
    lambda_max[i] = bisection(dfdl,10,10000,1e-6,T[i],1e-2)
    
plt.plot(1/(T*1e3),lambda_max,label="Wien displacement constant [slope] (SI): %.10f"%np.average(lambda_max*1e-9*T*1e3))
plt.grid()
plt.xlabel(r'$\frac{1}{T [K]}$',size = 23)
plt.ylabel(r'$\lambda_{max} [nm]$',size = 18)
plt.legend(loc='best', prop={'size': 16})
plt.show()
print("Wien displacement constant (SI): %.10f"%np.average(lambda_max*1e-9*T*1e3))
print('Wavelength = 502 nm Temperature = %d K'%(np.average(lambda_max*1e-9*T*1e3)/(502*1e-9)))

"""
Output

Wien displacement constant (SI): 0.0028977729
Wavelength = 502 nm Temperature = 5772 K
"""