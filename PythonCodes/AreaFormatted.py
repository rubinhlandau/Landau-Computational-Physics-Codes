""" From "COMPUTATIONAL PHYSICS", 3rd Ed, Enlarged Python eTextBook  
    by RH Landau, MJ Paez, and CC Bordeianu
    Copyright Wiley-VCH Verlag GmbH & Co. KGaA, Berlin;  Copyright R Landau,
    Oregon State Unv, MJ Paez, Univ Antioquia, C Bordeianu, Univ Bucharest, 2015.
    Support by National Science Foundation""" 
    
# AreaFormatted: examples: formated output, keyboard I/O, file I/O
#                Need Name and radius in file Name.dat

from numpy import *; from sys import version
if int(version[0])>2: raw_input=input   # raw_input deprecated in Python 3
name = raw_input( 'Key in your name: ')     # raw_input good for strings
print("Hi ",name)
radius = eval(raw_input('Enter a radius: '))            # OK for numbers
print('you entered radius= %8.5f'%radius)              # formatted output
name = raw_input('Key in another name: ')      # raw_input OK for strings
radius = eval(raw_input('Enter a radius: '))
print('Enter new name and r in file Name.dat')
inpfile = open('Name.dat','r')                 # Read from file Name.dat
for line in inpfile:
    line = line.split()                     # splits components of line
    name = line[0]                                  # first entry in list
    print(" Hi  %10s" %(name))                # print Hi plus first entry          
    r = float(line[1])                # 2nd entry, convert string to float
    print(" r = %13.5f" %(r))            # converts to float and print
inpfile.close()
A = math.pi*r**2                   # use radius to find circles's area
print("Done, look in A.dat\n")
outfile=open('A.dat','w')
outfile.write( 'r=  %13.5f\n'%(r))
outfile.write('A =  %13.5f\n'%(A))
outfile.close()
print('r = %13.5f'%(r))                                  #screen output    
print('A = %13.5f'%(A))             
print('Now example of integer input ')
age=int(eval(raw_input ('Now key in your age as an integer:  ')))
print("age: %4d  years old,  you don't look it!\n"%(age))

