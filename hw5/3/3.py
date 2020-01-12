#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 12:00:33 2019

@author: alankar
"""
import numpy as np
import matplotlib.pyplot as plt
from time import time

L = 101
x = np.arange(0,L,1)
y = np.arange(0,L,1)

x0 = (L-1)//2
y0 = (L-1)//2

steps = int(4e4)

x_particle = x0
y_particle = y0
pos = np.zeros((steps-1,2),dtype=np.int32) #-1 because the initial position is considered as step 0

np.random.seed(int(time()))
for step in range(1,steps,1):
    pos[step-1,:] = np.array([x_particle,y_particle],dtype=np.int32)
    counter = 0
    while(x_particle>=L or x_particle<0 or y_particle>=L or y_particle<0 or counter==0):
        #Undo the overshoots and undershoots
        if(x_particle>=L): x_particle-=1
        if(y_particle>=L): y_particle-=1
        if(x_particle<0): x_particle+=1
        if(y_particle<0): y_particle+=1
        move = np.random.randint(low=0,high=4) #0:up 1:down 2:left 3:right
        if(move==0):y_particle+=1
        elif(move==1):y_particle-=1
        elif(move==2):x_particle-=1
        elif(move==3):x_particle+=1   
        counter+=1
        

plt.figure(figsize=(13,10))
plt.plot(pos[:,0],pos[:,1])
plt.grid()
plt.xlabel(r'$x$',size=18)
plt.ylabel(r'$y$',size=20)
plt.title(r'Confined Random Walk', size=21)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.xlim(-1,L)
plt.ylim(-1,L)
plt.savefig('3.png')
plt.show()