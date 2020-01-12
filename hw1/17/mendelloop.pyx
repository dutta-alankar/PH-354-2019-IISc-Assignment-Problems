# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 18:08:18 2018

@author: Alankar
"""

import numpy as np
import mendelcheck as mc

cpdef mloop(x,y,int turns):
    #cpdef double xx
    #cpdef double yy
    prof = np.zeros((len(x),len(y)),dtype=np.float32)
    mendel, nomendel = [], []
    cpdef int i = 0
    cpdef int j = 0
    for i in range(0,len(x)):
        for j in range(0,len(y)):
            c = np.complex(x[i],y[j])
            if mc.isMendel(c,turns): mendel.append(c)
            else: nomendel.append(c)
            prof[i,j] = mc.isMendel_iter(c,turns)
            #j+=1
        #i+=1
        
    mendel = np.array(mendel)
    nomendel = np.array(nomendel)
    return(mendel,nomendel,prof)