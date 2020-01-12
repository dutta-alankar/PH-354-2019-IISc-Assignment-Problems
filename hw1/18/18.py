# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 01:54:22 2018

@author: Alankar
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('millikan.txt')
N = len(data[:,0])
Ex = (1/N)*np.sum(data[:,0])
Ey = (1/N)*np.sum(data[:,1])
Exx = (1/N)*np.sum(data[:,0]**2)
Exy = (1/N)*np.sum(data[:,0]*data[:,1])
m,c = (Exy-Ex*Ey)/(Exx-Ex**2), (Exx*Ey-Ex*Exy)/(Exx-Ex**2)
plt.scatter(data[:,0],data[:,1],color='black')
plt.plot(data[:,0],m*data[:,0]+c,color='black')
plt.xlabel('Frequency (hertz)')
plt.ylabel('Stopping Potential (volts)')
plt.savefig('millikan_exp.jpg')
print('Experimental value of Planck\'s constant is %.3e'%(m*1.602e-19))
plt.show()
