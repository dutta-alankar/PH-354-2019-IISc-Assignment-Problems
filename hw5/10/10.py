#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 15:39:22 2019

@author: alankar
"""

import numpy as np
import matplotlib.pyplot as plt
from basic_units import radians, sin

"""
u = np.random.uniform(low=0.,high=1.,size=1000)
x = np.piecewise(u,[u<=0.5],[lambda u: np.arccos(1-2*u),lambda u: np.pi-np.arccos(2*u-1)])
plt.hist(x,normed=True)
x = np.linspace(0,np.pi,100)
plt.plot(x,0.5*np.sin(x))
"""

def azim_draw(N):#radians
    u = np.random.uniform(low=0.,high=2*np.pi,size=N)
    return u

def polar_draw(N):#radians
    u = np.random.uniform(low=0.,high=1.,size=N)
    x = np.piecewise(u,[u<=0.5],[lambda u: np.arccos(1-2*u),lambda u: np.pi-np.arccos(2*u-1)])
    return x

phi = [val*radians for val in np.arange(0, 2*np.pi, 0.01)]
theta = [val*radians for val in np.arange(0, np.pi, 0.01)]
N = int(1e5)

plt.figure(figsize=(13,10))
plt.plot(phi,(1/(2*np.pi))*np.ones(len(phi)),xunits=radians,color='black')
plt.hist(azim_draw(N),normed=True,bins=20,color='orange')
plt.grid()
plt.ylabel(r'Probability',size=18)
plt.xlabel(r'Angle (rad)',size=20)
plt.title(r'Distribution of Azimuthal Angle', size=21)
plt.tick_params(axis='both', which='major', labelsize=18)
plt.tick_params(axis='both', which='minor', labelsize=15)
plt.savefig('10_1.png')
plt.show()

plt.figure(figsize=(13,10))
plt.plot(theta,np.array(sin(theta))/2,xunits=radians,color='black')
plt.hist(polar_draw(N),normed=True,bins=20,color='orange')
plt.grid()
plt.ylabel(r'Probability',size=18)
plt.xlabel(r'Angle (rad)',size=20)
plt.title(r'Distribution of Polar Angle', size=21)
plt.tick_params(axis='both', which='major', labelsize=18)
plt.tick_params(axis='both', which='minor', labelsize=15)
plt.savefig('10_2.png')
plt.show()
