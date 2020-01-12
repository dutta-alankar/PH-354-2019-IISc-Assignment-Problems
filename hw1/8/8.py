# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 14:41:30 2018

@author: Alankar
"""

import madelung as md
L = 100
M = md.Madelung_compute(L)
print('Madelung Constant: %.3f'%M)
#output: Madelung Constant: -1.742
