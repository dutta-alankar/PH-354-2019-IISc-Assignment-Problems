# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 20:33:02 2018

@author: Alankar
"""

import numpy as np

def binomial(n,k):
    if k==0: return 1
    return int(np.math.factorial(n)/(np.math.factorial(k)*np.math.factorial(n-k)))

for n in range(0,20):
    for k in range(0,n+1):
        print(binomial(n,k),'  ',end='')
    print('\n',end='')