#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 10:02:30 2019

@author: alankar
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import datetime


def update(lattice): #same number on adjacent lattice site corresponds to the same dimer
    lattice = np.copy(lattice) #ensure the original lattice isn't overwritten as arrays are passed by reference
    count = int(np.max(lattice))
    ny, nx = lattice.shape
    posx = np.random.randint(low=0,high=nx)
    posy = np.random.randint(low=0,high=ny)
    neigh_pos = []
    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        neighy = (posy + dy) % ny #Periodic boundary condition
        neighx = (posx + dx) % nx #Periodic boundary condition
        neigh_pos.append([neighy,neighx])
    neigh_pos = np.array(neigh_pos,dtype=np.int16)
    choose = np.random.randint(low=0,high=4) #randomly choose an adjacent site
    neigh_pos = neigh_pos[choose]
    site = np.array([[posy,posx],neigh_pos],dtype=np.int16)
    if(lattice[site[0,0],site[0,1]]>0):#occupied
        if(lattice[site[0,0],site[0,1]]==lattice[site[1,0],site[1,1]]):#same dimer
            remove = lattice[site[0,0],site[0,1]] #dimer no removed
            lattice[site[0,0],site[0,1]]=0
            lattice[site[1,0],site[1,1]]=0
            for r in range(ny):
                for c in range(nx):
                    if (lattice[r,c]>remove): lattice[r,c] -= 1 #all dimer numbers above the one removed falls down by 1 count
    elif((lattice[site[0,0],site[0,1]]==0) and (lattice[site[1,0],site[1,1]]==0)):
        count += 1
        lattice[site[0,0],site[0,1]]=count
        lattice[site[1,0],site[1,1]]=count
    return lattice

def MCMC_SA(x0,steps,cool_speed = 1.,T0 = 1):
    ny, nx = x0.shape
    kB = 1
    T = T0
    pos = np.zeros((steps+1,ny,nx),dtype=np.float64)
    pos[0] = x0
    xold = x0
    xnew = x0
    Eold = -int(np.max(x0))
    #delT = -10/steps
    for i in range(steps): 
        xnew = update(xold)
        Enew = -int(np.max(xnew))
        alpha = np.exp(-(Enew-Eold)/(kB*T))
        u = np.random.uniform(low=0.,high=1.,size=1)
        if (u>alpha): #reject
            xnew = np.copy(xold)
            pos[i+1] = xold
            Enew=Eold
        else: #accept
            pos[i+1] = xnew
            Eold=Enew
            xold = np.copy(xnew)
        T = T0*np.exp(-cool_speed*i/(steps-1))
        #while (T+delT<=0): delT/=2
        #T += delT
    #print(T)
    return (pos,int(np.max(pos[-1,:,:])))

#Dimers are numbered according to their increasing time of entry in the lattice
Lx, Ly = 50, 50
lattice = np.zeros((Ly,Lx),dtype=np.int16)
steps=int(1e4)
pos,dimers=MCMC_SA(lattice,steps,cool_speed=3.0)
holes = Lx*Ly - np.count_nonzero(pos[-1,:,:])
fill_frac = 1-holes/(Lx*Ly)
print('Total number of dimers: %d'%dimers)
print('Fraction of lattice filled by dimers: %f'%fill_frac)

fig = plt.figure(figsize=(10,10))
ims = []

for add in np.arange(0,pos.shape[0]//4,1):
    ims.append((plt.pcolor(pos[add,:-1, :-1],cmap='nipy_spectral'),)) 

im_ani = animation.ArtistAnimation(fig, ims, interval=35, repeat_delay=1000, blit=True)
im_ani.save('Dimer Filling.mp4', metadata={'Artist':'Alankar','Album':'PH 354','Comment':'steps = %d'%steps,'Title':'Dimer Covering Problem','Year':datetime.datetime.now().year})
plt.show()