#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 10:50:55 2019

@author: alankar
"""

import numpy as np
import matplotlib.pyplot as plt

d = 20*1e3 #nm
alpha = np.pi/d 
slits = 10
wavl = 500 #nm
f = 1*1e9 #nm
N = 1000
w = slits*d
enlarge_factor = 10
W = enlarge_factor*w

q = lambda u: np.sin(alpha*u)**2

u = np.linspace(-w/2,w/2,N)
q = q(u)
q = np.hstack((np.zeros(int(N*((enlarge_factor-1)/2))),q,np.zeros(int(N*((enlarge_factor-1)/2)))))

N *= enlarge_factor
width = np.linspace(-W/2,W/2,N)

y = np.abs(np.sqrt(q))
xlim = (N-1)*wavl*f/W
x = np.linspace(0,xlim,N)
I = (W/N)**2*np.abs(np.fft.fft(y))**2
L = 5*1e7 #nm
till = int(L/(wavl*f/W))
x = np.hstack((np.flip(-x[:till]),x[:till]))
I = np.hstack((np.flip(I[:till]),I[:till]))
plt.figure(figsize=(13,10))
plt.plot(x*1e-7,I*1e-10)
plt.grid()
plt.ylabel(r'$I (\times 10^{10} Wm^{-2})$',size=20)
plt.xlabel(r'$x (cm)$',size=20)
plt.title(r'Diffraction Pattern', size=21)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.savefig('7_1.png')
plt.show()

y = np.linspace(-0.8,0.8,10) #cm
XX,YY = np.meshgrid(x,y)
line = np.zeros((len(y),len(x)))

for i in range(len(x)):
    for j in range(len(y)):
        line[j,i] = I[i]

plt.figure(figsize=(13,1))
plt.pcolor(x*1e-7,y,line*1e-10,cmap='gray',vmax=0.1)
#plt.colorbar()
plt.xticks([])
plt.yticks([])
plt.savefig('7_2.png')
plt.show()