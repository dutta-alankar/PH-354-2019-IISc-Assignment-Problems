#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 16:48:41 2019

@author: alankar
"""
import numpy as np
import matplotlib.pyplot as plt

def quad_solve1(a,b,c):
    D = b**2-4*a*c
    return np.array([(-b+np.sqrt(D))/(2*a),(-b-np.sqrt(D))/(2*a)])

def quad_solve2(a,b,c):
    D = b**2-4*a*c
    return np.array([(2*c)/(-b-np.sqrt(D)),(2*c)/(-b+np.sqrt(D))])

print('Using form 1:')
print('Roots are:',end=' ')
print(quad_solve1(.001, 1000, .001))
print('Using form 2:')
print('Roots are:',end=' ')
print(quad_solve2(.001, 1000, .001))

"""
The two functions differ in their results. This happens when $b^2>>|4ac|$. In either of the two
formulae, finding one of the roots involve subtracting two nearly equal quantities (Discriminant is almost $b^2$).
This results in loss of numerical precision corresponding to that root. So in one formula if Root 1 is more accurate
than Root 2, then in the other formula, Root2 is more accurate than Root 1. Now the question is which root is more accurate
in which formula?
Well that depends on the sign of $b$ in $ax^2+bx+c=0$
When $b>0$, $-b-\sqrt{b^2-4ac}$ doesn't involve subtracting two nearly equal quantities. So Root 2 of quad_solve1 and
Root 1 of quad_solve2 gives accurate results.
Converse happens for $b<0$

Lets code this in the following function:
"""

def quad_solve_acc(a,b,c):
    if b>0:
        return np.array([quad_solve2(a,b,c)[0],quad_solve1(a,b,c)[1]])
    else:
        return np.array([quad_solve1(a,b,c)[10],quad_solve2(a,b,c)[1]])
    
print('Accurate Roots are:',end=' ')
print(quad_solve_acc(.001, 1000, .001))

x = -np.linspace(0,14,100)*1e-7
plt.plot(x,0.001*x**2+1000*x+0.001)
plt.grid()
plt.show()