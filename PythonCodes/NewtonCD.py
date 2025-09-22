""" From "COMPUTATIONAL PHYSICS", 3rd Ed, Enlarged Python eTextBook  
    by RH Landau, MJ Paez, and CC Bordeianu
    Copyright Wiley-VCH Verlag GmbH & Co. KGaA, Berlin;  Copyright R Landau,
    Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2015.
    Support by National Science Foundation"""

# NewtonCD.py    Newton Search with central difference

from sys import version
if int(version[0])>2:   # raw_input deprecated in Python 3
    raw_input=input   
from math import cos

x = 4.;         dx = 3.e-1;        eps = 0.2;                # Parameters
imax = 100;                                        # Max no of iterations
def f(x):                                                  # function def
    return 2*cos(x) - x

for it in range(0, imax + 1):
    F = f(x)
    if ( abs(F) <= eps ):                         # Check for convergence
        print("Root found, tolerance eps = " , eps) 
        break
    print("Iteration # = ", it, " x = ", x, " f(x) = ", F)
    df = ( f(x + dx/2)  -  f(x - dx/2) )/dx          # Central diff deriv
    dx = - F/df 
    x   += dx                                                 # New guess
print("Enter and return any character to quit")
s = raw_input()
