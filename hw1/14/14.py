# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 12:09:50 2018

@author: Alankar
"""

import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0,2*np.pi,1000)
x = 2*np.cos(theta) + np.cos(2*theta)
y = 2*np.sin(theta) - np.sin(2*theta)

plt.plot(x,y)
plt.savefig('deltoid.jpg')
plt.show()

theta = np.linspace(0,10*np.pi,10000)
r = theta**2
x = r*np.cos(theta)
y = r*np.sin(theta)
plt.plot(x,y)
plt.savefig('galilean_spiral.jpg')
plt.show()

theta = np.linspace(0,24*np.pi,100000)
r = np.exp(np.cos(theta)) - 2*np.cos(4*theta) + (np.sin(theta/12))**5
x = r*np.cos(theta)
y = r*np.sin(theta)
plt.plot(x,y)
plt.savefig('fey.jpg')
plt.show()