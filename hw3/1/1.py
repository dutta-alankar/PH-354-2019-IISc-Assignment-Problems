#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 12:06:53 2019

@author: alankar
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('velocities.txt')

h = data[1,0]-data[0,0]
sumover = 0
initial_pos = 0.
dist = np.zeros(len(data[:,0]))

for i in range(1,len(dist)):
    sumover += (data[i-1,1]+data[i,1])*(h/2)
    dist[i] = sumover
dist += initial_pos
 
plt.figure(figsize=(10,5))
plt.plot(data[:,0],data[:,1],label='velocity')
plt.plot(data[:,0],dist,label='displacement')
plt.legend(loc='best')
plt.grid()
plt.savefig('1.png')
plt.show()