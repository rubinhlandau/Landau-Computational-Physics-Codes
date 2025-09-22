""" From "COMPUTATIONAL PHYSICS", 3rd Ed, Enlarged Python eTextBook  
    by RH Landau, MJ Paez, and CC Bordeianu
    Copyright Wiley-VCH Verlag GmbH & Co. KGaA, Berlin;  Copyright R Landau,
    Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2015.
    Support by National Science Foundation"""
    
# Trapz.py      trapezoid rule N point integration of f(x) from A->B

from numpy import *   

def f(x):
    return x*x

def trapezoid(A,B,N):
    h = (B - A)/(N - 1)                    # step, N-1 intervals
    sum = (f(A) + f(B))/2.         # initialization, (1st + last)/2
    for i in range(1, N-1):             # 1st, last not included
       sum += f(A+i*h)                   # excluding 1st and last
    return h*sum                          # multiply result by h

A = 0.; B = 3.; N = 1200
print( trapezoid(A, B, N) )