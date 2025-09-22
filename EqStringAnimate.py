""" From "COMPUTATIONAL PHYSICS", 3rd Ed, Enlarged Python eTextBook  
    by RH Landau, MJ Paez, and CC Bordeianu
    Copyright Wiley-VCH Verlag GmbH & Co. KGaA, Berlin;  Copyright R Landau,
    Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2015.
    Support by National Science Foundation"""
	 
# EqString.py:  Animated leapfrog solution of wave equation

from visual import *

# Set up curve
g = display(width = 600, height = 300, title = 'Vibrating string')
vibst = curve(x = list(range(0, 100)), color = color.yellow)
ball1 = sphere(pos = (100, 0), color = color.red, radius = 2)
ball2 = sphere(pos = ( - 100, 0), color = color.red, radius = 2)
ball1.pos
ball2.pos
vibst.radius = 1.0

# Parameters
rho   = 0.01                                             # string density
ten   = 40.                                              # string tension
c     = sqrt(ten/rho)                                 # Propagation speed
c1    = c                                                 # CFL criterium
ratio =  c*c/(c1*c1)

# Initialization
xi = zeros((101,3), float)                             # 101 x's & 3 t's 
for i in range(0, 81):     xi[i, 0] = 0.00125*i;                     # IC
for i in range (81, 101):  xi[i, 0] = 0.1 - 0.005*(i - 80)           # IC
for i in range(0, 100):                                      # 1st t step
    vibst.x[i] = 2.0*i - 100.0                           # assign,scale x
    vibst.y[i] = 300.*xi[i, 0]                          # assign, scale y
vibst.pos                                                   # draw string

# Later time steps
for i in range(1, 100): xi[i,1] = xi[i,0] + 0.5*ratio*(xi[i+1,0]+xi[i-1,0]-2*xi[i,0])
while 1:                              # continue plotting till user quits
    rate(50)                         # delays plotting, (bigger = slower)
    for i in range(1, 100):              
        xi[i,2] = 2.*xi[i,1] - xi[i,0] + ratio * (xi[i+1,1]+xi[i-1,1]-2*xi[i, 1])
    for i in range(1, 100):
         vibst.x[i] = 2.*i - 100.0                             # scaled x
         vibst.y[i] = 300.*xi[i, 2]                            # scaled y
    vibst.pos                                               # plot string
    for i in range(0, 101):
        xi[i, 0] = xi[i, 1]                               # recycle array
        xi[i, 1] = xi[i, 2]                      

print("Done!")
