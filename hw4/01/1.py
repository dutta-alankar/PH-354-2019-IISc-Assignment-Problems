#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 15:33:13 2019

@author: alankar
"""

import numpy as np
import matplotlib.pyplot as plt

N = 1000

square = lambda n: np.piecewise(n, [n>=N/2], [1.,0.])

n = np.arange(0,N,1)

square = square(n)
sawtooth = n
modulated = np.sin(1*np.pi*n/N)*np.sin(20*np.pi*n/N)

plt.figure(figsize=(13,10))
plt.plot(n,square)
plt.grid()
plt.xlabel(r'$x$',size=18)
plt.ylabel(r'$f(x)$',size=20)
plt.title(r'Square Wave', size=21)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.savefig('1_1.png')
plt.show()

plt.figure(figsize=(13,10))
plt.plot(n,sawtooth)
plt.grid()
plt.xlabel(r'$x$',size=18)
plt.ylabel(r'$f(x)$',size=20)
plt.title(r'Sawtooth Wave', size=21)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.savefig('1_2.png')
plt.show()

plt.figure(figsize=(13,10))
plt.plot(n,modulated)
plt.grid()
plt.xlabel(r'$x$',size=18)
plt.ylabel(r'$f(x)$',size=20)
plt.title(r'Modulated Sine Wave', size=21)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.savefig('1_3.png')
plt.show()


square_fft = np.abs(np.fft.fft(square))**2
sawtooth_fft = np.abs(np.fft.fft(sawtooth))**2
modulated_fft = np.abs(np.fft.fft(modulated))**2

sampling = n[1] - n[0]
f = np.linspace(0,1/sampling,N)

plt.figure(figsize=(13,10))
plt.plot(f[1:N//2],square_fft[1:N//2])
plt.grid()
plt.xlabel(r'$k$',size=18)
plt.ylabel(r'$\~f(k)$',size=20)
plt.title(r'FT[Square Wave]', size=21)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.ylim(0,400)
plt.savefig('1_4.png')
plt.show()

plt.figure(figsize=(13,10))
plt.plot(f[1:N//2],sawtooth_fft[1:N//2])
plt.grid()
plt.xlabel(r'$k$',size=18)
plt.ylabel(r'$\~f(k)$',size=20)
plt.title(r'FT[Sawtooth Wave]', size=21)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.savefig('1_5.png')
plt.ylim(0,1e7)
plt.show()

plt.figure(figsize=(13,10))
plt.plot(f[1:N//2],modulated_fft[1:N//2])
plt.grid()
plt.xlabel(r'$k$',size=18)
plt.ylabel(r'$\~f(k)$',size=20)
plt.title(r'FT[Modulated Sine Wave]', size=21)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.savefig('1_6.png')
#plt.ylim(0,100)
plt.show()
