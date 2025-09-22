""" Author: Oscar Restrepo, From "COMPUTATIONAL PHYSICS", 3rd Ed, Enlarged Python  
   eTextBook by RH Landau, MJ Paez, and CC Bordeianu. 
    Copyright Wiley-VCH Verlag GmbH & Co. KGaA, Berlin;  Copyright R Landau,
    Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2015.
    Support by National Science Foundation"""

import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from pylab import *

M = 4                                # Initial points for plot Four
T = 2.                                           # Function period 

numwaves =  2
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.15, bottom=0.25) # margins left and botm
t = np.arange(0.0, pi, 0.01)              # Range with 314 elements
t1 = np.arange(0.0,T/2,0.01)              # First part 100 elements
t2 = t[100:300]                              # 2nd part of Sawtooth 
f1 = t1                                # Linear function start at 0
f2 = t2-T                                 # Linear func start at -1
s = 0 
plot(t1,f1)                                #  0<=t<= T/2, f=t/(T/2)
plot(t2,f2,color='b')        # In blue, t/2 <=t <= pi,f=(t-T)/(T/2)    

def Four(M,T,t):# M: number of sine waves, T: period, t:time
    sumy = 0                                           # Start sum
    om = 2.*pi/T                                    # Omega = 2pi/T
    fac = 1                                    # To alternate signs
    for m in range(1,M):         # M variable selected with slider
        sumy += fac* sin(m*om*t)           # Summing Fourier Terms
        fac = -fac                       # Multiply by -1 previous
    sumy = (2.0/pi)*sumy                           # Common factor
    return sumy

s = Four(M,T,t)                                    # Unitial plot   
l, = plt.plot(t,s, lw=1, color='red')
plt.axis([0, pi, -4.0, 4.0]) #minx, maxx, miny, maxy

xlabel('Time')                                       # x axis name
ylabel('Signal')                                     # y axis name
title('Fourier Synthesis of Sawtooth function')
grid(True)              # Show grid- vertical and horizontal lines

# Slider
axcolor = 'w'                         # White backgnd color slider 
axnumwaves = plt.axes([0.15, 0.1, 0.75, 0.03], axisbg=axcolor) 
snumwaves = Slider(axnumwaves, '# Waves', 1, 20, valinit=T)
# Previous: value of the slider (float) assigned to snumwaves

def hzfunc():    # call Fourier sums and plot
    hzdict = Four(int(numwaves),T,t)
    ydata = hzdict
    l.set_ydata(ydata)
    plt.draw()

hzfunc()

def update(val):              # Update as slider selects new values
    global  numwaves                        # Num sin waves summed
    numwaves =int( snumwaves.val)                # Make it integer
    l.set_ydata(Four(numwaves,T,t))      # Call for changing nwaves
    fig.canvas.draw_idle()
snumwaves.on_changed(update)

plt.show()
