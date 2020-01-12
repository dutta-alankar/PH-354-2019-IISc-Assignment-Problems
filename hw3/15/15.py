#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 15:16:13 2019

@author: alankar
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special.orthogonal import p_roots #Legendre Polynomial roots


def gauss_quad(func,a,b,n,*args):#Legendre
    [x,w] = p_roots(n+1)
    I_G = 0.5*(b-a)*np.sum(w*func(0.5*(b-a)*x+0.5*(b+a),*args))
    return I_G

a = [2,3,4]
x = np.linspace(0,5,100)

plt.figure(figsize=(13,10))
for A in a:
    plt.plot(x,x**(A-1)*np.exp(-x), label='a=%d'%A)

plt.legend(loc='best',prop={'size': 18})
plt.grid()
plt.title(r'$x^{a-1} \exp (-x)$',size=25,y=1.02)
plt.xlabel(r'$x$',size=22)
plt.ylabel(r'$f(x)$',size=22)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.savefig('15.png')
plt.show()    

def I (z,a):
    c = a-1
    x = c/(1/z-1)
    factor = c/(1-z)**2
    return np.exp((a-1)*np.log(x)-x)*factor

N = 100
gamma = gauss_quad(I,0.,1.,N,1.5)
print('Gamma(3/2) = %.3f'%gamma)

gamma = np.array([gauss_quad(I,0.,1.,N,a) for a in np.arange(2,11,1)])
for i,g in enumerate(gamma):
    print('Gamma(%d) = %d'%(i+2,g))
    
"""
Output:
    
Gamma(3/2) = 0.886
Gamma(2) = 1
Gamma(3) = 2
Gamma(4) = 6
Gamma(5) = 24
Gamma(6) = 120
Gamma(7) = 720
Gamma(8) = 5040
Gamma(9) = 40320
Gamma(10) = 362880

"""