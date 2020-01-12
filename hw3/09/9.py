#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 17:53:39 2019

@author: alankar
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special.orthogonal import p_roots #Legendre Polynomial roots
from scipy import constants

def gauss_quad(func,a,b,n,*args):#Legendre
    [x,w] = p_roots(n+1)
    I_G = 0.5*(b-a)*np.sum(w*func(0.5*(b-a)*x+0.5*(b+a),*args))
    return I_G

V = 1000*1e-6 #m^3
rho = 6.022e28 #m^-3
thetaD = 428  #K

def CV(T):
    N = 50
    f = lambda x:(x**4*np.exp(x))/(np.exp(x)-1)**2
    return 9*V*rho*constants.k*(T/thetaD)**3*gauss_quad(f,0,thetaD/T,N)
      
Temperature = np.linspace(5,500,1000)    
Heat_cap = np.array([CV(T) for T in Temperature])
plt.figure(figsize=(13,10))
plt.plot(Temperature,Heat_cap)
plt.grid()
plt.title(r'Debye Heat capacity $C_V(T)$ in a solid',size=25,y=1.02)
plt.xlabel(r'$T$',size=22)
plt.ylabel(r'$C_V(T)$',size=22)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.savefig('9.png')
plt.show()