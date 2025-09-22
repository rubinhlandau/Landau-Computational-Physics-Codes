""" From "COMPUTATIONAL PHYSICS", 3rd Ed, Enlarged Python eTextBook  
    by RH Landau, MJ Paez, and CC Bordeianu
    Copyright Wiley-VCH Verlag GmbH & Co. KGaA, Berlin;  Copyright R Landau,
    Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2015.
    Support by National Science Foundation"""
	 
# Bugs.py creates bifurcation diagram for Logistic Map

from visual.graph import *

m_min = 1.0;    m_max = 4.0;     step = 0.25
graph1 = gdisplay(width=600, height=400, title='Logistic map',xtitle = 'm', 
                  ytitle='x', xmax=4., xmin=1., ymax=1., ymin=0.)
pts = gdots(shape = 'square', size = 1, color = color.green)
lasty = int(1000 * 0.5)                  # to eliminate later some points
count = 0                            # to plot later every two iterations
for m in arange(m_min, m_max, step):
    y = 0.5
    for i in range(1,201,1):                        # to avoid transients
        y = m*y*(1-y)   
    for i in range(201,402,1):
        y = m*y*( 1 - y) 
    for i in range(201, 402, 1):                    # to avoid transients
        y = m*y*(1 - y)   
        inty = int(1000 * y)
        if inty != lasty and count%2 == 0:  pts.plot(pos=(m,y)) # no repeats
        lasty = inty
        count += 1

