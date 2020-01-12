#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 10:28:55 2019

@author: alankar
"""

import numpy as np
import matplotlib.pyplot as plt
import RK4

Vout0 = 0

def Vin(t):
    if (t==0): return Vout0
    if (int(np.floor(2*t)%2)==0): return 1
    return -1 

def f(t,Vout,RC):
    V = None
    if not(isinstance(t,np.ndarray) or isinstance(t,list)): 
        V = Vin(t)
    else:
        V = np.array([Vin(time) for time in t])
    return (V - Vout)/RC

t = np.linspace(0,10,100000)

plt.figure(figsize=(13,10))
plt.plot(t,np.array([Vin(time) for time in t]))
plt.grid()
plt.ylabel(r'Input Voltage',size=18)
plt.xlabel(r'time',size=20)
plt.title(r'Low Pass Filter (Input Voltage)', size=21)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.savefig('input.png')
plt.show()

RC = 0.01
Vout = RK4.RK4(f,Vout0,t,RC)

plt.figure(figsize=(13,10))
plt.plot(t,Vout)
plt.grid()
plt.ylabel(r'Output Voltage',size=18)
plt.xlabel(r'time',size=20)
plt.title(r'Low Pass Filter ($RC=%.2f$)'%RC, size=21)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.savefig('1_1.png')
plt.show()

RC = 0.1
Vout = RK4.RK4(f,Vout0,t,RC)

plt.figure(figsize=(13,10))
plt.plot(t,Vout)
plt.grid()
plt.ylabel(r'Output Voltage',size=18)
plt.xlabel(r'time',size=20)
plt.title(r'Low Pass Filter ($RC=%.2f$)'%RC, size=21)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.savefig('1_2.png')
plt.show()

RC = 1.
Vout = RK4.RK4(f,Vout0,t,RC)

plt.figure(figsize=(13,10))
plt.plot(t,Vout)
plt.grid()
plt.ylabel(r'Output Voltage',size=18)
plt.xlabel(r'time',size=20)
plt.title(r'Low Pass Filter ($RC=%.2f$)'%RC, size=21)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.savefig('1_3.png')
plt.show()