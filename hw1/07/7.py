# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 11:07:55 2018

@author: Alankar
"""
import numpy as np

C = [1]
n = 0
while(C[n]<1e9):
    C.append(((4*n+2)/(n+2))*C[n])
    n += 1
print('Catalan numbers:\n',np.array(C,dtype=np.int64))