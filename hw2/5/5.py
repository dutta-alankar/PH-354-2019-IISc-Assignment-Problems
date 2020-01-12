#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 10:09:13 2019

@author: alankar
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x,y,a,b):
    return y*(a+x**2)

def g(x,y,a,b):
    return b/(a+x**2)

a = 1.
b = 2.

x_new, x_old = 1., 0.
y_new, y_old = 1., 0.
tol = 1e-6
Nmax = 1000
counter = 0
x = []
y = []

while ((np.abs(x_new-x_old)>tol or np.abs(y_new-y_old)>tol) and (counter<Nmax)):
    x_old = x_new
    y_old = y_new
    x.append(x_old)
    y.append(y_old)
    x_new = f(x_old,y_old,a,b)
    y_new = g(x_old,y_old,a,b)
    counter += 1
    if (counter==Nmax): print('Didn\'t converge!')
 
    
"""
#plt.plot(np.arange(1,counter+1,1),np.array(x),label ='numerical x-value in each step')
plt.plot(np.arange(1,counter+1,1),np.array(y),label ='numerical y-value in each step')
#plt.plot(np.arange(1,counter+1,1),np.ones(counter)*b,label='analytic x-value')
plt.plot(np.arange(1,counter+1,1),np.ones(counter)*b/(a+b**2),label='analytic y-value')
plt.xlabel('Step', size=18)
plt.ylabel('value', size=18)
plt.title('Oscillating y-value about the true value', size=20)
plt.grid()
plt.legend(loc='best', prop={'size': 16})
plt.show()
"""    
    
print('Rearranging... Resetting the equations...')
#Rearranging the equations
def fnew1(x,y,a,b):
    return np.sqrt(b/y-a)

def fnew2(x,y,a,b): 
    return -np.sqrt(b/y-a)

def gnew(x,y,a,b):
    return x/(a+x**2)

x_new, x_old = 1., 0.
y_new, y_old = 1., 0.
tol = 1e-6
Nmax = 1000
counter = 0
x = []
y = []

while ((np.abs(x_new-x_old)>tol or np.abs(y_new-y_old)>tol) and (counter<Nmax)):
    x_old = x_new
    y_old = y_new
    x.append(x_old)
    y.append(y_old)
    x_new = fnew1(x_old,y_old,a,b) #Replacing fnew1 by fnew2 didn't converge
    y_new = gnew(x_old,y_old,a,b)
    counter += 1
    if (counter==Nmax): print('Didn\'t converge!')
    
print('x = %.2f  y = %.2f'%(x_new,y_new))

"""
plt.plot(np.arange(1,counter+1,1),np.array(x),label ='numerical x-value in each step')
#plt.plot(np.arange(1,counter+1,1),np.array(y),label ='numerical y-value in each step')
plt.plot(np.arange(1,counter+1,1),np.ones(counter)*b,label='analytic x-value')
#plt.plot(np.arange(1,counter+1,1),np.ones(counter)*b/(a+b**2),label='analytic y-value')
plt.xlabel('Step', size=18)
plt.ylabel('value', size=18)
plt.title('Converging x-value to the true value', size=20)
plt.grid()
plt.legend(loc='best', prop={'size': 16})
plt.show()
"""


"""
Output

Didn't converge!
Rearranging... Resetting the equations...
x = 2.00  y = 0.40
"""