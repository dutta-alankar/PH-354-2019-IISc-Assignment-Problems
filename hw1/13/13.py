# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 11:10:11 2018

@author: Alankar
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('sunspots.txt')
plt.plot(data[:,0],data[:,1])
plt.ylabel('# of Sunspots')
plt.xlabel('# of months since Jan 1749')
plt.savefig('sunspots_all.jpg')
plt.show()

plt.plot(data[:1001,0],data[:1001,1])
plt.ylabel('# of Sunspots')
plt.xlabel('# of months since Jan 1749')
plt.savefig('sunspots_1000.jpg')
plt.show()

r = 5
Yk=[]
for k in range (r,1001):
    yk = 0
    for m in range(-r,r):
        yk += data[k+m,1]
    Yk.append((1/(2*r))*yk)
Yk = np.array(Yk)
plt.plot(data[:1001,0],data[:1001,1],color='blue',label = 'Sunspot data')
plt.ylabel('# of Sunspots')
plt.xlabel('# of months since Jan 1749')
plt.plot(data[r:1001,0],Yk,color='red',label='Running Average (r=5)')
plt.legend(loc='best')
plt.savefig('sunspots_with_running_avg.jpg')
plt.show()

