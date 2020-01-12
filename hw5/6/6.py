#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 13:10:53 2019

@author: alankar
"""

import numpy as np
#import matplotlib.pyplot as plt

N = int(1e6)
#u = np.random.uniform(low=0.,high=1.,size=N)
#plt.hist(u**2,normed=True)
#x = np.linspace(0,1,100)
#plt.plot(x,1/(2*np.sqrt(x)))
f = lambda x: (1/np.sqrt(x))/(np.exp(x)+1)
w = lambda x:1/np.sqrt(x)
points = np.random.uniform(low=0.,high=1.,size=N)**2
norm = 2.
I = (norm/N)*np.sum(f(points)/w(points))
varf = (1/N)*np.sum((f(points)/w(points))**2)-((1/norm)*I)**2
error = np.sqrt(varf/N)*norm
print('Value of the Integral: %f'%I)
print('Error in the estimate: %f'%error)

"""
Output:
    
Value of the Integral: 0.838967
Error in the estimate: 0.000141
"""