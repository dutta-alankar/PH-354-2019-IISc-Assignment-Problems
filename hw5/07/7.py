#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 22:46:01 2019

@author: alankar
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import datetime

J = 1.0

def Energy(lattice):
    E = 0.
    ny,nx = lattice.shape
    for i in range(ny):
        for j in range(nx):
            #implementing periodic boundary condition
            spin_neighbour = np.hstack((np.take(lattice[i],[j-1,j+1],mode='wrap'),np.take(lattice[:,j],[i-1,i+1],mode='wrap')))
            E += np.sum(lattice[i,j]*spin_neighbour)
    return -J*(E/2) #double counted each neighbouring pair

def MCMC_MH(x0,steps,T = 1):
    #Randomly chosen lattice point flip as jumping distribution is assumed
    kB = 1
    till = int((30/100)*steps) 
    pos = np.zeros(steps+1,dtype=np.float64)
    Mag = pos = np.zeros(steps+1,dtype=np.float64)
    freq = int((0.01/100)*steps)
    config = [x0]
    pos[0] = Energy(x0)
    Mag[0] = np.sum(x0)
    xold = np.copy(x0)
    xnew = np.copy(x0)
    Eold = Energy(xold)
    ny,nx = x0.shape
    for i in range(steps):
        flip = np.array([np.random.randint(low=0,high=ny,dtype=np.int16),np.random.randint(low=0,high=nx,dtype=np.int16)],dtype=np.int16)
        xnew[flip[0],flip[1]]  *= -1
        spin_neighbour = np.hstack((np.take(xnew[flip[0]],[flip[1]-1,flip[1]+1],
                                            mode='wrap'),np.take(xnew[:,flip[1]],[flip[0]-1,flip[0]+1],mode='wrap')))
        Enew = Eold-2*(-J*np.sum(xold[flip[0],flip[1]]*spin_neighbour))
        #if (i==0 or i==1 or i==2 or i==3):
        #    print(Enew)
        #    print(Energy(xnew))
        alpha = np.exp(-(Enew-Eold)/(kB*T))
        u = np.random.uniform(low=0.,high=1.,size=1)
        if (u>alpha): #reject
            xnew = np.copy(xold)
            pos[i+1] = Eold
            Enew=Eold
        else: #accept
            pos[i+1] = Enew
            Eold=Enew
            xold = np.copy(xnew)
        Mag[i+1] = np.sum(xnew)
        if(i%freq==0 and i<=till): config.append(xold) #
    return (pos,np.array(config),Mag)
        

nx = 20
ny = 20
Temperature = 1
#spin = 1:up          spin = -1:down
#latticex,latticey = np.meshgrid(np.arange(0,nx,1,dtype=np.int16),np.arange(0,ny,1,dtype=np.int16))
lattice = np.random.randint(low=-1,high=1,size=(ny,nx),dtype=np.int16)
lattice += (lattice+1)

steps = int(1e6)
pos, lattice, M = MCMC_MH(lattice,steps,T=Temperature)
burn_in = int((10/100)*steps) #After the burnin steps, the auto-correlation drops to very low value of the MCMC steps
E = np.average(pos[burn_in:])
delE = np.std(pos[burn_in:])

plt.figure(figsize=(13,10))
plt.plot(np.arange(0,steps+1,1),pos)
plt.grid()
plt.xlabel(r'MCMC step',size=18)
plt.ylabel(r'Energy',size=20)
plt.title(r'Energy of the system', size=21)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.savefig('7_1_T=%d.png'%Temperature)
plt.show()

plt.figure(figsize=(13,10))
plt.plot(np.arange(0,steps+1,1),M)
plt.grid()
plt.xlabel(r'MCMC step',size=18)
plt.ylabel(r'Magnetization',size=20)
plt.title(r'Magnetization of the system', size=21)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.savefig('7_2_T=%d.png'%Temperature)
plt.show()

plt.figure(figsize=(10,10))
plt.pcolor(lattice[-1],cmap='gray')
plt.xlabel(r'$x$',size=18)
plt.ylabel(r'$y$',size=20)
plt.title(r'T=%d Ising Model lattice Final Configuration'%Temperature, size=21)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.savefig('7_3_T=%d.png'%Temperature)
plt.show()

fig = plt.figure(figsize=(13,10))
ims = []

for add in np.arange(0,lattice.shape[0]//6,1):
    ims.append((plt.pcolor(lattice[add,:-1, :-1],cmap='gray'),)) 

im_ani = animation.ArtistAnimation(fig, ims, interval=30, repeat_delay=1000, blit=True)
im_ani.save('T=%d_Ising.mp4'%Temperature, metadata={'Artist':'Alankar','Album':'PH 354','Comment':'Temperature = %d'%Temperature,'Title':'2D Ising Model','Year':datetime.datetime.now().year})
plt.show()