#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 10:28:55 2019

@author: alankar
"""

import numpy as np

def RK4(f,x0,t,*args): #f must be a matrix of order (dim,1)
    if isinstance(t,list): 
        t = np.array(t)
    elif not(isinstance(t,np.ndarray) or isinstance(t,list)): 
        t = np.array([0,t])
        
    if isinstance(x0,list): 
        x0 = np.array(x0)
    elif not(isinstance(x0,np.ndarray) or isinstance(x0,list)): 
        x0 = np.array([x0])

    x = np.zeros((x0.shape[0],t.shape[0],),dtype=np.float64)
    h = t[1] - t[0]
    x[:,0] = x0 #Initial Condition
    dim = x0.shape[0]
    
    for i in range(1,t.shape[0]):
        k1, k2, k3, k4 = None, None, None, None
        
        if (dim==1):
            k1 = f(t[i-1],x[:,i-1],*args)*h
            k2 = f(t[i-1]+h/2,x[:,i-1]+k1/2,*args)*h
            k3 = f(t[i-1]+h/2,x[:,i-1]+k2/2,*args)*h
            k4 = f(t[i-1]+h,x[:,i-1]+k3,*args)*h
            
            x[:,i] = x[:,i-1] + (k1+2*(k2+k3)+k4)/6
        else:
            k1 = f(t[i-1],x[:,i-1],*args)*h
            k2 = f(t[i-1]+h/2,x[:,i-1]+k1[:,0]/2,*args)*h
            k3 = f(t[i-1]+h/2,x[:,i-1]+k2[:,0]/2,*args)*h
            k4 = f(t[i-1]+h,x[:,i-1]+k3[:,0],*args)*h
            
            x[:,i] = x[:,i-1] + (k1[:,0]+2*(k2[:,0]+k3[:,0])+k4[:,0])/6
    
    if (x.shape[0]==1): return x[0]
    return x

