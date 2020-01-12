#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 10:53:23 2019

@author: alankar
"""

import numpy as np
import matplotlib.pyplot as plt

def DFT_slow(x):
    """Compute the discrete Fourier Transform of the 1D array x"""
    x = np.asarray(x, dtype=float)
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    M = np.exp(-2j * np.pi * k * n / N)
    return np.dot(M, x)

def FFT(x):
    #A recursive implementation of the 1D Cooley-Tukey FFT
    x = np.asarray(x, dtype=float)
    N = x.shape[0]
    
    if N % 2 > 0:
        raise ValueError("size of x must be a power of 2")
    elif N <= 32:  # this cutoff should be optimized
        return DFT_slow(x)
    else:
        X_even = FFT(x[::2])
        X_odd = FFT(x[1::2])
        factor = np.exp(-2j * np.pi * np.arange(N//2) / N)
        return np.concatenate([X_even + factor * X_odd,
                               X_even - factor * X_odd])
    
pitch = np.loadtxt('pitch.txt')
pitch_fft_custom = np.abs(FFT(pitch))**2
#pitch_fft_np = np.fft.fft(pitch)**2

plt.figure(figsize=(13,10))
plt.plot(np.arange(0,len(pitch)//2,1),pitch_fft_custom[:len(pitch)//2])
plt.grid()
plt.xlabel(r'$f (Hz)$',size=18)
plt.ylabel(r'$A(f)$',size=20)
plt.title(r'Piano Music', size=21)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.ylim(0,10000)
plt.savefig('6.png')
plt.show()


"""
In FFT implementation, at the lowest recursion level we perform N/N_min identical matrix-vector products
"""

"""
def FFT(x):
    #A vectorized, non-recursive version of the Cooley-Tukey FFT
    x = np.asarray(x, dtype=float)
    N = len(x)
    N_min = 32

    if np.log2(N) % 1 > 0:
        raise ValueError("size of x must be a power of 2")

    # N_min here is equivalent to the stopping condition above,
    # and should be a power of 2 and needs to be optimized
    N_min = min(N, N_min)
    
    # Perform an O[N^2] DFT on all length-N_min sub-problems at once (each of size N/N_min)
    n = np.arange(0,N_min,1)
    k = n[:, None]
    M = np.exp(-2j * np.pi * n * k / N_min)
    X = np.dot(M, x.reshape((N_min, -1)))

    # build-up each level of the recursive calculation all at once
    while X.shape[0] < N:
        X_even = X[:, :X.shape[1] / 2]
        X_odd = X[:, X.shape[1] / 2:]
        factor = np.exp(-1j * np.pi * np.arange(X.shape[0])
                        / X.shape[0])[:, None]
        X = np.vstack([X_even + factor * X_odd,
                       X_even - factor * X_odd])

    return np.reshape(X,-1)
"""
