#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 19:15:08 2019

@author: alankar
"""
import numpy as np
from scipy.special.orthogonal import p_roots #Legendre Polynomial roots
import matplotlib.pyplot as plt

def gauss_quad(func,a,b,n,*args):#Legendre
    [x,w] = p_roots(n+1)
    I_G = 0.5*(b-a)*np.sum(w*func(0.5*(b-a)*x+0.5*(b+a),*args))
    return I_G

V = lambda x:x**4
eps = 1e-15
m = 1
N = 20

f = lambda x,a:4/np.sqrt((2/m)*(V(a)-V(x)+eps))

amplitude = np.linspace(0.1,2,100)

period = np.abs(np.array([gauss_quad(f,a,0,N,a) for a in amplitude]))

plt.figure(figsize=(13,10))
plt.plot(amplitude[1:],period[1:])
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.grid()
plt.title(r'Anharmonic Oscillator Time period',size=25,y=1.02)
plt.xlabel(r'Amplitude',size=22)
plt.ylabel(r'Time period',size=22)
plt.savefig('10.png')
plt.show()