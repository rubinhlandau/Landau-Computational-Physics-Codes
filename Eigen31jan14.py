""" From "COMPUTATIONAL PHYSICS", 3rd Ed, Enlarged Python eTextBook  
    by RH Landau, MJ Paez, and CC Bordeianu
    Copyright Wiley-VCH Verlag GmbH & Co. KGaA, Berlin;  Copyright R Landau,
    Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2015.
    Support by National Science Foundation"""

# Eigen.py  Solution of matrix eigenvalue problem

from numpy import*
from numpy.linalg import eig

A = array( [[2./3,-1./4,-1./4], [-1./4,2./3,-1./4], [-1./4,-1./4,2./3]] )
print('I =\n', A)

Es, evectors = eig(A)                         # Solves eigenvalue problem
print('Eigenvalues =  ', Es, '\n Matrix of Eigenvectors =\n', evectors) 
Vec = array([ evectors[0, 0], evectors[1, 0], evectors[2, 0] ] )
print('A single eigenvector  =', Vec)
LHS = dot(A, Vec)
RHS = Es[0]*Vec 
print('LHS - RHS =', LHS-RHS) 
