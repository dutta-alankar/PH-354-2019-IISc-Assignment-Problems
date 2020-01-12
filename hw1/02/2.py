# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 18:06:25 2018

@author: Alankar
"""

import numpy as np

ME, RE = 5.972e24, 6371 #in SI
G = 6.67e-11

def height(T):
    return (((G*(ME*1e3)*T**2)/(4*np.pi**2))**(1/3))*1e-3-RE # in km

print('-----------------------------------------------------------')
print('Demo Output:')
print('The satellite with T = %d day has to be approximately %d km above the Earth\'s surface.'%(1,height(1*24*60**2)))
print('The satellite with T = %d minutes has to be approximately %d km above the Earth\'s surface.'%(90,height(90*60)))
print('The satellite with T = %d minutes has to be approximately %d km above the Earth\'s surface.'%(45,height(45*60)))
print('Faster satellites are at lower heights.')
print('-----------------------------------------------------------')    
h = height(float(input('Enter the desired revolution time period of satellite in seconds: ')))
print('The satellite has to be approximately %d km above the Earth\'s surface.'%h)

del_h = height(24*60**2)-height(23.93*60**2)
print('Difference in heights of satellites from Earth\'s surface with time period T = 24 hrs and T = 23.93 hrs (sidereal day) is %d km'%del_h)
