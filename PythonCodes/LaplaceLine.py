""" From "COMPUTATIONAL PHYSICS", 3rd Ed, Enlarged Python eTextBook  
    by RH Landau, MJ Paez, and CC Bordeianu
    Copyright Wiley-VCH Verlag GmbH & Co. KGaA, Berlin;  Copyright R Landau,
    Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2015.
    Support by National Science Foundation"""
   
# LaplaceLine.py:  Solve Laplace's eqtn, 3D matplot, close shell to quit


import matplotlib.pylab as p;
from mpl_toolkits.mplot3d import Axes3D
from numpy import *;
import numpy;
print("Initializing")
Nmax = 100; Niter = 70; V = zeros((Nmax, Nmax), float)            # float maybe Float

print "Working hard, wait for the figure while I count to 60"
for k in range(0, Nmax-1):  V[k,0] = 100.0                             # line at 100V
    
for iter in range(Niter):                                 # iterations over algorithm
    if iter%10 == 0: print iter
    for i in range(1, Nmax-2):                                                
        for j in range(1,Nmax-2): V[i,j] = 0.25*(V[i+1,j]+V[i-1,j]+V[i,j+1]+V[i,j-1])  
x = range(0, Nmax-1, 2);  y = range(0, 50, 2)                # plot every other point                        
X, Y = p.meshgrid(x,y)                 

def functz(V):                                             # Function returns V(x, y)
    z = V[X,Y]                        
    return z

Z = functz(V)                          
fig = p.figure()                                                      # Create figure
ax = Axes3D(fig)                                                       # plot axes
ax.plot_wireframe(X, Y, Z, color = 'r')                               # red wireframe
ax.set_xlabel('X')                                                       # label axes
ax.set_ylabel('Y')
ax.set_zlabel('Potential')
p.show()                                           # display fig, close shell to quit
