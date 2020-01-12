#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 16:36:43 2019

@author: alankar
"""

import numpy as np
from scipy.special.orthogonal import p_roots #Legendre Polynomial roots
from scipy import constants

def gauss_quad(func,a,b,n,*args):#Legendre
    [x,w] = p_roots(n+1)
    I_G = 0.5*(b-a)*np.sum(w*func(0.5*(b-a)*x+0.5*(b+a),*args))
    return I_G

N = 100

integ = lambda theta:(np.tan(theta)**3/np.cos(theta)**2)/(np.exp(np.tan(theta))-1)

T  = 1e3
print('Using %d points Gaussian (Legendre) Quadrature (T=%.1f K):\n'%(N,T))
W = ((constants.k**4*T**4)/(4*np.pi**2*constants.c**2*constants.hbar**3))*gauss_quad(integ,0,np.pi/2,N)
error = np.abs(((constants.k**4*T**4)/(4*np.pi**2*constants.c**2*constants.hbar**3))*gauss_quad(integ,0,np.pi/2,20*N)-W)
print('W = %6e W⋅m^−2\nError Estimate: %.4e\n'%(W,error))
print('Stefan-Boltzmann Constant Calculated: %.6e W⋅m^−2⋅K^−4'%(W/T**4))
print('Stefan-Boltzmann Constant from Literature: %.e W⋅m^−2⋅K^−4\n'%constants.Stefan_Boltzmann)

"""
Output:
    
Using 100 points Gaussian (Legendre) Quadrature (T=1000.0 K):

W = 5.670367e+04 W⋅m^−2
Error Estimate: 6.3883e-09

Stefan-Boltzmann Constant Calculated: 5.670367e-08 W⋅m^−2⋅K^−4
Stefan-Boltzmann Constant from Literature: 6e-08 W⋅m^−2⋅K^−4
"""