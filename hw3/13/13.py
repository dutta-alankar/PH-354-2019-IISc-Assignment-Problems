#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 17:02:36 2019

@author: alankar
"""

import numpy as np
from scipy.special.orthogonal import p_roots #Legendre Polynomial roots
import matplotlib.pyplot as plt
#import time


def Hermite_pol(n,x,Outside=True):   #memo is refreshed whenever called from outside, Always keep outside True
    if (Outside):
        global memo #remembers the child recursion loops for speedup
        memo = {}
        try:#So that it may also work with scalar value of x
           memo = {0:np.ones(len(x)),1:2*x} 
        except:
           memo = {0:1.,1:2*x}  
    if n not in memo:
        N = n-1
        memo[n] = 2*x*Hermite_pol(N,x,False)-2*N*Hermite_pol(N-1,x,False) 
    return memo[n]
    
x = np.linspace(-4,4,100)
plt.figure(figsize=(13,10))
for n in range(4):
    y = Hermite_pol(n,x)
    plt.plot(x,y,label=r'$H_{%d}(x)$'%n)

plt.legend(loc='best',prop={'size': 18})
plt.ylim(-15.0,20.0)
plt.grid()
plt.xlabel(r'$x$',size=22)
plt.ylabel(r'$H_n(x)$',size=22)
plt.title('Hermite Polynomials',size=25,y=1.02)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.savefig('13_1.png')
plt.show()

plt.figure(figsize=(13,10))
for n in range(4):
    psi = Hermite_pol(n,x)
    psi *= np.exp(-x**2/2)/np.sqrt((2**n)*np.math.factorial(n)*np.pi**0.5)
    plt.plot(x,psi,label=r'$\psi_{%d}(x)$'%n)

plt.legend(loc='best',prop={'size': 18})
plt.grid()
plt.xlabel(r'$x$',size=22)
plt.ylabel(r'$\psi_n(x)$',size=22)
plt.title('Harmonic Oscillator Wavefunctions',size=25,y=1.02)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.savefig('13_2.png')
plt.show()

#t = time.time()
x = np.linspace(-10,10,800)
n = 30
psi = Hermite_pol(n,x)
psi *= (1/np.sqrt(2**n*np.math.factorial(n)*np.sqrt(np.pi)))*np.exp(-x**2/2)
plt.figure(figsize=(13,10))
plt.plot(x,psi,label=r'$\psi_{%d}(x)$'%n)
plt.legend(loc='best',prop={'size': 18})
plt.grid()
plt.xlabel(r'$x$',size=22)
plt.ylabel(r'$\psi_n(x)$',size=22)
plt.title('Harmonic Oscillator Wavefunction',size=25,y=1.02)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.savefig('13_3.png')
plt.show()
#print("Took %.2f secs"%(time.time()-t))

def gauss_quad(func,a,b,n,*args):#Legendre
    [x,w] = p_roots(n+1)
    I_G = 0.5*(b-a)*np.sum(w*func(0.5*(b-a)*x+0.5*(b+a),*args))
    return I_G

N = 50
psi = lambda x,n:Hermite_pol(n,x)*(1/np.sqrt(2**n*np.math.factorial(n)*np.sqrt(np.pi)))*np.exp(-x**2/2)
integ = lambda theta,n:np.tan(theta)**2*np.abs(psi(np.tan(theta),n))**2/np.cos(theta)**2

n = 0
uncer = np.sqrt(gauss_quad(integ,-np.pi/2,np.pi/2,N,n))
print('Ground state uncertainty: %.4f'%uncer)

n = 5
uncer = np.sqrt(gauss_quad(integ,-np.pi/2,np.pi/2,N,n))
print('%dth Eigenstate uncertainty: %.4f'%(n,uncer))

"""
Output:
    
Ground state uncertainty: 0.7071
5th Eigenstate uncertainty: 2.3451
"""
