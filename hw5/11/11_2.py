#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 18:46:28 2019

@author: alankar
"""

import numpy as np
import matplotlib.pyplot as plt


def dla_walk_org(lattice,arrive,rad): #starts a particle from center and moves according to dla rules
    #print(rad)
    lattice = np.copy(lattice) #not change the original array as they are passed by reference
    #rad += 1 
    y0, x0 = lattice.shape[0]//2, lattice.shape[1]//2
    lattice[y0,x0] = 1
    lattice_hold = np.copy(lattice) #saves the initial state
    stuck = False
    end = False
    
    xstart, ystart = 0, 0    
    counter = 0
    while (lattice[ystart,xstart]>0 or counter==0):
        counter+=1
        angle = np.random.uniform(low=-np.pi,high=np.pi,size=1)[0]
        xstart, ystart = int(np.ceil(x0+(rad+1)*np.cos(angle))), int(np.ceil(y0+(rad+1)*np.sin(angle)))
        
    lattice[ystart,xstart] = arrive
    pos = np.array([ystart,xstart],dtype=np.int16)
    #else: 
    #    stuck = True
    if(rad>=x0//2 or rad>=y0//2): 
        end = True
        stuck = True
        lattice[ystart,xstart] = 0 #undo the last entry
    if (lattice[ystart-1,xstart]>0 or lattice[ystart+1,xstart]>0 or lattice[ystart,xstart-1]>0 or lattice[ystart,xstart+1]>0):
        #already starts stuck
        stuck = True
        rad = np.max([rad,np.sqrt((pos[0]-y0)**2+(pos[1]-x0)**2)])
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
        if (lattice[posnew[0],posnew[1]]>0): 
            stuck = True #stuck on encountering an already anchored particle
            rad = np.max([rad,np.sqrt((pos[0]-y0)**2+(pos[1]-x0)**2)])
        else:
            lattice[pos[0],pos[1]] = 0
            pos = np.copy(posnew)
            lattice[pos[0],pos[1]] = arrive
            #if ((pos[0]==(lattice.shape[0]-1)) or (pos[1]==(lattice.shape[1]-1))): stuck = True #stuck at edge
        if (np.sqrt((pos[0]-y0)**2+(pos[1]-x0)**2)>=2*rad):
            stuck = True
            lattice, rad, end = dla_walk_org(lattice_hold,arrive, rad) #restart the walk
    return (lattice,rad,end)
        


ny, nx = 201, 201
lattice = np.zeros((ny,nx),dtype=np.int16)
end = False
counter = 1 #the stuck initial particle corresponds to the first arrival
rad = 0.
while(not(end)):
    counter+=1
    lattice,rad,end = dla_walk_org(lattice,counter,rad)

plt.figure(figsize=(13,10))
plt.pcolormesh(lattice)
#plt.colorbar()
plt.title(r'Center joining DLA', size=21)
plt.tick_params(axis='both', which='major', labelsize=18)
plt.tick_params(axis='both', which='minor', labelsize=15)
plt.savefig('11_2.png')
plt.show()
