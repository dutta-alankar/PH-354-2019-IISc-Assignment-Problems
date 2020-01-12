#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 21:10:04 2019

@author: alankar
"""

import numpy as np
from scipy.special.orthogonal import p_roots #Legendre Polynomial roots
import matplotlib.pyplot as plt

def gauss_quad(func,a,b,n,*args):#Legendre
    [x,w] = p_roots(n+1)
    I_G = 0.5*(b-a)*np.sum(w*func(0.5*(b-a)*x+0.5*(b+a),*args))
    return I_G

N = 50
ci = lambda t:np.cos(0.5*np.pi*t**2)
si = lambda t:np.sin(0.5*np.pi*t**2)

C = lambda u:gauss_quad(ci,0,u,N)
S = lambda u:gauss_quad(si,0,u,N)

IbyI0 = lambda u:(1/8)*((2*C(u)+1)**2+(2*S(u)+1)**2)

x = np.linspace(-5.,5.,300)
z = 3.
wavl = 1.

ratio = np.array([IbyI0(u) for u in (x*np.sqrt(2/(wavl*z)))])

plt.figure(figsize=(13,10))
plt.plot(x,ratio)
plt.title(r'Plane wave diffraction by a straight barrirer at $x \leq 0$',size=25,y=1.03)
plt.xlabel(r'$x$',size=22)
plt.ylabel(r'$\frac{I}{I_0}$ at fixed distance from barrier $(z=3)$',size=22)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.grid()
plt.savefig('11.png')
plt.show()