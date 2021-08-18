# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 14:24:32 2018

@author: Melisa Tanrikulu
"""

# Input 3 decimal numbers
x = float(input('Enter x: '))
y = float(input('Enter y: '))
z = float(input('Enter z: '))

# Calculate the result
result = (x+y*z)*(x*y+z)/(x+y)

# Display the result
print('The result of the calculation is {0:.2f}'.format(result))
