#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 16:23:09 2019

@author: alankar
"""

import numpy as np
#import matplotlib.pyplot as plt

distance = lambda x:np.dot(x,x.T)

dimension = 10
N = int(1e4)
x = np.random.uniform(low=-1,high=1,size=(N,dimension))
length = np.diag(distance(x))
f = np.piecewise(length,[length<=1.],[1.,0.])
I = (2**dimension/N)*np.sum(f)
varf = (1/N)*np.sum(f**2)-(I/2**dimension)**2
error = (2**dimension)*np.sqrt(varf/N)
print('Volume of a unit sphere in %d dimension: %f'%(dimension,I))
print('Error in the estimate: %f'%error)

"""
Output:
    
Volume of a unit sphere in 10 dimension: 2.150400
Error in the estimate: 0.468763
"""