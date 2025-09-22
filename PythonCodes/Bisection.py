""" From "COMPUTATIONAL PHYSICS", 3rd Ed, Enlarged Python eTextBook  
    by RH Landau, MJ Paez, and CC Bordeianu
    Copyright Wiley-VCH Verlag GmbH & Co. KGaA, Berlin;  Copyright R Landau,
    Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2015.
    Support by National Science Foundation"""

# Bisection.py                     Find zero via Bisection algorithm

from visual import *
from visual.graph import *

def f(x):                                           # Function = 0?
    return 2*cos(x) - x

def bisection(xminus, xplus, Nmax, eps):     # x+, x-, Nmax, error
   for it in range(0, Nmax):
       x = ( xplus  +  xminus )/2.                     # Mid point
       print(" it ", it, " x  ", x, " f(x) ", f(x))
       if ( f(xplus)*f(x) > 0. ):             # Root in other half
          xplus = x                               # Change x+ to x
       else:
          xminus =  x                             # Change x- to x
       if ( abs(f(x) ) < eps ):                       # Converged?
          print("\nRoot found with precision eps = ", eps)
          break
       if it == Nmax-1:
           print ("\n root not found after Nmax iterations\n")
   return x

eps = 1e-6                                    # Precision of zero
a = 0.0; b = 7.0                                  # Root in [a,b]
imax = 100                                   # Max no. iterations
root = bisection(a ,b, imax, eps)
print("Root =", root)
