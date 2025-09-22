""" From "COMPUTATIONAL PHYSICS", 3rd Ed, Enlarged Python eTextBook  
    by RH Landau, MJ Paez, and CC Bordeianu
    Copyright Wiley-VCH Verlag GmbH & Co. KGaA, Berlin;  Copyright R Landau,
    Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2015.
    Support by National Science Foundation"""

# Redirection.py illustrates escape and formatting  characters

import sys
temp=sys.stdout                                       # in temporaty file
sys.stdout = open('outfile2.dat','w')
print("hello \n")
print("\t it's me")                                           # tabulator
b=73
print("decimal 73 as integer b = %d "%(b))                  # for integer
print("as octal b = %o"%(b))                                      # octal
print("as hexadecimal b = %x "%(b))                   # works hexadecimal
print("learn \"Python\" ")                   # use of double quote symbol
print("shows a backslash \\")                                 # use of \\
print('use of single \' quotes \' ')                # print single quotes
sys.stdout.close()
sys.stdout=temp              # to be able to read because file was closed
print(open('outfile2.dat').read())               # read the file produced

