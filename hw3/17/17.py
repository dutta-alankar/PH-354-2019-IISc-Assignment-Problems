#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 22:38:10 2019

@author: alankar
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc,rcParams
from scipy import constants
from scipy.special.orthogonal import p_roots #Legendre Polynomial roots


def phi(q,x,y,x0,y0):
    r = np.sqrt((x-x0)**2+(y-y0)**2)
    return (q/(4*np.pi*constants.epsilon_0*r))

res = 0.01 #1 cm resolution
x = np.arange(-0.5,0.5+res,res) #1m X 1m
y = np.arange(-0.5,0.5+res,res) #1m X 1m

XX, YY = np.meshgrid(x,y)
pot = phi(1.,XX,YY,-0.05,0)+phi(-1.,XX,YY,0.05,0)
pot *= 1e-10
pot = np.piecewise(pot,[pot>=1,pot<=-1],[1,-1,lambda pot: pot])

plt.figure(figsize=(15,10))
plt.pcolormesh(100*x,100*y,pot)
plt.colorbar()

rcParams['contour.negative_linestyle'] = 'solid'
CS = plt.contour(100*x,100*y,pot, 6,colors='white')
plt.clabel(CS, fontsize=18, inline=1, fmt='%1.1f')
plt.xlabel('x(cm)',size=20)
plt.ylabel('y(cm)',size=20)
plt.title(r'Potential $(\times 10^{10}V)$',size=25,y=1.01)

plt.scatter([-5],[0],c='r',marker='o',s=500)
plt.scatter([-5],[0],c='w',marker='+',s=300)
plt.scatter([5],[0],c='r',marker='o',s=500)
plt.scatter([5],[0],c='w',marker='_',s=300)
rc('xtick', labelsize=18) 
rc('ytick', labelsize=18) 
plt.savefig('17_1.png')
plt.show()

def Ex(q,x,y,x0,y0):
    r = np.sqrt((x-x0)**2+(y-y0)**2)
    return (q/(4*np.pi*constants.epsilon_0*r**(3/2.)))*(x-x0)

def Ey(q,x,y,x0,y0):
    r = np.sqrt((x-x0)**2+(y-y0)**2)
    return (q/(4*np.pi*constants.epsilon_0*r**(3/2.)))*(y-y0)

Elec_X = Ex(1.,XX,YY,-0.05,0)+Ex(-1.,XX,YY,0.05,0)
Elec_Y = Ey(1.,XX,YY,-0.05,0)+Ey(-1.,XX,YY,0.05,0)
Elec_X *= 1e-10
Elec_X = np.piecewise(Elec_X,[Elec_X>=1,Elec_X<=-1],[1,-1,lambda Elec_X: Elec_X])
Elec_Y *= 1e-10
Elec_Y = np.piecewise(Elec_Y,[Elec_Y>=1,Elec_Y<=-1],[1,-1,lambda Elec_Y: Elec_Y])

plt.figure(figsize=(15,10))

plt.streamplot(x*100,y*100,Elec_X,Elec_Y,color='white')
plt.pcolormesh(x*100,y*100,np.sqrt(Elec_X**2+Elec_Y**2))
plt.colorbar()

plt.title(r'Electric field ($\times 10^{10} Vm^{-1}$)',size=25,y=1.01)
plt.scatter([-5],[0],c='r',marker='o',s=500)
plt.scatter([-5],[0],c='w',marker='+',s=300)
plt.scatter([5],[0],c='r',marker='o',s=500)
plt.scatter([5],[0],c='w',marker='_',s=300)
plt.xlabel('x(cm)',size=20)
plt.ylabel('y(cm)',size=20)
rc('xtick', labelsize=18) 
rc('ytick', labelsize=18) 
plt.savefig('17_2.png')
plt.show()

#-----------------------------------------------------------------------------------

N = 10
"""
def gauss_quad(func,a,b,n,*args):#Legendre
    [x,w] = p_roots(n+1)
    I_G = 0.5*(b-a)*np.sum(w*func(0.5*(b-a)*x+0.5*(b+a),*args))
    return I_G

def gauss_quad_2d(func,a,b,n,*args):#Legendre 
    I_G = gauss_quad(lambda y:gauss_quad(func,a[0],b[0],n[0],y,*args),a[1],b[1],n[1])
    return I_G
"""
def gauss_quad_2d(func,a,b,n,*args):#Legendre 
    [x,wx] = p_roots(n[0]+1)
    [y,wy] = p_roots(n[1]+1)
    x,y = np.meshgrid(x,y)
    wx,wy = np.meshgrid(wx,wy)
    I_G = 0.5*(b[0]-a[0])*0.5*(b[1]-a[1])*np.sum(wx*wy*\
              func(0.5*(b[0]-a[0])*x+0.5*(b[0]+a[0]),0.5*(b[1]-a[1])*y+0.5*(b[1]+a[1]),*args))
    return I_G

def phi(x,y,sigma,L): #L in m
    I = lambda xp,yp:sigma(xp,yp)/np.sqrt((x-xp)**2+(y-yp)**2)
    return (1./(4*np.pi*constants.epsilon_0))*gauss_quad_2d(I,[-L/2.,-L/2.],[L/2.,L/2.],[N,N])

def Ex(x,y,sigma,L):
    I = lambda xp,yp:sigma(xp,yp)*(x-xp)/((x-xp)**2+(y-yp)**2)**1.5
    return (1./(4*np.pi*constants.epsilon_0))*gauss_quad_2d(I,[-L/2.,-L/2.],[L/2.,L/2.],[N,N])

def Ey(x,y,sigma,L):
    I = lambda xp,yp:sigma(xp,yp)*(y-yp)/((x-xp)**2+(y-yp)**2)**1.5
    return (1./(4*np.pi*constants.epsilon_0))*gauss_quad_2d(I,[-L/2.,-L/2.],[L/2.,L/2.],[N,N])



q0 = 100 #cm^-2
L = 10 #cm
sigma = lambda x,y: q0*np.sin(2*np.pi*x/L)*np.sin(2*np.pi*y/L) #x and y converted to cm

res = 0.01 #1 cm resolution
x = np.arange(-0.5,0.5+res,res) #1m X 1m
y = np.arange(-0.5,0.5+res,res) #1m X 1m

pot = np.zeros((len(y),len(x)))
Elec_X = np.zeros((len(y),len(x)))
Elec_Y = np.zeros((len(y),len(x)))

for i in range(len(x)):
    for j in range(len(y)):
        pot[j,i] = phi(x[i],y[j],sigma,L*1e-2) #L is converted to m
        Elec_X[j,i] = Ex(x[i],y[j],sigma,L*1e-2) #L is converted to m
        Elec_Y[j,i] = Ey(x[i],y[j],sigma,L*1e-2) #L is converted to m


pot = np.piecewise(pot,[np.abs(pot)>=1e6],[lambda pot:1e6*np.abs(pot)/pot,lambda pot: pot])
pot *= 1e-3
plt.figure(figsize=(13,10))        
plt.pcolormesh(100*x,100*y,pot)
plt.colorbar()

rcParams['contour.negative_linestyle'] = 'solid'
CS = plt.contour(100*x,100*y,pot,5,colors='white')#,locator=ticker.LogLocator())
plt.clabel(CS, fontsize=18, inline=1, fmt='%1.1f')
plt.xlabel('x(cm)',size=20)
plt.ylabel('y(cm)',size=20)
plt.title(r'Potential $(\times 10^{3}V)$',size=25,y=1.01)
plt.savefig('17_3.png')
plt.show()


plt.figure(figsize=(13,10))

Elec_X[50,50], Elec_Y[50,50] = 0., 0.
E = np.sqrt(Elec_X**2+Elec_Y**2)
E *= 1e-6
E = np.piecewise(E,[E>=1.e3],[1.e3,lambda E: E])
plt.streamplot(x*100,y*100,Elec_X,Elec_Y,color='white')
plt.pcolormesh(x*100,y*100,np.log10(E))
plt.colorbar()

plt.title(r'Electric field ($\times 10^{6} Vm^{-1}$)',size=25,y=1.01)
plt.xlabel('x(cm)\nlogged colormap for magnitude of Electric field',size=20)
plt.ylabel('y(cm)',size=20)
rc('xtick', labelsize=18) 
rc('ytick', labelsize=18) 
plt.savefig('17_4.png')
plt.show()
