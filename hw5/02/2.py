#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 12:42:27 2019

@author: alankar
"""
import numpy as np
import matplotlib.pyplot as plt

dt = 1 #s

tauBi, tauTl, tauPb = 46, 2.2, 3.3 #min

def Pb_decay(N_Pb,N_Bi_209,N_Bi_213,N_Tl):
    decay = np.random.uniform(low=0.,high=1.,size=N_Pb)
    prob = 1- 2**(-dt/(tauPb*60))
    decay = int(np.sum(np.array(decay<=prob,dtype=np.int16)))
    N_Pb -= decay
    N_Bi_209 += decay
    return (N_Pb,N_Bi_209,N_Bi_213,N_Tl)

def Tl_decay(N_Pb,N_Bi_209,N_Bi_213,N_Tl):
    decay = np.random.uniform(low=0.,high=1.,size=N_Tl)
    prob = 1- 2**(-dt/(tauTl*60))
    decay = int(np.sum(np.array(decay<=prob,dtype=np.int16)))
    N_Tl -= decay
    N_Pb += decay
    return (N_Pb,N_Bi_209,N_Bi_213,N_Tl)

def Bi_decay(N_Pb,N_Bi_209,N_Bi_213,N_Tl):
    route = np.random.uniform(low=0.,high=100.,size=N_Bi_213)
    N_Bi_Pb = int(np.sum(route<97.91))
    N_Bi_Tl = int(np.sum(route>=97.91)) #route.shape[0]-N_Bi_Pb 
    #Bi---->Pb decay
    decay = np.random.uniform(low=0.,high=1.,size=N_Bi_Pb)
    prob = 1- 2**(-dt/(tauBi*60))
    decay = int(np.sum(np.array(decay<=prob,dtype=np.int16)))
    N_Bi_213 -= decay
    N_Pb += decay
    #Bi---->Tl decay
    decay = np.random.uniform(low=0.,high=1.,size=N_Bi_Tl)
    prob = 1- 2**(-dt/(tauBi*60))
    decay = int(np.sum(np.array(decay<=prob,dtype=np.int16)))
    N_Bi_213 -= decay
    N_Tl += decay
    return (N_Pb,N_Bi_209,N_Bi_213,N_Tl)            

t = 20000
steps = t//dt    
N_Pb,N_Bi_209,N_Bi_213,N_Tl=np.zeros(steps+1,dtype=np.int16),np.zeros(steps+1,dtype=np.int16),np.zeros(steps+1,dtype=np.int16),np.zeros(steps+1,dtype=np.int16) 
N_Pb[0],N_Bi_209[0],N_Bi_213[0],N_Tl[0] = 0, 0, 10000, 0

for i in range(1,steps+1):
    N_Pb[i],N_Bi_209[i],N_Bi_213[i],N_Tl[i] = Pb_decay(N_Pb[i-1],N_Bi_209[i-1],N_Bi_213[i-1],N_Tl[i-1])
    N_Pb[i],N_Bi_209[i],N_Bi_213[i],N_Tl[i] = Tl_decay(N_Pb[i],N_Bi_209[i],N_Bi_213[i],N_Tl[i])
    N_Pb[i],N_Bi_209[i],N_Bi_213[i],N_Tl[i] = Bi_decay(N_Pb[i],N_Bi_209[i],N_Bi_213[i],N_Tl[i])

time = np.arange(0,steps+1,1)
plt.figure(figsize=(13,10))
plt.plot(time,N_Bi_209,label=r'Bi [209]')
plt.plot(time,N_Bi_213,label=r'Bi [213]')
plt.grid()
plt.ylabel(r'Atom Count',size=18)
plt.xlabel(r'Time (s)',size=20)
plt.title(r'Population of Starting element and Final decay product', size=21)
plt.tick_params(axis='both', which='major', labelsize=18)
plt.tick_params(axis='both', which='minor', labelsize=15)
plt.legend(loc='best',prop={'size': 18})
plt.savefig('2_1.png')
plt.show()
    
plt.figure(figsize=(13,10))
plt.plot(time,N_Pb,label=r'Pb')
plt.plot(time,N_Tl,label=r'Tl')
plt.grid()
plt.ylabel(r'Atom Count',size=18)
plt.xlabel(r'Time (s)',size=20)
plt.title(r'Population of Intermediate decay elements', size=21)
plt.tick_params(axis='both', which='major', labelsize=18)
plt.tick_params(axis='both', which='minor', labelsize=15)
plt.legend(loc='best',prop={'size': 18})
plt.savefig('2_2.png')
plt.show()