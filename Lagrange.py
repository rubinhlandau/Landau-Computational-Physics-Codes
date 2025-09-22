""" From "COMPUTATIONAL PHYSICS", 3rd Ed, Enlarged Python eTextBook  
    by RH Landau, MJ Paez, and CC Bordeianu
    Copyright Wiley-VCH Verlag GmbH & Co. KGaA, Berlin;  Copyright R Landau,
    Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2015.
    Support by National Science Foundation"""

# Lagrange.py: Langrange interpolation of tabulated data
# Toggle switch selects 1 polynom degree 8 or 4 2nd degree polynomials
from visual import*
from visual.graph import*
from visual.controls import *
sceneK = display(x=0,y=0,width=500,height=500,
title='Lagrange interpolation Toggle switch to interpolate')
graph=curve(color= color.yellow,x=range(0,201),radius=3)
xin = array([0, 25, 50, 75, 100, 125, 150, 175, 200])
yin = array([10.6, 6, 45, 83.5, 52.8, 19.9, 10.8, 8.25, 4.7])
expts=[]                          #will contain poits to fit
yy=zeros((204),float)
w=150
c = controls(x=300, y=50, width=w, height=w, range=60)
t1 = toggle(pos=(0,0), width=30, height=30, text0='1 polynom deg 8', 
      text1='4 polynms deg. 2', action=lambda:  selectpoly())

def selectpoly():
    global polinom                         # to change the previous value
    if t1.value:
        polinom = 3        
    else:
        polinom = 9    
def axis():
    xmin=-200
    xmax=200
    xincr=100
    yincr=400.0/6.0
    ymin=-200
    ymax=200 
    curve(color=color.white,pos=[(-200,-200),(200,-200)])      #hor. axis
    curve(color=color.white,pos=[(-200,-200),(-200,200)])      #ver. axis
    for i in range(0,5):                             #x tics and x labels
        curve(pos=[(xmin+xincr*i,ymin),(xmin+xincr*i,ymin-10)],
				         color=color.white)
        xnum=i*50
        xtext=`xnum`                                     #convert to text                  
        label(pos=(xmin+xincr*i,ymin-30),color=color.white,box=0,text=xtext)
    for i in range(0,7):                             #y tics and y labels
        ynum=i*15
        ytext=`ynum`
        curve(pos=[(xmin-10,ymin+yincr*i),(xmin,ymin+yincr*i)],color=color.white)
        label(pos=(xmin-30,ymin +yincr*i),color=color.white,box=0,text=ytext)
def points():                                        #experimental points
    for i in range (0,9):
        xc=2*xin[i]-200          #x linear trsn. from 0->100 to -200->200
        yc=40*yin[i]/9.0-200     #y linear trsn. from 0->90  to -200->200
        expts.append(sphere(pos=(xc,yc), radius=8,color=color.red))
def legendrepol (x,beg,finish):          #poly interpolation beg:begining
    y = 0.0;
    for  i in range(beg,finish+1): 
       lambd = 1.0;
       for j in range(beg,finish+1):
           if i != j:                       #Lagrange polynom formed here
              lambd *= ((x - xin[j-1])/(xin[i-1] - xin[j-1]))
       y += (yin[i-1] * lambd)
    return y
# Plots 8th degree polynomial through the 9 points or
#    four polynomials of second degree
def plotpoly():
    axis()
    points()                                        #plot the nine points
    if polinom == 9:                          #case of 8th degree polynom
       #joint all points with one polynomial
       xx=0.0
       for  k in range (0,201):                #number of points to graph
           yy[k]=legendrepol(xx,1,9)
           xc=2*xx-200           #x linear coord from 0->100 to -200->200
           yc=40*yy[k]/9.0-200   #y linear coord from 0->90  to -200->200
           graph.x[k]=xc
           graph.y[k]=yc
           xx+=1.0
    graph.pos  
    if polinom==3:                           #case of 2nd degree polynoms
       #use 3 points and a second degree polynomial.
       xx=0.0
       startat=0
       for mm in range(1,8,2):
           for k in range(startat,startat+50 +1):       #keeps track of y
              xx=1.0*k
              yy[k]=legendrepol(xx,mm,mm+2)
              xc=2*xx-200      #x linear trsn. from 0->100 to -200->200
              yc=40*yy[k]/9.0-200 #y linear trsn. from 0->90 to -200->200
              graph.x[k]=xc
              graph.y[k]=yc
           graph.pos
           startat=startat+50

polinom=9
while 1:
    c.interact()                      # checks events like toggle switch
    plotpoly()

