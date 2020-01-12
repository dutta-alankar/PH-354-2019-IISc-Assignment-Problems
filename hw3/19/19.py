#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 21:50:36 2019

@author: alankar
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import time
from PIL import Image


def gradient(val,dx,dy): #forward difference for boundary and central for others
    #global grad
    grad = np.zeros((2,len(val[:,0]),len(val[0])))
    grad[0,:,0]=(val[:,1]-val[:,0])/dx
    grad[0,:,-1]=(val[:,-1]-val[:,-2])/dx
    grad[1,-1,:]=(val[-1,:]-val[-2,:])/dy
    grad[1,0,:]=(val[1,:]-val[0,:])/dy
    for i in range(1,len(val[0])-1):
        grad[0,:,i] = (val[:,i+1]-val[:,i-1])/(2*dx)
    for i in range(1,len(val[:,0])-1):
        grad[1,i,:] = (val[i+1,:]-val[i-1,:])/(2*dy)
    return grad

def Intensity(theta,phi,altitude,h):
    theta = 90. - theta
    theta = np.deg2rad(theta)
    phi = np.deg2rad(phi)
    grad = gradient(altitude,h,h)
    #grad = np.gradient(altitude,h,h)
    return (np.sin(theta)*np.cos(phi)*grad[0]+np.sin(theta)*np.sin(phi)*grad[1]-np.cos(theta))/np.sqrt(grad[0]**2+grad[1]**2+1)


#im = Image.open('cdnf45k_kolkata.tif')
#altitude = np.array(im)
#plt.figure(figsize=(13,10))
#plt.pcolormesh(altitude,vmin=15,vmax=35)
#plt.show()
altitude = np.loadtxt('altitude.txt')
h = 30000 #m
#h = 2
x = np.arange(0,len(altitude[0]),1)*h
y = np.arange(0,len(altitude[:,0]),1)*h

z = Intensity(0.,30.,altitude,h)

fig = plt.figure(figsize=(13,7))
plt.xticks([])
plt.yticks([])

print('Plotting...')
t = time.time()
plt.pcolormesh(x,-y,-z,cmap=cm.magma,vmax=1e-2,vmin=-1e-2) #gist_earth
#plt.imshow(-z)
plt.savefig('19_1.png')
print('Took %.2f secs'%(time.time()-t))
plt.show()




altitude = np.loadtxt('stm.txt')
h = 2.5
x = np.arange(0,len(altitude[0]),1)*h
y = np.arange(0,len(altitude[:,0]),1)*h
z = Intensity(0.,30.,altitude,h)

fig = plt.figure(figsize=(9,7))
plt.xticks([])
plt.yticks([])

print('Plotting...')
t = time.time()
plt.pcolormesh(x,-y,-z,cmap=cm.inferno)
plt.savefig('19_2.png')
print('Took %.2f secs'%(time.time()-t))
plt.show()

"""
fig = plt.figure(figsize=(13,10))
ax = fig.gca(projection='3d')
x,y = np.meshgrid(x,y)
#z = np.piecewise(z,[z>=0.4,z<=-0.4],[0.4,-0.4,lambda z: z])
xnew, ynew = np.mgrid[-1:1:80j, -1:1:80j]
tck = interpolate.bisplrep(x, y, z, s=0)
znew = interpolate.bisplev(xnew[:,0], ynew[0,:], tck)
surf = ax.plot_surface(xnew, ynew, znew, cmap=cm.gist_earth,
                       linewidth=0, antialiased=True)
plt.show()
"""