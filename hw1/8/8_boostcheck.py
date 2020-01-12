# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 17:24:16 2018

@author: Alankar
"""

import numpy as np
from time import time

L = 100
M = 0
t1 = time()
for i in range(-L,L+1):
    for j in range(-L,L+1):
        for k in range(-L,L+1):
            if (i==0 and j==0 and k==0): continue
            n = i+j+k
            M += (-1)**n/np.sqrt(i**2+j**2+k**2)
t2 = time()
print(M)
print('Took ', (t2-t1))

import madelung as md
L = 100
t1 = time()
M = md.Madelung_compute(L)
t2 = time()
print(M)
print('Took ', (t2-t1))
