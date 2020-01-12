# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 18:02:07 2018

@author: Alankar
"""

import numpy as np

cpdef isMendel(c,int iterations):
    z = 0
    cpdef int i
    for i in range(0,iterations):
        z = z*z + c
    if np.abs(z)<=2: return True
    else: return False
    
cpdef int isMendel_iter(c,int maxiter):
    z = 0
    cpdef int i
    for i in range(0,maxiter):
        z = z*z + c
        if np.abs(z)>2: return i
    return maxiter
    