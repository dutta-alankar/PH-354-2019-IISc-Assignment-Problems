# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 16:50:22 2018

@author: Alankar
"""

import numpy as np
import matplotlib.pyplot as plt
import mendelloop as ml

gridlength = 10000
x = np.linspace(-2,2,gridlength)
y = np.linspace(-2,2,gridlength)

iterations = 100

mendel,nomendel,prof = ml.mloop(x,y,iterations)
x, y = np.mgrid[slice(-2,2+x[1]-x[0],x[1]-x[0]),slice(-2,2+y[1]-y[0],y[1]-y[0])]
plt.scatter(mendel.real,mendel.imag,color='black',s=0.5)
plt.savefig('mbrot_BW.jpg')
#plt.show()
#plt.pcolor(x,y,np.log10(prof.T),cmap='jet')
#plt.savefig('mbrot_colored_logged.jpg')
#plt.show()
plt.pcolor(x,y,prof.T,cmap='jet',vmin=np.min(prof),vmax=np.max(prof))
plt.axis([-2,2,-2,2])
plt.savefig('mbrot_colored.jpg')
#plt.show()