# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 10:22:11 2018

@author: Alankar
"""

import numpy as np
 
def factorial(n):
    if (n==1 or n==0): return 1
    else:
        return n*factorial(n-1)

n = int(input('Enter a positive integer:'))
print('%d! = %d'%(n,factorial(n)))
