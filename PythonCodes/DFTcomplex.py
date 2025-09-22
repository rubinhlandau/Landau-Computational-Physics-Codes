""" From "COMPUTATIONAL PHYSICS", 3rd Ed, Enlarged Python eTextBook  
    by RH Landau, MJ Paez, and CC Bordeianu
    Copyright Wiley-VCH Verlag GmbH & Co. KGaA, Berlin;  Copyright R Landau,
    Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2015.
    Support by National Science Foundation"""

# DFTcomplex.py:  Discrete Fourier Transform, using built in complex
from visual import *
from visual.graph import *
import cmath                                 # for complex math functions
                                
signgr = gdisplay(x=0, y=0, width=600, height=250, title ='Signal',\
             xtitle='x', ytitle = 'signal', xmax = 2.*math.pi, xmin = 0,\
						 ymax = 30, ymin = 0)
sigfig = gcurve(color=color.yellow, display=signgr)
imagr = gdisplay(x=0,y=250,width=600,height=250,title ='Imag Fourier TF',
       xtitle = 'x',ytitle='TF.Imag',xmax=10.,xmin=-1,ymax=100,ymin=-0.2)
impart = gvbars(delta = 0.05, color = color.red, display = imagr)  # thin

N = 50;                  Np = N                           # Number points
signal = zeros( (N+1), float )     
twopi  = 2.*pi;       sq2pi = 1./sqrt(twopi);         h = twopi/N
dftz   = zeros( (Np), complex )               # sequence complex elements

def f(signal):                                          # signal function
    step = twopi/N;        x = 0. 
    for i in range(0, N+1):
       signal[i] = 30*cos(x*x*x*x)
       sigfig.plot(pos = (x, signal[i]))                    # plot signal
       x += step
      
def fourier(dftz):                                                  # DFT
    for n in range(0, Np):              
      zsum = complex(0.0, 0.0)               # real and imag parts = zero
      for  k in range(0, N):                              # loop for sums
          zexpo = complex(0, twopi*k*n/N)              # complex exponent
          zsum += signal[k]*exp(-zexpo)          # Fourier transform core
      dftz[n] = zsum * sq2pi                                     # factor
      if dftz[n].imag != 0:                  # plot if not too small imag
          impart.plot(pos = (n, dftz[n].imag) )               # plot bars

f(signal);       fourier(dftz)                   # call signal, transform
