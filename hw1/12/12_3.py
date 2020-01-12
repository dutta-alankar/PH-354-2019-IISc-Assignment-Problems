# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 10:45:11 2018

@author: Alankar
"""


def g(m,n):
    if (n==0): return m
    return g(n,m%n)
    
print('The Greatest Common Divisor of %d and %d is %d'%(108,192,g(108,192))) 
