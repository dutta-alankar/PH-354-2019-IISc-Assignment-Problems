#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 12:23:24 2019

@author: alankar
"""

import numpy as np
from scipy.linalg import eigh_tridiagonal


def lanczos(A,N):
    A = np.array(A,dtype=np.float64)
    R,C = A.shape
    if (R!=C): 
        print('Square Matrix is required!')
        return None
    if (N>R): N = R
    beta = 0
    np.random.seed(100)    
    b = np.ones((R,1))
    qold = np.zeros((R,1))
    qnew = b/np.linalg.norm(b)
    Q = np.zeros((R,N))
    #T = np.zeros((R,N))
    Q[:,0] = qnew[:,0]
    for i in range(1,N):
        v = np.matmul(A,qnew)
        alpha = np.dot(qnew.T,v)[0,0]
        v = v - beta*qold - alpha*qnew
        beta = np.linalg.norm(v)
        qold = np.copy(qnew)
        qnew = v/beta
        Q[:,i] = qnew[:,0]
        #T[i,i] = alpha
        #if (i+1<N): 
        #    Q[:,i+1] = qnew[:,0]
        #    T[i+1,i] = beta
        #    T[i,i+1] = beta
    T = np.matmul(Q.T,np.matmul(A,Q))
    for i in range(0,T.shape[0]):
        for j in range(0,T.shape[1]):
            if not(i==j or i==j+1 or i==j-1): T[i,j]=0.
    return (Q,T)
    
np.random.seed(10)   
size = 20 
B = 2*np.diag(np.full(size,1.0))+np.random.rand(size, 20)/np.sqrt(size)
A = (B+B.T)/2

eigval, eigvec = np.linalg.eig(A)
file = open('eigen_inbuilt.txt','w')
for i in range(0,eigval.shape[0]):
    file.write('Eigenvalue: %.5f\n'%eigval[i])
    file.write('Eigenvector: \n')
    file.close()
    append = open('eigen_inbuilt.txt','a')
    np.savetxt(append,eigvec[:,i])
    append.close()
    file = open('eigen_inbuilt.txt','a')
    file.write('\n\n')
file.close()

Q,T = lanczos(A,size)
eigval_l, eigvec_l = eigh_tridiagonal([T[i,i] for i in range(T.shape[0])],[T[i,i+1] for i in range(T.shape[0]-1)])
eigvec_l = np.matmul(Q,eigvec_l)
#check = np.dot(Q.T,Q)
#check2 = np.dot(Q.T,np.matmul(A,Q))

file = open('eigen_lanczos.txt','w')
for i in range(0,eigval_l.shape[0]):
    file.write('Eigenvalue: %.5f\n'%eigval_l[i])
    file.write('Eigenvector: \n')
    file.close()
    append = open('eigen_lanczos.txt','a')
    np.savetxt(append,eigvec_l[:,i])
    append.close()
    file = open('eigen_lanczos.txt','a')
    file.write('\n\n')
file.close()
