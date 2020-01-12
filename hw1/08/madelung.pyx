# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 16:10:17 2018

@author: Alankar
"""

from numpy import sqrt

cpdef double Madelung_compute(int L):
    cpdef int i
    cpdef int j
    cpdef int k
    cpdef double M = 0.
    for i in range(-L,L+1):
        for j in range(-L,L+1):
            for k in range(-L,L+1):
                if (i==0 and j==0 and k==0): continue
                n = i+j+k
                M += (-1)**n/sqrt(i**2+j**2+k**2)
    return M