# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 03:22:11 2018

@author: Alankar
"""

import numpy as np

primes = [2]


for n in range(3,10001):
    nonprime = False
    limit = np.ceil(np.sqrt(n))
    for factor in primes:
        if (n%factor==0): 
            nonprime = True
            break
        elif(factor>limit):
            break
    if not(nonprime): primes.append(n)
primes = np.array(primes)
for nums in primes:
    print(nums)
            
