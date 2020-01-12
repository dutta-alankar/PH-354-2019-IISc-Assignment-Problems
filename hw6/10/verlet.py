#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 20:55:47 2019

@author: alankar
"""

import numpy as np

def VLET(f,x0,t,*args): #f must be a matrix of order (dim,1)
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
        vhalf = x[:,i-1] + (h/2)*f(t[i-1],x[:,i-1],*args)[:,0]
        for j in range(0,dim,2):  
            x[j,i] = x[j,i-1] + h*vhalf[j+1]
        k = h*f(t[i],x[:,i],*args)[:,0]
        for j in range(1,dim,2): 
            x[j,i] = vhalf[j] + k[j]/2
        
    return x