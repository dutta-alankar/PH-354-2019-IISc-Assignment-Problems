# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 05:35:36 2018

@author: Alankar
"""

import numpy as np

def wave_vec(E,V,m=1,hbar=1):
    k1 = np.sqrt(2*m*E)/hbar
    k2 = np.sqrt(2*m*(E-V))/hbar
    return(k1,k2)

def Ref(k1,k2):
    R = (k1-k2)/(k1+k2)
    return np.abs(R)**2

def Trans(k1,k2):
    T = (2*k1)/(k1+k2)
    return (k2/k1)*np.abs(T)**2

m = 9.11e-31    
#units of Mass, Energy and hbar doesn't change Reflection and Transmission Probabilities as long as they are consistently used
E, V = 10, 9
k1, k2 = wave_vec(E,V)
print('Particle energy: %.1f eV\nBarrier height: %.1f eV'%(E,V))
print('Transmission Probability: %.2f\nReflection Probability: %.2f'%(Trans(k1,k2),Ref(k1,k2)))
    