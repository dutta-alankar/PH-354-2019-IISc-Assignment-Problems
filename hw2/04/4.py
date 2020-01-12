#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 13:31:03 2019

@author: alankar
"""
import numpy as np
import matplotlib.pyplot as plt

def f(x,c):
    return 1-np.exp(-c*x)

def fpi(func,x0, tol, verbose, *args): #x0 is initial guess
    x_old = x0
    x_new = x0+10  #some arbitrary initialization
    counter = 0
    while(np.abs(x_new-x_old)>=tol):
        counter += 1
        x_old = x_new
        x_new = func(x_old,*args)
    if (verbose==True): print ("Converged in %d steps"%counter)
    return x_new

c = 2
print('Fixed Point Iteration:')
print('Solution for x=1-exp(-%.2f x) is: x=%f\n'%(c,fpi(f,0.5,1e-6,True,c)))

c = np.arange(0,3,0.01)
x = np.zeros(len(c))
for i in range(len(c)):
    x[i] = fpi(f,0.5,1e-6,False,c[i])

plt.plot(c,x)
plt.grid()
plt.xlabel('c',size=18)
plt.ylabel('x',size=18)
#plt.savefig('tansition.jpg')

def steffensen_fpi(func,x0, tol, verbose, *args):
    x_old = x0
    x_new = x0+10  #some arbitrary initialization
    counter = 0
    while(np.abs(x_new-x_old)>=tol):
        counter +=1
        x_old = x_new
        g = (func(func(x_old,*args),*args)-func(x_old,*args))/(func(x_old,*args)-x_old)-1
        x_new = x_old-(func(x_old,*args)-x_old)/g
    if (verbose==True): print ("Converged in %d steps"%counter)
    return x_new

c = 2
print('Accelerated Fixed Point Iteration')
print('Solution for x=1-exp(-%.2f x) is: x=%f'%(c,steffensen_fpi(f,0.5,1e-6,True,c)))

plt.show()

"""
Output

Fixed Point Iteration:
Converged in 15 steps
Solution for x=1-exp(-2.00 x) is: x=0.796813

Accelerated Fixed Point Iteration
Converged in 4 steps
Solution for x=1-exp(-2.00 x) is: x=0.796812
"""