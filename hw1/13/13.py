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

cutoff = 1000
plt.plot(data[:cutoff+1,0],data[:cutoff+1,1])
plt.ylabel('# of Sunspots')
plt.xlabel('# of months since Jan 1749')
plt.savefig('sunspots_1000.jpg')
plt.show()

r = 5
Yk=[]
for k in range (r,cutoff+1):
    yk = np.sum(data[k-r:k+r+1,1])
    Yk.append((1/(2*r))*yk)
Yk = np.array(Yk)
plt.plot(data[:cutoff+1,0],data[:cutoff+1,1],color='blue',label = 'Sunspot data')
plt.ylabel('# of Sunspots')
plt.xlabel('# of months since Jan 1749')
plt.plot(data[r:cutoff+1,0],Yk,color='red',label='Running Average (r=5)')
plt.legend(loc='best')
plt.savefig('sunspots_with_running_avg.jpg')
plt.show()
