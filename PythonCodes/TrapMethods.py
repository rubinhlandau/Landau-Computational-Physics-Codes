""" From "COMPUTATIONAL PHYSICS", 3rd Ed, Enlarged Python eTextBook  
    by RH Landau, MJ Paez, and CC Bordeianu
    Copyright Wiley-VCH Verlag GmbH & Co. KGaA, Berlin;  Copyright R Landau,
    Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2015.
    Support by National Science Foundation"""

# TrapMethods      Trapezoid integration of function

from numpy import *
from sys import version

if int(version[0])>2:  raw_input=input  # raw_input deprecated in Python3
A = 0.0; 	B = 3.0;     N = 4

def f(y):                                     # function being integrated
    print(" y  f(y)  = ", y, y*y)
    return y*y

def wTrap(i, h):                                      # determines weight
    if ( (i == 1) or (i == N) ):   wLocal = h/2.0
    else: wLocal = h
    return wLocal

h = (B - A)/(N - 1)
suma = 0.0

for i in range(1, N + 1):
    t = A + (i - 1)*h
    w = wTrap(i, h)
    suma  = suma + w * f(t)
    
print(' Total sum = ', suma)
print("Enter and return any character to quit")
s = raw_input()
