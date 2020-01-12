# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 17:40:53 2018

@author: Alankar
"""
import numpy as np

def timeit(h,g=9.8):
    return np.sqrt(2*h/g)
    
print('-----------------------------------------------------------')
print('Demo Output: \nA ball takes approximately %.2f seconds to reach the bottom of the tower of height %d metres under free fall.' %(timeit(100),100))  
print('-----------------------------------------------------------')

t = timeit(float(input('Enter height of the tower in metres: ')))
print('A ball takes approximately %.2f seconds to reach the bottom of the tower under free fall.'%t)
