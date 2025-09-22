""" From "COMPUTATIONAL PHYSICS", 3rd Ed, Enlarged Python eTextBook  
    by RH Landau, MJ Paez, and CC Bordeianu
    Copyright Wiley-VCH Verlag GmbH & Co. KGaA, Berlin;  Copyright R Landau,
    Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2015.
    Support by National Science Foundation"""
 # Matrix.py Matrix ,ultiplication using visual arrays
 
from visual import *                   # Load Visual package

vector1 = array([1, 2, 3, 4, 5])       # Fill 1-D array
print('vector1 =',vector1)             # Print entire array object
vector2 = vector1 + vector1            # Add 2 vectors
print('vector2=',vector2)              # Print vector2
vector2 = 3 * vector1                  # Mult array by scalar
print ('3 * vector1 = ', vector2)      # Print vector
matrix1 = array(([0,1],[1,3]))         # An array of arrays
print(matrix1)                         # Print matrix1
print ('vector1.shape= ',vector1.shape)
print  (matrix1 * matrix1)             # Matrix multiply
