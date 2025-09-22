""" From "COMPUTATIONAL PHYSICS", 3rd Ed, Enlarged Python eTextBook  
    by RH Landau, MJ Paez, and CC Bordeianu
    Copyright Wiley-VCH Verlag GmbH & Co. KGaA, Berlin;  Copyright R Landau,
    Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2015.
    Support by National Science Foundation"""

# FDTD.py  FDTD solution of Maxwell's equations in 1-D

from visual import *
xmax=201
ymax=100
zmax=100
scene = display(x=0,y=0,width= 800, height= 500, \
               title= 'E: cyan, H: red. Periodic BC',forward=(-0.6,-0.5,-1))
Efield = curve(x=list(range(0,xmax)),color=color.cyan,radius=1.5,display=scene)
Hfield = curve(x=list(range(0,xmax)),color=color.red, radius=1.5,display=scene)
vplane= curve(pos=[(-xmax,ymax),(xmax,ymax),(xmax,-ymax),(-xmax,-ymax),
                   (-xmax,ymax)],color=color.cyan)
zaxis=curve(pos=[(-xmax,0),(xmax,0)],color=color.magenta)
hplane=curve(pos=[(-xmax,0,zmax),(xmax,0,zmax),(xmax,0,-zmax),(-xmax,0,-zmax),
                   (-xmax,0,zmax)],color=color.magenta)
ball1 = sphere(pos = (xmax+30, 0,0), color = color.black, radius = 2)
ts = 2                          # for old and new time
beta = 0.01
Ex = zeros((xmax,ts),float)      # init E, 201 points, ts=0 old, ts=1 new
Hy = zeros((xmax,ts),float)      # init H, 201 points, ts=0 old, ts=1 new
Exlabel1 = label( text = 'Ex', pos = (-xmax-10, 50), box = 0 )
Exlabel2 = label( text = 'Ex', pos = (xmax+10, 50), box = 0 )
Hylabel  = label( text = 'Hy', pos = (-xmax-10, 0,50), box = 0 )
zlabel   = label( text = 'Z',  pos = (xmax+10, 0), box = 0 )  # shift fig
ti=0                               # t=0: initial position, t=1 next time

def inifields():
    k = arange(xmax)
    Ex[:xmax,0] = 0.1*sin(2*pi*k/100.0)
    Hy[:xmax,0] = 0.1*sin(2*pi*k/100.0)
    
def plotfields(ti):                                  # screen coordinates
    k = arange(xmax)
    Efield.x = 2*k-xmax                          # world to screen coords
    Efield.y = 800*Ex[k,ti]
    Hfield.x = 2*k-xmax                          # world to screen coords
    Hfield.z = 800*Hy[k,ti]   
        
inifields()                                                # initial time
plotfields(ti)
while True:
    rate(600)
    Ex[1:xmax-1,1] = Ex[1:xmax-1,0] + beta*(Hy[0:xmax-2,0]-Hy[2:xmax,0])
    Hy[1:xmax-1,1] = Hy[1:xmax-1,0] + beta*(Ex[0:xmax-2,0]-Ex[2:xmax,0])
    Ex[0,1]        = Ex[0,0]        + beta*(Hy[xmax-2,0]  -Hy[1,0])  # BC
    Ex[xmax-1,1]   = Ex[xmax-1,0]   + beta*(Hy[xmax-2,0]  -Hy[1,0])  
    Hy[0,1]        = Hy[0,0]        + beta*(Ex[xmax-2,0]  -Ex[1,0])  # BC
    Hy[xmax-1,1]   = Hy[xmax-1,0]   + beta*(Ex[xmax-2,0] - Ex[1,0]) 
    plotfields(ti)                                      # plot new fields
    Ex[:xmax,0] = Ex[:xmax,1]                            # next iteration
    Hy[:xmax,0] = Hy[:xmax,1]                                 # old = new

