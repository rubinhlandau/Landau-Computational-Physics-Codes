""" From "COMPUTATIONAL PHYSICS", 3rd Ed, Enlarged Python eTextBook  
    by RH Landau, MJ Paez, and CC Bordeianu
    Copyright Wiley-VCH Verlag GmbH & Co. KGaA, Berlin;  Copyright R Landau,
    Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2015.
    Support by National Science Foundation"""

#  QuantumNumerov:  Quantum BS via Numerov ODE solver + search

from visual import *
from visual.graph import *
psigr  = display(x=0, y=0, width=600,height=300,title='R & L Wave Funcs')
psi    = curve(x=list(range(0,1000)), display=psigr, color=color.yellow)
psi2gr = display(x=0,y=300,width=600,height=200,title='Wave func^2')
psio   = curve(x=list(range(0,1000)),color=color.magenta, display=psi2gr)
energr = display(x=0, y=500, width=600,height=200,title='Potential & E')
poten  = curve(x=list(range(0,1000)), color=color.cyan, display=energr)
autoen = curve(x=list(range(0,1000)), display=energr)

dl    = 1e-6                      # very small interval to stop bisection
ul    = zeros([1501], float)
ur    = zeros([1501], float)
k2l   = zeros([1501], float)     # k**2 in Schroedinger eq. left wavefunc
k2r   = zeros([1501], float)    # k**2 in Schroedinger eq. right wavefunc
n     = 1501
m     = 5                                        # to plot every 5 points
imax  = 100 
xl0   = -1000;   xr0   =  1000      # leftmost, rightmost x wave function
h     = (1.0*(xr0-xl0)/(n-1.))            # 1.0 to make it a float number
amin  = -0.001; amax  = -0.00085             # root between amin and amax
e     = amin                                   # Initial guess for energy
de    = 0.01
ul[0] = 0.0; ul[1] = 0.00001; ur[0] = 0.0; ur[1] = 0.00001     
im = 500                                  # match point left and right wv
nl = im+2;   nr = n-im+1                             # for left, right wv
istep=0

def V(x):                                  # Potential finite square well
    if (abs(x)<=500):	  v = -0.001                           # well depth
    else:               v = 0
    return v

def setk2():                             # sets k2l=(sqrt(e-V))^2 and k2r
    for i in range(0,n):         
       xl = xl0+i*h
       xr = xr0-i*h
       k2l[i] = e-V(xl)
       k2r[i] = e-V(xr)
			 
def numerov (n,h,k2,u):               # Numerov algorithm can be used for
    b=(h**2)/12.0                         # left and right wave functions
    for i in range(1, n-1):  
     u[i+1] = (2*u[i]*(1-5*b*k2[i])-(1.+b*k2[i-1])*u[i-1])/(1+b*k2[i+1])
				
setk2()
numerov (nl, h, k2l, ul)                       # finds left wave function
numerov (nr, h, k2r, ur)                      # finds right wave function
fact= ur[nr-2]/ul[im]                              # to Rescale  solution
for i  in range (0,nl): ul[i] = fact*ul[i]
f0 = (ur[nr-1]+ul[nl-1]-ur[nr-3]-ul[nl-3])/(2*h*ur[nr-2])    #  Log deriv

def normalize():    
    asum = 0
    for i in range( 0,n):                    # to normalize wave function
        if i > im :
            ul[i] = ur[n-i-1]
            asum = asum+ul[i]*ul[i]
    asum        = sqrt(h*asum); 
    elabel      = label(pos=(700, 500), text='e=', box=0,display=psigr)
    elabel.text = 'e=%10.8f' %e
    ilabel      = label(pos=(700,400),text='istep=',box=0,display=psigr)
    ilabel.text = 'istep=%4s' %istep
    poten.pos   = [(-1500,200),(-1000,200),(-1000,-200),
		                          (0,-200),(0,200),(1000,200)]
    autoen.pos = [(-1000,e*400000.0+200),(0,e*400000.0+200)]
    label(pos=(-1150,-240), text='0.001', box=0, display=energr)
    label(pos=(-1000,300),  text='0',     box=0, display=energr)
    label(pos=(-900,180),   text='-500',  box=0, display=energr)
    label(pos=(-100,180),   text='500',   box=0, display=energr)
    label(pos=(-500,180),   text='0',     box=0, display=energr)
    label(pos=(900,120),    text='r',     box=0, display=energr)

    j=0
    for i in range(0,n,m):                   
        xl        = xl0 + i*h
        ul[i]     = ul[i]/asum                 # wave function normalized
        psi.x[j]  = xl - 500                                   # plot psi
        psi.y[j]  = 10000.0*ul[i]       # vertical line for match of wvfs
        line      = curve(pos=[(-830,-500),(-830,500)],
				            color=color.red,display=psigr)
        psio.x[j] = xl-500                                     # plot psi
        psio.y[j] = 1.0e5*ul[i]**2
        j +=1

while abs(de) > dl and istep < imax :        # bisection algorithm begins
    rate(2)                                      # to slowdown  animation
    e1 = e                                                 # guessed root
    e  = (amin+amax)/2                                    # half interval
    for i in range(0,n):  
        k2l[i] = k2l[i] + e-e1             
        k2r[i] = k2r[i] + e-e1
    im = 500;
    nl = im+2
    nr = n-im+1;
    numerov (nl,h,k2l,ul)             # Find wavefuntions for new k2l,k2r
    numerov (nr,h,k2r,ur)               
    fact = ur[nr-2]/ul[im]
    for i in range(0,nl):  ul[i] = fact*ul[i] 
    f1 = (ur[nr-1]+ul[nl-1]-ur[nr-3]-ul[nl-3])/(2*h*ur[nr-2]) # Log deriv
    rate(2)
    if f0*f1 < 0:                               # bisection localize root
        amax = e
        de = amax - amin
    else:
         amin = e
         de = amax - amin
         f0 = f1
    normalize()     
    istep = istep + 1

     
