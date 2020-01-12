# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 14:08:39 2018

@author: Alankar
"""

import numpy as np
import matplotlib.pyplot as plt

profile = np.loadtxt('stm.txt')
x = np.arange(0,len(profile[0,:])+1,1)
y = np.arange(0,len(profile[:,0])+1,1)
plt.axis([0,len(x),0,len(y)])
plt.pcolor(profile,cmap='jet')
plt.colorbar()
plt.savefig('silicon_surface.jpg')
plt.show()