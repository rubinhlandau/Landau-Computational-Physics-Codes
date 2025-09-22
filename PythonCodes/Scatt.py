""" From "COMPUTATIONAL PHYSICS", 3rd Ed, Enlarged Python eTextBook  
    by RH Landau, MJ Paez, and CC Bordeianu
    Copyright Wiley-VCH Verlag GmbH & Co. KGaA, Berlin;  Copyright R Landau,
    Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2015.
    Support by National Science Foundation"""

# Scatt.py:  Soln of Lippmann Schwinger in p space for scattering
from visual import *
from visual.graph import *
from gauss import gauss                      # gauss.pyc for gauss method
import numpy.linalg as lina          # Numpy's LinearAlgebra will be lina

graphscatt = gdisplay(x=0, y=0, xmin=0, xmax=6,ymin=0, ymax=1, width=600, height=400,
title='S wave cross section vs E', xtitle='kb', ytitle='[sin(delta)]**2')
sin2plot = gcurve(color=color.yellow)       

M = 27;             b = 10.0;           n = 26
k = zeros((M),float);        x = zeros((M),float);   w = zeros((M),float)
Finv = zeros((M,M),float);  F = zeros((M,M), float); D = zeros((M),float)
V = zeros((M), float);       Vvec = zeros((n+1,1),float)
scale = n/2;                 lambd = 1.5
gauss(n, 2, 0., scale, k, w)                        # Set up points & wts
ko = 0.02

for m in range(1,901):	
    k[n] = ko		
    for i in range (0, n):  D[i]=2/pi*w[i]*k[i]*k[i]/(k[i]*k[i]-ko*ko) #D
    D[n] = 0. 
    for  j in range(0,n):   D[n]=D[n]+w[j]*ko*ko/(k[j]*k[j]-ko*ko)
    D[n] = D[n]*(-2./pi)    
    for i in range(0,n+1):                 # Set up F matrix and V vector
        for j in range(0,n+1):
            pot = -b*b * lambd * sin(b*k[i])*sin(b*k[j])/(k[i]*b*k[j]*b)
            F[i][j] = pot*D[j]	                                 # Form F
            if i==j: F[i][j] = F[i][j] + 1. 
        V[i] = pot                                             # Define V
    for  i in range(0,n+1):  Vvec[i][0]= V[i]   
    Finv = lina.inv(F)                    # Use LinearAlgebra fir inverse
    R = dot(Finv, Vvec)                                 # Matrix multiply
    RN1 = R[n][0]
    shift = atan(-RN1*ko)
    sin2 = (sin(shift))**2
    sin2plot.plot(pos = (ko*b,sin2))                 # Plot sin**2(delta)
    ko = ko + 0.2*pi/1000.
print("Done")
