#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 01:25:05 2019

@author: alankar
"""

import numpy as np
import matplotlib.pyplot as plt
import RK4

def f_drag(t,x,m,rho,C,R,g): #Quadratic drag model
    x, x1, y, x2 = x
    xdot = x1
    ydot = x2
    x1dot = -(np.pi/(2*m))*R**2*rho*C*xdot*np.sqrt(xdot**2+ydot**2)
    x2dot = -(np.pi/(2*m))*R**2*rho*C*ydot*np.sqrt(xdot**2+ydot**2) - g
    return np.array([[xdot,x1dot,ydot,x2dot]]).T

def f_no_drag(t,x,g):
    x, x1, y, x2 = x
    xdot = x1
    ydot = x2
    x1dot = 0
    x2dot = - g
    return np.array([[xdot,x1dot,ydot,x2dot]]).T

m = 1 #kg
R = 8*1e-2 #m
angle = 30 #deg
v0 = 100 #m/s
rho = 1.22 #kg/m^3
C = 0.47
g = 9.8 #ms^-2
x0 = [0,v0*np.cos(np.deg2rad(angle)),0,v0*np.sin(np.deg2rad(angle))] #x=0 vx, y=0 vy

t = np.linspace(0,7,10000)
soln = RK4.RK4(f_drag,x0,t,m,rho,C,R,g)
t_no_drag = np.linspace(0,10.5,10000)
no_drag = RK4.RK4(f_no_drag,x0,t_no_drag,g)

plt.figure(figsize=(13,10))
plt.plot(soln[0],soln[2],label=r'Quadratic Drag Model')
plt.plot(no_drag[0],no_drag[2],label=r'No Drag Model')
plt.grid()
plt.ylabel(r'y (m)',size=18)
plt.xlabel(r'x (m)',size=20)
plt.ylim(0,130)
plt.title(r'Trajectory of a Projectile', size=21)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.legend(loc='best',prop={'size': 18})
plt.savefig('5_1.png')
plt.show()

m = np.linspace(0.1,10,100)
freq = 25
Range = np.zeros(len(m))

t = np.linspace(0,20,1000)
plt.figure(figsize=(13,10))
for idx, mass in enumerate(m):
    soln = RK4.RK4(f_drag,x0,t,mass,rho,C,R,g)
    Range[idx] = soln[0,np.argmax(soln[2,:]<0)-1]-soln[0,0]
    if(idx%freq==0): plt.plot(soln[0],soln[2],label=r'mass = %.2f'%mass)

plt.plot(no_drag[0],no_drag[2],label=r'No Drag Model')
plt.grid()
plt.ylabel(r'y (m)',size=18)
plt.xlabel(r'x (m)',size=20)
plt.ylim(0,130)
plt.title(r'Trajectory of a Projectile with Quadratic Drag model', size=21)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.legend(loc='best',prop={'size': 18})
plt.savefig('5_2.png')
plt.show()
    
plt.figure(figsize=(13,10))
plt.plot(m,Range)
plt.grid()
plt.ylabel(r'Range (m)',size=18)
plt.xlabel(r'Mass (kg)',size=20)
plt.title(r'Projectile Trajectory without Drag', size=21)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=12)
plt.savefig('5_3.png')
plt.show()
 