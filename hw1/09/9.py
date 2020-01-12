# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 19:51:06 2018

@author: Alankar
"""
import numpy as np
import matplotlib.pyplot as plt

def BE(A,Z):
    a1, a2, a3, a4 = 15.67, 17.23, 0.75, 93.2
    a5 = 0
    if not(A%2==0):
        a5 = 0
    elif(A%2==0 and Z%2==0):
        a5 = 12
    elif(A%2==0 and not(Z%2==0)):
        a5 = -12
    return a1*A - a2*A**(2/3) - a3*(Z**2/A**(1/3)) - a4*((A-2*Z)**2/A) + a5/A**(1/2)

print('-----------------------------------------------------------')
print('Demo Output: \nBinding Energy of a nucleus with Z = %d and A = %d is %.2f MeV'%(28,58,BE(58,28)))  
print('Binding Energy per nucleon: %.2f MeV'%(BE(58,28)/58))
print('-----------------------------------------------------------')    
    
Z = float(input('Enter Atomic number of nucleus: '))
A = float(input('Enter Mass number of nucleus: '))
B = BE(A,Z)
print('\nBinding Energy is %.2f MeV'%B)
print('Binding Energy per nucleon: %.2f MeV'%(BE(A,Z)/A))

def stableA(Z):
    B = BE(Z,Z)/Z
    A_st = Z
    for A in range(Z+1,3*Z+1):
        B_tmp = BE(A,Z)/A
        if (B_tmp>B): 
            B = B_tmp
            A_st = A
    return (A_st,B)

NuProf = np.zeros((100,2),dtype=np.float32)    
for Z in range(0,100):    
    st = stableA(Z+1)
    NuProf[Z,0] = st[0]
    NuProf[Z,1] = st[1]
    print('Most stable nucleus with Z = %d has A = %d'%((Z+1),NuProf[Z,0]))

print('\n\nMax Binding Energy per nucleon is at Z = ',(np.argmax(NuProf[:,1])+1))

plt.plot(np.arange(1,101,1),NuProf[:,1])
plt.xlabel('Atomic Number Z')
plt.ylabel('Binding Energy per nucleon (MeV)')
plt.savefig('Binding Energy Curve.png')
plt.show()