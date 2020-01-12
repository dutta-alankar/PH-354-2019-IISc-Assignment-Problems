#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 21:45:48 2019

@author: alankar
"""
import numpy as np
import os

def trapezoidal(func, a, b, n,*args):
    h = float(b - a) / n
    s = 0.0
    s += func(a,*args)/2.0
    for i in range(1, n):
        s += func(a + i*h,*args)
    s += func(b,*args)/2.0
    return s * h

def romberg(func, a, b, n,verbose,*args): #approximation error of order 2n
    file = open('Romberg Triangle.txt','a')
    h = float(b - a)
    T = np.zeros((n+1,n+1))
    if verbose: file.write('Romberg Triangular matrix: N = %d\n'%n)
    for j in range(1,n+1):
        T[j,1] = (h/2)*(func(a,*args)+2*np.sum(func(a+np.arange(h,int(2**(j-1))*h,h),*args))+func(b,*args)) #Comp Trapz
        if verbose: file.write('%f  '%T[j,1])
        for k in range(2,j+1):
            T[j,k] = T[j,k-1]+(T[j,k-1]-T[j-1,k-1])/(4**(k-1)-1) #Richardson Extrp
            if verbose: file.write('%f  '%T[j,k])
        if verbose: file.write('\n')
        h/=2
    if verbose: file.write('\n\n')
    if verbose: file.close()
    return T[n,n]


f = lambda x:np.sin(np.sqrt(100*x))**2

tol = 1e-6

n = 1
I_old = 0
I_new = trapezoidal(f,0,1,n)

print('TRAPEZOIDAL INTEGRATION (ADAPTIVE):')
while (abs(I_new-I_old)>tol):
    n *= 2
    print('Slices = %d'%n)
    I_old = I_new
    I_new = trapezoidal(f,0,1,n)
    print('I = %.7f'%I_new)
    print('Fractional error estimate: %e'%abs((I_new-I_old)/I_new))

n = 1
I_old = 0
I_new = romberg(f,0,1,n,True)
os.remove('Romberg Triangle.txt')

print('\n\nROMBERG INTEGRATION:')
while (abs(I_new-I_old)>tol):
    n *= 2
    print('Slices = %d'%n)
    I_old = I_new
    I_new = romberg(f,0,1,n,True)
    print('I = %.7f'%I_new)
    print('Fractional error estimate: %e'%abs((I_new-I_old)/I_new))
    
"""
Output:

TRAPEZOIDAL INTEGRATION (ADAPTIVE):
Slices = 2
I = 0.3252319
Fractional error estimate: 5.450032e-01
Slices = 4
I = 0.5122829
Fractional error estimate: 3.651322e-01
Slices = 8
I = 0.4029974
Fractional error estimate: 2.711814e-01
Slices = 16
I = 0.4301034
Fractional error estimate: 6.302188e-02
Slices = 32
I = 0.4484147
Fractional error estimate: 4.083563e-02
Slices = 64
I = 0.4539129
Fractional error estimate: 1.211304e-02
Slices = 128
I = 0.4553485
Fractional error estimate: 3.152691e-03
Slices = 256
I = 0.4557113
Fractional error estimate: 7.960349e-04
Slices = 512
I = 0.4558022
Fractional error estimate: 1.995014e-04
Slices = 1024
I = 0.4558249
Fractional error estimate: 4.990618e-05
Slices = 2048
I = 0.4558306
Fractional error estimate: 1.247847e-05
Slices = 4096
I = 0.4558321
Fractional error estimate: 3.119738e-06
Slices = 8192
I = 0.4558324
Fractional error estimate: 7.799420e-07


ROMBERG INTEGRATION:
Slices = 2
I = 0.3843160
Fractional error estimate: 6.149537e-01
Slices = 4
I = 0.3489739
Fractional error estimate: 1.012746e-01
Slices = 8
I = 0.4558325
Fractional error estimate: 2.344253e-01
Slices = 16
I = 0.4558325
Fractional error estimate: 8.931689e-12
"""