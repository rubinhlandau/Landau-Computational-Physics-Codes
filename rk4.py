""" From "COMPUTATIONAL PHYSICS", 3rd Ed, Enlarged Python eTextBook  
    by RH Landau, MJ Paez, and CC Bordeianu
    Copyright Wiley-VCH Verlag GmbH & Co. KGaA, Berlin;  Copyright R Landau,
    Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2015.
    Support by National Science Foundation"""

# rk4.py 4th order Runge Kutta soltn of ODE
from visual import *
from visual.graph import *

#   Initialization
a = 0.;                       b = 10.;                   n = 100                                          
ydumb = zeros((2),float);y = zeros((2),float); fReturn = zeros((2),float)
y[0] = 3. ;  y[1] = -5.;  t = a;   h = (b-a)/n; 

def f( t, y, fReturn ):                    # function returns RHS, change
    fReturn[0] = y[1]                                         # 1st deriv
    fReturn[1] = -9*y[0]-2*y[1] + 9*sin(3.*t) # 2nd spring, friction, ext

def rk4Function(h, fReturn):               # Func for rk4; do not disturb
    k1 = zeros((2),float); k2 = zeros((2),float);  k3 = zeros((2),float);
    k4 = zeros((2), float)
    k1[0] = h*fReturn[0];  k1[1] = h*fReturn[1]        # Compute function
    for i in range(0, 2): ydumb[i] = y[i] + k1[i]/2. 
    f(t + h/2., ydumb, fReturn) 
    k2[0] = h*fReturn[0];  k2[1] = h*fReturn[1] 
    for i in range(0, 2):  ydumb[i] = y[i] + k2[i]/2. 
    f(t + h/2., ydumb, fReturn)
    k3[0] = h*fReturn[0];  k3[1] = h*fReturn[1] 
    for i in range(0, 2): ydumb[i] = y[i] + k3[i] 
    f(t + h, ydumb, fReturn) 
    k4[0] = h*fReturn[0];   k4[1] = h*fReturn[1]  
    for i in range(0, 2): y[i] = y[i] + (k1[i]+2.*(k2[i]+k3[i])+k4[i])/6.
    
graph1 = gdisplay(x=0,y=0, width = 400, height = 400, title = 'RK4', 
             xtitle = 't', ytitle = 'Y[0]',xmin=0,xmax=10,ymin=-2,ymax=3)
funct1 = gcurve(color = color.blue)
graph2 = gdisplay(x=400,y=0, width = 400, height = 400, title = 'RK4', 
           xtitle = 't', ytitle = 'Y[1]',xmin=0,xmax=10,ymin=-25,ymax=18)
funct2 = gcurve(color = color.red)
funct1.plot(pos = (t, y[0]) )
funct2.plot(pos = (t, y[1]) )
while (t < b):                                                # Time loop
    if ( (t + h) > b ): h = b - t                             # Last step
    f(t, y, fReturn)                  # Evaluate RHS's, return in fReturn
    rk4Function(h, fReturn)
    t = t + h
    rate(30)
    funct1.plot(pos = (t, y[0]))
    funct2.plot(pos = (t, y[1]))                         # End while loop
