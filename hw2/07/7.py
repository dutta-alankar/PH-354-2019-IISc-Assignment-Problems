#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 22:23:04 2019

@author: alankar
"""
import numpy as np
import scipy.constants as const
import warnings
warnings.filterwarnings('ignore')

L = 1.    #nm
V0 = 20.  #eV
u02 = (const.m_e*(L*1e-9)**2/(2*const.hbar**2))*(V0*const.e)

def sym(v):
    return  -v*np.sin(v) + np.sqrt(u02-v**2)* np.cos(v)
      

def asym(v):
    return v*np.cos(v) + np.sqrt(u02-v**2)* np.sin(v)

def false_pos(func,a,b,tol,*args):
    c = (a+b)/2.
    counter = 0
    while(np.abs(func(c,*args))>=tol):
        counter += 1
        c = (a*func(b,*args)-b*func(a,*args))
        c = c/(func(b,*args)-func(a,*args))
        #print("%-20.8g %-20.8g %-20.8g %-20.8g %-20.8g\n" % (counter, a, b, c, func(c,*args)))
        if (func(a,*args)*func(c,*args)>=0): a=c
        else: b=c
    return c


print('The energy eigenstates are as follows: ')

for n in range(4):
    a = (1+3*n)-0.3*3
    b = (1+3*n)+0.3*3
    E = ((1/(2*const.m_e))*(2*const.hbar*false_pos(sym,a,b,1e-6)/(L*1e-9))**2)/const.e
    if (E<V0): print("%.6g eV [Symmetric]"%E)
    a = (2.7+3*n)-0.3*3
    b = (2.7+3*n)+0.3*3
    E = ((1/(2*const.m_e))*(2*const.hbar*false_pos(asym,a,b,1e-6)/(L*1e-9))**2)/const.e
    if (E<V0): print("%.6g eV [Anti-Symmetric]"%E)

"""
Output:
The energy eigenstates are as follows: 
0.317939 eV [Symmetric]
1.27008 eV [Anti-Symmetric]
2.85103 eV [Symmetric]
5.05042 eV [Anti-Symmetric]
7.84985 eV [Symmetric]
11.2151 eV [Anti-Symmetric]
15.0706 eV [Symmetric]
"""