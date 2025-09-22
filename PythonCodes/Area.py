""" From "COMPUTATIONAL PHYSICS", 3rd Ed, Enlarged Python eTextBook  
    by RH Landau, MJ Paez, and CC Bordeianu
    Copyright Wiley-VCH Verlag GmbH & Co. KGaA, Berlin;  Copyright R Landau,
    Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2015.
    Support by National Science Foundation"""                         

# Area.py: Area of a circle, simple program

from math import pi
from sys import version
if int(version[0])>2: raw_input=input   # raw_input deprecated in Python 3
     
modelN = 1
radius = 1.
circum = 2.*pi*radius
area = radius * radius *pi

print ('Program number = ', modelN)
print ('Radius,  Circumference, Area = ', radius, circum, area)
print("press a key to finish")
s=raw_input()

# Expected OUTPUT:
'''
Program number =  1
Radius,  Circumference, Area =  1.0 6.283185307179586 3.141592653589793
press a key to finish
'''

