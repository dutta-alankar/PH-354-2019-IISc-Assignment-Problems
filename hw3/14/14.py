#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 11:14:22 2019

@author: alankar
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special.orthogonal import p_roots #Legendre Polynomial roots
#from scipy import constants

"""
def gauss_quad(func,a,b,n,*args):#Legendre
    [x,w] = p_roots(n+1)
    I_G = 0.5*(b-a)*np.sum(w*func(0.5*(b-a)*x+0.5*(b+a),*args))
    return I_G

def gauss_quad_2d(func,a,b,n,*args):#Legendre 
    I_G = gauss_quad(lambda y:gauss_quad(func,a[0],b[0],n[0],y,*args),a[1],b[1],n[1])
    return I_G
"""

def gauss_quad_2d(func,a,b,n,*args):#Legendre 
    [x,wx] = p_roots(n[0]+1)
    [y,wy] = p_roots(n[1]+1)
    x,y = np.meshgrid(x,y)
    wx,wy = np.meshgrid(wx,wy)
    I_G = 0.5*(b[0]-a[0])*0.5*(b[1]-a[1])*np.sum(wx*wy*\
              func(0.5*(b[0]-a[0])*x+0.5*(b[0]+a[0]),0.5*(b[1]-a[1])*y+0.5*(b[1]+a[1]),*args))
    return I_G

I = lambda x,y,z: np.nan_to_num(z/(x**2+y**2+z**2)**1.5) #To remove singularity at (0,0,0)

L = 10
N = 100


z = np.linspace(0.,10,30) 
#G sigma = 1

Fz = np.array([gauss_quad_2d(I,[-L/2.,-L/2.],[L/2.,L/2.],[N,N],Z) for Z in z])

plt.figure(figsize=(13,10))
plt.plot(z,Fz,c='r')
plt.xlabel(r'$z$',size=22)
plt.ylabel(r'$F_z$',size=22)
plt.title('Gravitational pull',size=25)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.grid()
plt.savefig('14_1.png')
plt.show()

N = 800
z = np.linspace(0.,10,400) 
Fz = np.array([gauss_quad_2d(I,[-L/2.,-L/2.],[L/2.,L/2.],[N,N],Z) for Z in z])

plt.figure(figsize=(13,10))
plt.plot(z,Fz,c='r')
plt.xlabel(r'$z$',size=22)
plt.ylabel(r'$F_z$',size=22)
plt.title('Gravitational pull',size=25)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.grid()
plt.savefig('14_2.png')
plt.show()

