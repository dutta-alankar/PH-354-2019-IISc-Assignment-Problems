# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 04:46:16 2018

@author: Alankar
"""
import numpy as np

def cart_to_pol(x,y):
    r = np.sqrt(x**2+y**2)
    if (x>0 and y>0):
        theta = np.arctan2(np.abs(y),np.abs(x))
    elif(x>0 and y<0):
        theta = -np.arctan2(np.abs(y),np.abs(x))
    elif(x<0 and y>0):
        theta = np.pi - np.arctan2(np.abs(y),np.abs(x))
    elif(x<0 and y<0):
        theta = np.pi + np.arctan2(np.abs(y),np.abs(x))
    else:
        theta = 0
    return (r,theta*(180/np.pi))

x = float(input('Enter abcissa (x-coordinate): '))
y = float(input('Enter ordinate (y-coordinate): '))
print('In Polar:\nr = %.4f\ntheta = %.4f (degrees)'%cart_to_pol(x,y))