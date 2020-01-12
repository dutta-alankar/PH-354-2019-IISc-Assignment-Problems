#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 17:09:12 2019

@author: alankar
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special.orthogonal import p_roots #Legendre Polynomial roots

def gauss_quad(func,a,b,n,*args):#Legendre
    [x,w] = p_roots(n+1)
    I_G = 0.5*(b-a)*np.sum(w*func(0.5*(b-a)*x+0.5*(b+a),*args))
    return I_G


def I(x,d,slits,f,wavl,q):
    w = d*slits
    N = 100
    alpha = np.pi/d
    real = lambda u:np.sqrt(q(u,alpha))*np.cos(2*np.pi*x*u/(wavl*f))
    imag = lambda u:np.sqrt(q(u,alpha))*np.sin(2*np.pi*x*u/(wavl*f))
    #u = np.linspace(-w/2,w/2,1000)
    #plt.plot(u,real(u))
    #plt.plot(u,imag(u))
    #plt.grid()
    #plt.show()
    real_I = gauss_quad(real,-w/2,w/2,N) 
    imag_I = gauss_quad(imag,-w/2,w/2,N) 
    return real_I**2+imag_I**2


q = lambda u,alpha: np.sin(alpha*u)**2

d = 20*1e3 #nm
wavl = 500 #nm
f = 1*1e9 #nm
slits = 10
x = np.linspace(-5,5,1000)*1e7


Intensity = np.array([I(X,d,slits,f,wavl,q) for X in x])
plt.plot(x*1e-7,Intensity*1e-10)
plt.grid()
plt.xlabel(r'$x (cm)$')
plt.ylabel(r'$I (\times 10^{10} Wm^{-2})$')
plt.savefig('16_1_1.png')
plt.show()
y = np.linspace(-0.8,0.8,10)*1e7
XX,YY = np.meshgrid(x,y)
line = np.zeros((len(y),len(x)))

for i in range(len(x)):
    for j in range(len(y)):
        line[j,i] = Intensity[i]

plt.figure(figsize=(13,1))
plt.pcolor(x*1e-7,y*1e-7,line*1e-10,cmap='gray',vmax=0.2)
#plt.colorbar()
plt.xticks([])
plt.yticks([])
plt.savefig('16_1_2.png')
plt.show()



#--------------------------------------------------------------------------------




q = lambda u,alpha: np.sin(alpha*u)**2*np.sin(alpha*u/2)**2

d = 20*1e3 #nm
wavl = 500 #nm
f = 1*1e9 #nm
slits = 10
x = np.linspace(-5,5,1000)*1e7


Intensity = np.array([I(X,d,slits,f,wavl,q) for X in x])
plt.plot(x*1e-7,Intensity*1e-10)
plt.grid()
plt.xlabel(r'$x (cm)$')
plt.ylabel(r'$I (\times 10^{10} Wm^{-2})$')
plt.savefig('16_2_1.png')
plt.show()
y = np.linspace(-0.8,0.8,10)*1e7
XX,YY = np.meshgrid(x,y)
line = np.zeros((len(y),len(x)))

for i in range(len(x)):
    for j in range(len(y)):
        line[j,i] = Intensity[i]

plt.figure(figsize=(13,1))
plt.pcolor(x*1e-7,y*1e-7,line*1e-10,cmap='gray',vmax=0.1)
#plt.colorbar()
plt.xticks([])
plt.yticks([])
plt.savefig('16_2_2.png')
plt.show()



#--------------------------------------------------------------------------------

def I(x,f,wavl,q):
    w = 75*1e3 #nm
    N = 100
    real = lambda u:np.sqrt(q(u*1e-3))*np.cos(2*np.pi*x*u/(wavl*f)) #u converted to micro m
    imag = lambda u:np.sqrt(q(u*1e-3))*np.sin(2*np.pi*x*u/(wavl*f))
    #u = np.linspace(-w/2,w/2,1000)
    #plt.plot(u,real(u))
    #plt.plot(u,imag(u))
    #plt.grid()
    #plt.show()
    real_I = gauss_quad(real,-w/2,w/2,N) 
    imag_I = gauss_quad(imag,-w/2,w/2,N) 
    return real_I**2+imag_I**2


q = lambda u: np.piecewise(u, [np.logical_and(u>=-37.5, u<=-27.5), np.logical_and(u>=17.5, u<=37.5)], [1.,1.,0.])
    

wavl = 500 #nm
f = 1*1e9 #nm
x = np.linspace(-5,5,1000)*1e7


Intensity = np.array([I(X,f,wavl,q) for X in x])
plt.plot(x*1e-7,Intensity*1e-10)
plt.grid()
plt.xlabel(r'$x (cm)$')
plt.ylabel(r'$I (\times 10^{10} Wm^{-2})$')
plt.savefig('16_3_1.png')
plt.show()
y = np.linspace(-0.8,0.8,10)*1e7
XX,YY = np.meshgrid(x,y)
line = np.zeros((len(y),len(x)))

for i in range(len(x)):
    for j in range(len(y)):
        line[j,i] = Intensity[i]

plt.figure(figsize=(13,1))
plt.pcolor(x*1e-7,y*1e-7,line*1e-10,cmap='gray')
#plt.colorbar()
plt.xticks([])
plt.yticks([])
plt.savefig('16_3_2.png')
plt.show()