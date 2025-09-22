''' From: "A SURVEY OF COMPUTATIONAL PHYSICS" 
   by RH Landau, MJ Paez, and CC BORDEIANU 
   Copyright Princeton University Press, Princeton, 2007.
   Electronic Materials copyright: R Landau, Oregon State Univ, 2007;
   MJ Paez, Univ Antioquia, 2007; and CC BORDEIANU, Univ Bucharest, 2007.
   Support by National Science Foundation                              
'''
# AreaFormatted: examples formated, keyboard  & file I/O (Python 3 not 2)

from numpy import *

name = input('Key in your name: ')              # String input
print("Hi ", name)
radius = eval(input('Enter a radius: '))        # Convert string to numeric
print('you entered radius = %8.5f'%(radius))    # Formatted output
outfile = open('A.dat','w')                     # Open file A.dat to write
outfile.write(name)                             # Output name in A.dat
outfile.write( '   radius=  %13.5f'%(radius))   # Output radius in A.dat
Area = pi*radius**2                                 
outfile.write('    Area =  %13.5f\n'%(Area))    # Output area in A.dat
outfile.close()                                 # Close A.dat
print("name radius Area written in file A.dat")
print("next: read file A.dat")

inpfile = open('A.dat','r')                     # Open A.dat for read
for line in inpfile:                            # One line, 5 entries
    line = line.split()                         # Split components of line
    name = line[0]                              # 1st entry  
    print(" Hi  %10s" %(name))                  # Print Hi plus name         
    r = float(line[2])                          # Covert r to float
    print(" r = %13.5f" %(r))                   # Print r
    print("area = ", Area)                      # Nonformatted output
inpfile.close()                                 # Close inpfile
 
# Sample  A.dat: Robert   radius=        9.00000    Area=      254.46900

