#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 16:28:42 2019

@author: alankar
"""

import numpy as np
import matplotlib.pyplot as plt


def dla_walk(lattice,arrive): #starts a particle from center and moves according to dla rules
    lattice = np.copy(lattice) #not change the original array as they are passed by reference
    y0, x0 = lattice.shape[0]//2, lattice.shape[1]//2
    stuck = False
    end = False
    pos = np.array([y0,x0],dtype=np.int16)
    if (lattice[y0,x0]==0):
        lattice[y0,x0] = arrive
    else: 
        stuck = True
        end = True
    while (not(stuck)):
        posnew = np.zeros(2,dtype=np.int16)
        counter = 0
        while(counter==0 or (posnew[0]>lattice.shape[0]-1) or (posnew[1]>lattice.shape[1]-1) or posnew[0]<0 or posnew[1]<0):
            #Ensures movement is always inside the lattice domain
            counter += 1
            move = np.random.randint(low=0,high=4,size=1)[0] #0:up 1:down 2:left 3:right
            if(move==0): posnew = np.array([pos[0]+1,pos[1]],dtype=np.int16)
            elif(move==1): posnew = np.array([pos[0]-1,pos[1]],dtype=np.int16)
            elif(move==2): posnew = np.array([pos[0],pos[1]-1],dtype=np.int16)
            elif(move==3): posnew = np.array([pos[0],pos[1]+1],dtype=np.int16)
        
        #step += 1
        if (lattice[posnew[0],posnew[1]]>0): stuck = True #stuck on encountering an already anchored particle
        else:
            lattice[pos[0],pos[1]] = 0
            pos = np.copy(posnew)
            lattice[pos[0],pos[1]] = arrive
            if ((pos[0]==(lattice.shape[0]-1)) or (pos[1]==(lattice.shape[1]-1))): stuck = True #stuck at edge
    return (lattice,end)
        


ny, nx = 201, 201
lattice = np.zeros((ny,nx),dtype=np.int16)
end = False
counter = 0
while(not(end)):
    counter+=1
    lattice,end = dla_walk(lattice,counter)

plt.figure(figsize=(13,10))
plt.pcolormesh(lattice)
#plt.colorbar()
plt.title(r'Edge Halting DLA', size=21)
plt.tick_params(axis='both', which='major', labelsize=18)
plt.tick_params(axis='both', which='minor', labelsize=15)
plt.savefig('11_1.png')
plt.show()
