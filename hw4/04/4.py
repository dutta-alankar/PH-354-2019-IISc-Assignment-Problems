#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 19:53:09 2019

@author: alankar
"""

import numpy as np
import matplotlib.pyplot as plt

dow = np.loadtxt('dow.txt')
N = len(dow)
t = np.arange(0,N,1)

sampling = 1/(t[1]-t[0])
f = np.linspace(0,sampling,N//2+1)
dow_fft = np.fft.rfft(dow)
plt.figure(figsize=(13,10))
plt.semilogy(f,np.abs(dow_fft)**2)
plt.grid()
plt.xlabel(r'f',size=18)
plt.ylabel(r'Power Spectrum $P(f)$',size=20)
plt.title(r'FFT[DOW]', size=21)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.savefig('4_1.png')
plt.show()


plt.figure(figsize=(13,10))
plt.plot(t,dow,label='Original Data')
plt.grid()
plt.xlabel(r'Days',size=18)
plt.ylabel(r'DOW',size=20)
plt.title(r'DOW Industrial Average', size=21)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.savefig('4_2.png')

compress = lambda data,freq,percent_acc: np.piecewise(data,[(freq-freq[0])<=\
                                                       (percent_acc/100)*(freq[-1]-freq[0])],[lambda data: data,0.])

dow_fft1 = compress(dow_fft,f,10)
dow_fft2 = compress(dow_fft,f,2)
dow1 = np.fft.irfft(dow_fft1)
dow2 = np.fft.irfft(dow_fft2)
plt.plot(t,dow1,label=r'%d percent Fourier modes Accepted'%90)
plt.plot(t,dow2,label=r'%d percent Fourier modes Accepted'%2)
plt.legend(loc='best', prop={'size': 16})
plt.savefig('4_3.png')
plt.show()
