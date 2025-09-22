""" From "COMPUTATIONAL PHYSICS", 3rd Ed, Enlarged Python eTextBook  
    by RH Landau, MJ Paez, and CC Bordeianu
    Copyright Wiley-VCH Verlag GmbH & Co. KGaA, Berlin;  Copyright R Landau,
    Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2015.
    Support by National Science Foundation"""                             

#  vonNeuman: Monte-Carlo integration via stone throwing 
from visual import *
import random
from visual.graph import *

N        = 100   # points to plot the function
graph    = display(width=500,height=500,title='vonNeumann Rejection Int')
xsinx    = curve(x=list(range(0,N)), color=color.yellow, radius=0.5)    
pts      = label(pos=(-60, -60), text='points=', box=0)          # labels
pts2     = label(pos=(-30, -60), box=0)
inside   = label(pos=(30,-60), text='accepted=', box=0)
inside2  = label(pos=(60,-60), box=0)
arealbl  = label(pos=(-65,60), text='area=', box=0)
arealbl2 = label(pos=(-35,60), box=0)
areanal  = label(pos=(30,60), text='analytical=', box=0)
zero     = label(pos=(-85,-48), text='0', box=0)
five     = label(pos=(-85,50), text='5', box=0)
twopi    = label(pos=(90,-48), text='2pi',box=0)

def fx (x):  return x*sin(x)*sin(x)                           # Integrand
		
def plotfunc():             # Plot function and the box
    incr = 2.0*pi/N
    for i in range(0,N):
        xx         = i*incr
        xsinx.x[i] = ((80.0/pi)*xx-80)
        xsinx.y[i] = 20*fx(xx)-50
    box            = curve(pos=[(-80,-50), (-80,50), (80,50)
                   ,(80,-50), (-80,-50)], color=color.white)        # box
    
plotfunc()                     # the area of the box = height*width=5*2pi
j            = 0
Npts         = 3001                     # points generated inside the box
analyt       = (pi)**2                              # analytical integral
areanal.text = 'analytical=%8.5f'%analyt     # Output analytical integral
genpts       = points(size=2)
for i in range(1,Npts):                 # generates points inside the box
    rate(500)               # to slow the process to see point generation
    x = 2.0*pi*random.random()                             # 0=< x <= 2pi
    y = 5*random.random()                                    # 0=< x <= 5
    xp = x*80.0/pi-80
    yp = 20.0*y-50 
    pts2.text = '%4s' %i
    if y <= fx(x):                                 # case below the curve
           j += 1                            # increase count below curve
           genpts.append(pos=(xp,yp), color=color.cyan)
           inside2.text='%4s'%j                   # accepted points label
    else:  genpts.append(pos=(xp,yp), color=color.green)
    boxarea = 2.0*pi*5.0                        # area of box propto Npts
    area = boxarea*j/(Npts-1)                    # area of curve propto j
    arealbl2.text = '%8.5f'%area            # write current computed area

