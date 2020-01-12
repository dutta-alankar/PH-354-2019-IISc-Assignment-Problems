#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 17:56:45 2019

@author: alankar
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

piano = np.loadtxt('piano.txt')
trumpet = np.loadtxt('trumpet.txt')

N = len(piano)
freq = 44100
time = 1/freq
t = np.arange(0,N*time,time)

plt.figure(figsize=(13,10))
plt.plot(t,piano)
plt.grid()
plt.xlabel(r'$t$',size=18)
plt.ylabel(r'$A(t)$',size=20)
plt.title(r'Piano Music', size=21)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.savefig('Piano_music.png')
plt.show()


plt.figure(figsize=(13,10))
plt.plot(t,trumpet)
plt.grid()
plt.xlabel(r'$t$',size=18)
plt.ylabel(r'$A(t)$',size=20)
plt.title(r'Trumpet Music', size=21)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.savefig('Trumpet_music.png')
plt.show()

piano_fft = np.abs(np.fft.fft(piano))**2
trumpet_fft = np.abs(np.fft.fft(trumpet))**2

f = np.linspace(0,freq,N)

plt.figure(figsize=(13,10))
plt.plot(f[:N//2],piano_fft[:N//2])
plt.grid()
plt.xlabel(r'f (Hz)',size=18)
plt.ylabel(r'A(f)',size=20)
plt.title(r'FFT[Piano Music]', size=21)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.savefig('Piano_FFT.png')
plt.show()
peak_pos = signal.find_peaks(piano_fft[:N//2],distance=200//(f[1]-f[0]),threshold=1e13)[0]
#print('Dominant frequency is: %d Hz, %d Hz and %d Hz'%(f[sort_pos[-1]],f[sort_pos[-2]],f[sort_pos[-3]]) )
print('Piano frequencies observed at (Hz): ')
print(np.array([f[i] for i in peak_pos]))

plt.figure(figsize=(13,10))
plt.plot(f[:N//2],trumpet_fft[:N//2])
plt.grid()
plt.xlabel(r'f (Hz)',size=18)
plt.ylabel(r'A(f)',size=20)
plt.title(r'FFT[Trumpet Music]', size=21)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.savefig('Trumpet_FFT.png')
plt.show()
peak_pos = signal.find_peaks(trumpet_fft[:N//2],distance=200//(f[1]-f[0]),threshold=1e13)[0]
print('Trumpet frequencies observed at (Hz): ')
print(np.array([f[i] for i in peak_pos]))

"""
Output:
    
Piano frequencies observed at (Hz): 
[ 524.79524795 1051.35451355 1578.35478355]


Trumpet frequencies observed at (Hz): 
[ 521.70821708 1043.85743857 1566.00666007 2087.71487715 2609.86409864
 3132.01332013 3653.72153722 4175.87075871]

"""