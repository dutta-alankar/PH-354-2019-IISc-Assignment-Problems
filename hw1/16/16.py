# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 14:27:15 2018

@author: Alankar
"""

import numpy as np
import matplotlib.pyplot as plt


def xp(r,x):
    return r*x*(1-x)

            
r = np.arange(1,4+0.01,0.01)
x0 = 0.5
iterations = 1000
x = x0*np.ones(len(r))

for i in range(iterations):
    x = xp(r,x)

for i in range(iterations):
    plt.scatter(r,x,color='black',s=0.1)
    x = xp(r,x)
"""
In the Feigenbaum Diagram:
For a given value of r a fixed point is just one point with no other points vertically
above or below. A limit cycle is a fixed finite number of points (vertically) for a given value
of r. The system moves from orderly nature to chaotic (edge of chaos) at r = 3.52
"""
plt.xlabel('r')
plt.ylabel('x')
plt.savefig('fbaum.jpg')    
plt.show()