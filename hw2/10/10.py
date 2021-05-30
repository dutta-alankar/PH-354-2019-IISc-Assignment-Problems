#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 00:38:06 2019

@author: alankar
"""
import numpy as np

Vp = 5 #V
#kohm resistances, mA currents
R1 = 1
R2 = 4
R3 = 3
R4 = 2
I0 = 3e-6 #3nA
VT = 0.05 #diode emission/ideality factor=1.93 (VT=0.0259V)

def func(I):
    I1, I2, I3, I4 = I[0], I[1], I[2], I[3]
    equations = []
    ID = I0*np.exp(-(I1*R1-I3*R3)/VT)
    equations.append( Vp - I1*R1 - I2*R2)
    equations.append( Vp - I3*R3 - I4*R4)
    equations.append( I1 - ID - I2 )
    equations.append( I3 + ID - I4 )
    return np.array(equations).T

def jac(I):
    I1, I2, I3, I4 = I[0], I[1], I[2], I[3]
    g = 1+I0*R1/VT*np.exp((I3*R3-I1*R1)/VT)
    h = -I0*R3/VT*np.exp((I3*R3-I1*R1)/VT)
    m = 1-g
    d = 1-h
    J = np.array( [
                  [-R1,    -R2,     0.,      0.],
                  [ 0.,     0.,    -R3,     -R4],
                  [ g,     -1.,     h,       0.],
                  [ m,      0.,     d,      -1.] ])
    return J

tol = 1e-10

I_new = np.array([1.,1.,1.,1.])
I_old = np.array([0.,0.,0.,0.])
 
while( np.abs(I_old[0]-I_new[0])>tol or np.abs(I_old[1]-I_new[1])>tol or np.abs(I_old[2]-I_new[2])>tol or np.abs(I_old[3]-I_new[3])>tol):
    I_old = I_new
    equations = func(I_old)
    delI = np.linalg.solve(jac(I_old),-equations)
    I_new = I_old + delI.T

for i in range(len(I_new)):
    print("I%d = %.3f mA"%(i+1,I_new[i]))
ID = I0*np.exp(-(I_new[0]*R1-I_new[2]*R3)/VT)
print("ID = %.3f mA"%ID)
print("Voltage across diode (FB) = %.2f V"%(-(I_new[0]*R1-I_new[2]*R3)))

"""
I1 = 1.553 mA
I2 = 0.862 mA
I3 = 0.723 mA
I4 = 1.415 mA
ID = 0.691 mA
Voltage across diode (FB) = 0.62 V
"""
