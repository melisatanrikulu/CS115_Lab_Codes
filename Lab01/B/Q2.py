# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 14:44:00 2018

@author: Melisa Tanrikulu
"""

# Input an integer value
num = int(input('Enter an integer number: '))

# If the number is greater than 100, inform the user
if num > 100: 
    print('Value is greater than 100')
    
# If the number is between 50 and 100 inclusive, inform the user    
elif num >= 50:
    print('Value is between [50-100]')
    
# If the number is less than 50, inform the user    
else:
    print('Value is less than 50 ')
    