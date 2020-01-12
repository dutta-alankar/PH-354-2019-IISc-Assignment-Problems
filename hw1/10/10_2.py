# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 20:43:40 2018

@author: Alankar
"""
import numpy as np

def binomial(n,k):
    if k==0: return 1
    return int(np.math.factorial(n)/(np.math.factorial(k)*np.math.factorial(n-k)))

print('An unbaised coin is tossed 100 times')
print('Probability of 60 heads turning up is %.3f'%(binomial(100,60)/2**100))
P = 0
for i in range(60,101):
    P += binomial(100,i)
P /= 2**100
print('Probability of 60 or more heads turning up is %.3f'%P)
