# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 14:44:00 2018

@author: Melisa Tanrikulu
"""

# Input an integer
num = int(input('Enter an integer number: '))

# If input is even and positive, inform the user
if num%2 == 0 and num > 0: 
    print('Value even and positive')
    
# If input is odd and positive, inform the user
elif num%2 == 1 and num > 0:
    print('Value odd and positive')
    
# If input is zero, inform the user   
elif num == 0:
    print('Number is zero')
    
# If input is negative, inform the user   
else:   
    print('Number is not positive ')
    