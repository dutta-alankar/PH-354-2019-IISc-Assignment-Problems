#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 19:41:58 2019

@author: alankar
"""
import numpy as np


def func(z):
    z1, z2 = z[0], z[1]
    equations = []
    equations.append( z2**2*(1-z1) - z1**3 )
    equations.append( z1**2 + z2**2 -1 )
    return np.array(equations).T

def jac(z):
    z1, z2 = z[0], z[1]
    J = np.array( [
                  [-z2**2-3*z1**2,    2*z2*(1-z1)],
                  [ 2*z1,                2*z2] ])
    return J

tol = 1e-6

z_new = np.array([-1.6+0.j,0.8+0.j])
z_old = np.array([0.+0.j,0.+0.j])
 
while( np.abs(z_old[0]-z_new[0])>tol or np.abs(z_old[1]-z_new[1])>tol ):
    z_old = z_new
    equations = func(z_old)
    delz = np.linalg.solve(jac(z_old),-equations)
    z_new = z_old + delz.T
    
print('Roots are: ')
for i in range(len(z_new)):
    print('z%d = '%(i+1),end='')
    if (np.abs(z_new[i].real) >=tol): print(" %.2f"%z_new[i].real,end='')
    if((np.abs(z_new[i].real) >=tol) and (np.abs(z_new[i].imag) >=tol)): print(' + ',end='')
    if (np.abs(z_new[i].imag) >=tol): print("%.2f i"%z_new[i].imag)
    print('')
    
"""
Output

Roots are: 
z1 =  -1.62
z2 = 1.27 i
"""