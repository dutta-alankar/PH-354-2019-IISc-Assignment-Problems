# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 05:02:30 2018

@author: Alankar
"""

import numpy as np

def Eobs(v,d):
    t = d/v #yr
    return t

def Robs(v,d):
    Gamma = 1/np.sqrt(1-v**2)
    t = d/(Gamma*v)
    return t

print('-----------------------------------------------------------')
print('Demo Output:')
print('Distance between Earth and the planet of interest is 10 light yrs')
print('Spaceship is heading towards the planet with a fixed velocity of 0.99c')
print('\nTime taken by the spaceship noted by an observor on Earth to reach the planet is %.2f yrs.'%Eobs(0.99,10))
print('Time taken by the spaceship noted by an observor on spaceship to reach the planet is %.2f yrs.'%Robs(0.99,10))  
print('-----------------------------------------------------------')

dist = float(input('Enter distance between Earth and the planet of interest in light yrs: '))
vel = float(input('Enter spaceship velocity as a fraction of light speed c in vacuum: '))
print('\nTime taken by the spaceship noted by an observor on Earth to reach the planet is %.2f yrs.'%Eobs(vel,dist))
print('Time taken by the spaceship noted by an observor on spaceship to reach the planet is %.2f yrs.'%Robs(vel,dist))
