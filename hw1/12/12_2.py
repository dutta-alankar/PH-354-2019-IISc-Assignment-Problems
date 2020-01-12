# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 10:35:11 2018

@author: Alankar
"""

def catalan(n):
    if (n==0): return 1
    return ((4*n-2)/(n+1))*catalan(n-1)

print('Catalan Number: C(%d)=%d'%(100,catalan(100)))
