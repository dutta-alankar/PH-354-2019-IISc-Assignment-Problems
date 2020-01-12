#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 12:02:37 2019

@author: alankar
"""

import numpy as np

np.random.seed(500)
dice1 = np.random.randint(low=1,high=6)
dice2 = np.random.randint(low=1,high=6)

print('Dice 1: %d'%dice1)
print('Dice 2: %d'%dice2)

N = int(1.e6)

dice1 = np.random.randint(low=1,high=7,size=N)
dice2 = np.random.randint(low=1,high=7,size=N)

counter = 0
for i in range(N):
    if(dice1[i]==6 and dice2[i]==6): counter+=1

print('Probability of getting a double six: %f'%(counter/N))

"""
Output:
    
Dice 1: 3
Dice 2: 2
Probability of getting a double six: 0.027814
"""