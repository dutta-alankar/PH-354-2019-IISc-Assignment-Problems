#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 00:40:50 2019

@author: alankar
"""

import numpy as np
import matplotlib.pyplot as plt
import RK4
import os

#In Code units
G = 1

def f(t,x,M): #F is an array of functions of time
    dim = len(x)//(2*len(M))
    if (len(x)%(2*len(M))!=0): raise Exception('Improper Intial Conditions!')        
    pos = np.array([x[i] for i in range(0,len(x),2)],dtype=np.float32)
    vel = np.array([x[i] for i in range(1,len(x),2)],dtype=np.float32)
    acc = np.zeros(len(pos),dtype=np.float32)
    for i in range(0,len(pos)):
        for j in range(0,len(pos)):
            if (j//dim!=i//dim and j%dim==i%dim): #different body and same coordinates
                dist = 0
                for k in range((j//dim)*dim,(j//dim+1)*dim):
                    dist += (pos[k]-pos[i])**2
                dist = np.sqrt(dist)               
                acc[i] += G*M[j//dim]*(pos[j]-pos[i])/dist**3

    vector = np.zeros((2*len(pos),1))
    counter = 0
    for i in range(0,2*len(pos),2):
        vector[i] = vel[counter]
        vector[i+1] = acc[counter]
        counter += 1
    return vector


t = np.linspace(0,2,1000) #Time in code units
x0 = [3,0,1,0,-1,0,-2,0,-1,0,1,0] # xjb vjb
M = [150,200,250]
delta = 1e-6
t, soln = RK4.RK4_adaptive(f,x0,t,delta,M)

plt.figure(figsize=(13,10))
plt.plot(soln[0],soln[2],label='Body %d'%1)
plt.plot(soln[4],soln[6],label='Body %d'%2)
plt.plot(soln[8],soln[10],label='Body %d'%3)
plt.grid()
plt.ylabel(r'y (Code Units)',size=18)
plt.xlabel(r'x (Code Units)',size=20)
plt.title(r'Trajectory of the point masses under mutual gravity (Adaptive RK4)', size=21)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.legend(loc='best',prop={'size': 18})
plt.savefig('12_1.png')
plt.show()

plt.figure(figsize=(13,10))
plt.plot(soln[0],soln[2],label='Body %d'%1)
plt.plot(soln[4],soln[6],label='Body %d'%2)
plt.plot(soln[8],soln[10],label='Body %d'%3)
plt.xlim(-1.1,5)
plt.ylim(-3,6)
plt.grid()
plt.ylabel(r'y (Code Units)',size=18)
plt.xlabel(r'x (Code Units)',size=20)
plt.title(r'Trajectory of the point masses under mutual gravity (Adaptive RK4) [Zoomed]', size=21, y=1.03)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.legend(loc='best',prop={'size': 18})
plt.savefig('12_2.png')
plt.show()

plt.figure(figsize=(13,10))
plt.plot(soln[0],soln[2],'o',label='Body %d'%1)
plt.plot(soln[4],soln[6],'o',label='Body %d'%2)
plt.plot(soln[8],soln[10],'o',label='Body %d'%3)
plt.grid()
plt.ylabel(r'y (Code Units)',size=18)
plt.xlabel(r'x (Code Units)',size=20)
plt.title(r'Demosnstration of Adaptive RK4 stepping', size=21)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.legend(loc='best',prop={'size': 18})
plt.savefig('12_3.png')
plt.show()

plt.figure(figsize=(13,10))
plt.plot(soln[0],soln[2],'o',label='Body %d'%1)
plt.plot(soln[4],soln[6],'o',label='Body %d'%2)
plt.plot(soln[8],soln[10],'o',label='Body %d'%3)
plt.xlim(-1.1,5)
plt.ylim(-3,6)
plt.grid()
plt.ylabel(r'y (Code Units)',size=18)
plt.xlabel(r'x (Code Units)',size=20)
plt.title(r'Demosnstration of Adaptive RK4 stepping [Zoomed]', size=21)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.legend(loc='best',prop={'size': 18})
plt.savefig('12_4.png')
plt.show()

os.system('mkdir video')
for add in np.arange(0,3*soln.shape[1]//4,1):
    plt.figure(figsize=(13,10))
    plt.xlim(-1.1,5)
    plt.ylim(-3,6)
    plt.ylabel(r'y (Code Units)',size=18)
    plt.xlabel(r'x (Code Units)',size=20)
    plt.grid()
    plt.plot(soln[0,add],soln[2,add],'o',label='Body %d'%1,color='red')
    plt.plot(soln[0,:add+1],soln[2,:add+1],color='red')
    plt.plot(soln[4,add],soln[6,add],'o',label='Body %d'%2,color='green')
    plt.plot(soln[4,:add+1],soln[6,:add+1],color='green')
    plt.plot(soln[8,add],soln[10,add],'o',label='Body %d'%3,color='blue')
    plt.plot(soln[8,:add+1],soln[10,:add+1],color='blue')
    plt.title(r'Demosnstration of Adaptive RK4 stepping [Zoomed]', size=21)
    plt.tick_params(axis='both', which='major', labelsize=15)
    plt.tick_params(axis='both', which='minor', labelsize=12)
    plt.legend(loc='best',prop={'size': 18})
    plt.savefig('video/%03d.png'%add)
    
os.system("ffmpeg -r 5 -i video/%03d.png -vcodec mpeg4 -y 3_body_movie.mp4")
os.system('rm -rf video')