#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 21:12:09 2019

@author: alankar
"""

import numpy as np

def TrapzC(func,m,N,*args):
    k = np.arange(0,N+1,1)
    z = np.exp((2*np.pi*k/N)*1.j)
    return (np.math.factorial(m)/N)*np.sum(func(z,*args)*np.exp(-(2*np.pi*k*m/N)*1.j))

f = lambda z: np.exp(2*z)
N = 100000

for m in range(0,7):
    print('Order: %d          '%m,end='')
    print('Derivative Value: ',end='')
    derv = TrapzC(f,m,N)
    if (np.real(derv)>1e-6):
        print('%d'%int(np.real(derv)),end='')
        if (np.imag(derv)>1e-6):print('+',end='')
    if (np.imag(derv)>1e-6):print('%d'%int(np.imag(derv)),end='j')
    print('')