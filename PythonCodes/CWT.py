""" From "COMPUTATIONAL PHYSICS", 3rd Ed, Enlarged Python eTextBook  
    by RH Landau, MJ Paez, and CC Bordeianu
    Copyright Wiley-VCH Verlag GmbH & Co. KGaA, Berlin;  Copyright R Landau,
    Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2015.
    Support by National Science Foundation"""

# CWT.py  Continuous Wavelet TF. Based on program by Zlatko Dimcovic 
from visual import *												
import matplotlib.pylab as p;
from mpl_toolkits.mplot3d import Axes3D ;
import numpy

iT =  0.0;          fT =  12.0;     W = fT - iT;    N =  240;   h =  W/N
noPtsSig =  N;      noS =  20;      noTau =  90;    iTau =  0.
iS =  0.1;          tau =  iTau;        s =  iS                
            
# Need *very* small s steps for high frequency if s small;
dTau =  W/noTau;    dS =  (W/iS)**(1./noS);
maxY =  0.001;      sig =  zeros((noPtsSig), float)              
      
def signal(noPtsSig, y):                                         # Signal
    t = 0.0;     hs = W/noPtsSig;     t1 = W/6.;    t2 = 4.*W/6.
    for i in range(0, noPtsSig):  
        if  t >= iT  and t <=  t1:  y[i] =  sin(2*pi*t)
        elif t >= t1 and t <=  t2: y[i] = 5.*sin(2*pi*t)+10.*sin(4*pi*t);
        elif t >= t2 and t <=  fT: 
             y[i] = 2.5*sin(2*pi*t) + 6.*sin(4*pi*t) + 10.*sin(6*pi*t)
        else: 
            print("In signal(...) : t out of range.")
            sys.exit(1)
        t += hs    
signal(noPtsSig, sig)                                       # Form signal
Yn =  zeros( (noS+1, noTau+1), float)                         # Transform

def morlet(t, s, tau):                                   # Mother wavelet
     T =  (t - tau)/s
     return sin(8*T) * exp( - T*T/2. )
	
def transform(s, tau, sig):                                    # Finds TF
    integral = 0.
    t = iT;                                                        # Time
    for i in range(0, len(sig) ):
         t += h
         integral += sig[i]*morlet(t, s, tau)*h
    return integral / sqrt(s)
          
def invTransform(t, Yn):                       # Compute nonormed inverse
    s = iS                                           
    tau = iTau                                      
    recSig_t = 0                 
    for i in range (0, noS):
        s *= dS                                               # Scale = s
        tau = iTau                                          
        for j in range (0, noTau):
            tau += dTau                 
            recSig_t += dTau*dS *(s**(-1.5))*Yn[i,j] * morlet(t, s, tau)
    return recSig_t

print("working, finding transform, count 20")
for i in range( 0, noS):
    s *= dS             # was with *                            # Scaling
    tau = iT
    print(i)
    for j in range(0, noTau):
         tau += dTau                                        # Translation
         Yn[i, j] = transform(s, tau, sig)
print("transform found")  
for i in range( 0, noS):
    for j in range( 0, noTau):
        if Yn[i, j] > maxY or Yn[i, j] < - 1 *maxY :
            maxY = abs( Yn[i, j] )                           # Find max Y
tau =  iT
s =  iS
print("normalize")      
for i in range( 0, noS):
     s *= dS                             
     for j in range( 0, noTau):
         tau +=   dTau                                        # Transform
         Yn[i, j] = Yn[i, j]/maxY
     tau = iT
print("finding inverse transform")                      # Find inverse TF
recSigData =  "recSig.dat"                   
recSig =  zeros(len(sig) )                              # Same resolution
t =  0.0;
print("count to 10")
kco = 0;            j = 0;              Yinv =  Yn             

x = list(range(1, noS + 1))                                  # For x plot
y = list(range(1, noTau + 1))                                # For y plot
X,Y = p.meshgrid(x, y)                               # Grid for s and tau

def functz(Yn):                                        # Return transform
    z = Yn[X, Y]    
    return z
              
Z = functz(Yn)  
fig = p.figure()                                         # Creates figure
ax = Axes3D(fig)
ax.plot_wireframe(X, Y, Z, color = 'r')  
ax.set_xlabel('s: scale')   
ax.set_ylabel('Tau')
ax.set_zlabel('Transform')
p.show()

