#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 15:43:56 2019

@author: alankar
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def fmt(x, pos):
    a, b = '{:.1e}'.format(x).split('e')
    b = int(b)
    return r'${} \times 10^{{{}}}$'.format(a, b)

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

f = lambda theta,m,x: np.cos(m*theta-x*np.sin(theta))
N = 1000
J = lambda m,x:simpson(f,0,np.pi,N,m,x)/np.pi

plt.figure(figsize=(13,10))
x= np.linspace(0,20,100)
M = np.arange(0,3,1)
for m in M: plt.plot(x,J(m,x),label=r'$J_{%d}(x)$'%m)
    
plt.grid()
plt.legend(loc='best',prop={'size': 18})
plt.xlabel(r'$x$',size=22)
plt.ylabel(r'$J_m(x)$',size=22)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.savefig('bessel.png')
plt.show()

resolution = 1024
x = np.linspace(-2,2,resolution)*1e3 #in nm
y = np.linspace(-2,2,resolution)*1e3 #in nm
XX, YY = np.meshgrid(x,y)
wav = 500
k = 2*np.pi/wav

r = np.sqrt(XX**2+YY**2)
I = (J(1,k*r)/(k*r))**2

plt.figure(figsize=(13,10))
plt.pcolormesh(x/1000,y/1000,I,vmax=0.005)
cbar = plt.colorbar(format=ticker.FuncFormatter(fmt))
cbar.ax.tick_params(labelsize=15) 
plt.title(r'$I(r) = \left(\frac{J_1(kr)}{kr}\right)^2$',size=25,y=1.03)
plt.xlabel(r'$\mu m$',size=22)
plt.ylabel(r'$\mu m$',size=22)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.savefig('I.png')
plt.show()

plt.figure(figsize=(13,10))
plt.pcolormesh(x/1000,y/1000,np.log10(I))
cbar = plt.colorbar()
cbar.ax.tick_params(labelsize=15) 
plt.title(r'$I(r) = \left(\frac{J_1(kr)}{kr}\right)^2$ (log scale)',size=25,y=1.03)
plt.xlabel(r'$\mu m$',size=22)
plt.ylabel(r'$\mu m$',size=22)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.savefig('logI.png')
plt.show()