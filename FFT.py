""" From "COMPUTATIONAL PHYSICS", 3rd Ed, Enlarged Python eTextBook  
    by RH Landau, MJ Paez, and CC Bordeianu
    Copyright Wiley-VCH Verlag GmbH & Co. KGaA, Berlin;  Copyright R Landau,
    Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2015.
    Support by National Science Foundation"""

# FFT.py:  FFT for complex numbers in dtr[][2], returned in dtr

from numpy import *
from sys import version
if int(version[0]) > 2:                # raw_input deprecated in Python 3
    raw_input=input  
max = 2100                 
points = 1026                                          # Can be increased
data = zeros((max), float) 
dtr  = zeros((points,2), float)
  
def fft(nn,isign):                                      # FFT of dtr[n,2]
    n = 2*nn
    for i in range(0,nn+1):                # Original data in dtr to data
         j = 2*i+1
         data[j] = dtr[i,0]                       # Real dtr, odd data[j]
         data[j+1] = dtr[i,1]                  # Imag dtr, even data[j+1]
    j = 1                               # Place data in bit reverse order
    for i in range(1,n+2, 2):
        if (i-j) < 0 :                # Reorder equivalent to bit reverse
            tempr = data[j]
            tempi = data[j+1]
            data[j] = data[i]
            data[j+1] = data[i+1]
            data[i] = tempr
            data[i+1] = tempi 
        m = n/2;
        while (m-2 > 0): 
            if  (j-m) <= 0 :
                break
            j = j-m
            m = m/2
        j = j+m;
                               
    print(" Bit-reversed data ")
  
    for i in range(1, n+1, 2):
        print("%2d  data[%2d]  %9.5f "%(i,i,data[i]))    # To see reorder
    mmax = 2
    while (mmax-n) < 0 :                                # Begin transform
       istep = 2*mmax
       theta = 6.2831853/(1.0*isign*mmax)
       sinth = math.sin(theta/2.0)
       wstpr = -2.0*sinth**2
       wstpi = math.sin(theta)
       wr = 1.0
       wi = 0.0
       for m in range(1,mmax +1,2):  
           for i in range(m,n+1,istep):
               j = i+mmax
               tempr = wr*data[j]   -wi *data[j+1]
               tempi = wr*data[j+1] +wi *data[j]
               data[j]   = data[i]   -tempr
               data[j+1] = data[i+1] -tempi
               data[i]   = data[i]   +tempr
               data[i+1] = data[i+1] +tempi        
           tempr = wr
           wr = wr*wstpr - wi*wstpi + wr
           wi = wi*wstpr + tempr*wstpi + wi;
       mmax = istep              
    for i in range(0,nn):
        j = 2*i+1
        dtr[i,0] = data[j]
        dtr[i,1] = data[j+1] 
nn = 16                                                      # Power of 2
isign = -1                           # -1 transform, +1 inverse transform
print('        INPUT')
print("  i   Re part   Im  part")
for i in range(0,nn ):                                       # Form array
    dtr[i,0] = 1.0*i                                          # Real part
    dtr[i,1] = 1.0*i                                            # Im part
    print(" %2d %9.5f %9.5f" %(i,dtr[i,0],dtr[i,1]))
fft(nn, isign)                             # Call FFT, use global dtr[][]
print('    Fourier transform')
print("  i      Re      Im    ")
for i in range(0,nn):  
    print(" %2d  %9.5f  %9.5f "%(i,dtr[i,0],dtr[i,1]))
print("Enter and return any character to quit")
s = raw_input()
