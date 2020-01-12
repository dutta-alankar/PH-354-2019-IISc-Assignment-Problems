#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 12:40:30 2019

@author: alankar
"""

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

print('SIMPSON RULE:')
n = 10
print('Slices = %d'%n)
print('Fractional error is %e\n'%abs((simpson(f,0,2,n)-4.4)/4.4))

n = 100
print('Slices = %d'%n)
print('Fractional error is %e\n'%abs((simpson(f,0,2,n)-4.4)/4.4))

n = 1000
print('Slices = %d'%n)
print('Fractional error is %e\n'%abs((simpson(f,0,2,n)-4.4)/4.4))


print('\n\nTRAPEZOIDAL RULE:')
n = 10
print('Slices = %d'%n)
print('Fractional error is %e\n'%abs((trapezoidal(f,0,2,n)-4.4)/4.4))

n = 100
print('Slices = %d'%n)
print('Fractional error is %e\n'%abs((trapezoidal(f,0,2,n)-4.4)/4.4))

n = 1000
print('Slices = %d'%n)
print('Fractional error is %e\n'%abs((trapezoidal(f,0,2,n)-4.4)/4.4))

"""
Output:
    
    
SIMPSON RULE:
Slices = 10
Fractional error is 9.696970e-05

Slices = 100
Fractional error is 9.696972e-09

Slices = 1000
Fractional error is 9.735647e-13



TRAPEZOIDAL RULE:
Slices = 10
Fractional error is 2.421818e-02

Slices = 100
Fractional error is 2.424218e-04

Slices = 1000
Fractional error is 2.424242e-06
"""