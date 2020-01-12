#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 16:42:53 2019

@author: alankar
"""

import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

data = np.loadtxt('sunspots.txt')
t = data[:,0]
spots = data[:,1]

plt.figure(figsize=(13,10))
#plt.bar(k[:N//2],square_fft[:N//2]/N, width=1.5)
plt.plot(t,spots)
plt.grid()
plt.xlabel(r'Months',size=18)
plt.ylabel(r'No. of Sunspots',size=20)
plt.title(r'Sunspots by month since January 1749', size=21)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.savefig('2_1.png')
plt.show()

spots_fft = np.abs(np.fft.fft(spots))**2

N = len(spots)
sampling = t[1] - t[0]
Period = (1/np.linspace(0,1/sampling,N))/12 #yr

plt.figure(figsize=(13,10))
plt.plot(Period[1:N//2],spots_fft[1:N//2])
plt.grid()
plt.xlabel(r'Period (yr)',size=18)
plt.ylabel(r'FT[Spot Count]',size=20)
plt.title(r'Sunspot periodicity', size=21)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.xlim(0,20)
plt.savefig('2_2.png')
plt.show()
print('Dominant period: %.1f years'%Period[np.argmax(spots_fft[1:N//2])])

"""
Output:
    
Dominant period: 11.4 years

"""