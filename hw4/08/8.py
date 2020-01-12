#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 17:48:45 2019

@author: alankar
"""

import numpy as np
import matplotlib.pyplot as plt

pic = np.loadtxt('blur.txt')
sizey = pic.shape[0]
sizex = pic.shape[1]

sigma = 25.
gauss = lambda x,xc:np.exp(-(x-xc)**2/(2*sigma**2))

def point_spread(x,y): 
    fx = np.piecewise(np.asarray(x,dtype=np.float64),[x<sizex//2],[lambda x: gauss(x,0),lambda x: gauss(x,sizex)])  #gauss(x,0)+gauss(x,sizex-1)
    fy = np.piecewise(np.asarray(y,dtype=np.float64),[y<sizey//2],[lambda y: gauss(y,0),lambda y: gauss(y,sizey)])  #gauss(y,0)+gauss(y,sizey-1)
    
    fx, fy = np.meshgrid(fx,fy)
    return fx*fy

x = np.arange(0,sizex,1)
y = np.arange(0,sizey,1)

plt.figure(figsize=(13,10))
plt.pcolormesh(x,-y,pic,cmap='gray')
#plt.colorbar()
plt.xticks([])
plt.yticks([])
plt.savefig('8_1.png')
plt.show()

plt.figure(figsize=(13,10))
pspread = point_spread(x,y)
plt.pcolormesh(x,-y,pspread,cmap='gray')
#plt.colorbar()
plt.xticks([])
plt.yticks([])
plt.savefig('8_2.png')
plt.show()


pspread_fft = np.fft.rfft2(pspread,axes=(-1,-2))
pic_fft = np.fft.rfft2(pic,axes=(-1,-2))
epsilon = 1e-3


pspread_fft = np.piecewise(pspread_fft,[np.abs(pspread_fft)<=epsilon],[epsilon,lambda pspread_fft:pspread_fft])

pic_sharp_fft = pic_fft/pspread_fft
pic_sharp = np.fft.irfft2(pic_sharp_fft,axes=(-1,-2))

plt.figure(figsize=(13,10))
plt.pcolormesh(x,-y,pic_sharp,cmap='gray')
#plt.colorbar()
plt.xticks([])
plt.yticks([])
plt.savefig('8_3.png')
plt.show()
