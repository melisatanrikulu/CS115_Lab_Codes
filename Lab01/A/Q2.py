# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 14:44:00 2018

@author: b
"""

num = int(input('Enter an integer number: '))
if num%2 == 0 and num > 0: 
    print('Value even and positive')
elif num%2 == 1 and num > 0:
    print('Value odd and positive')
elif num == 0:
    print('Number is zero')
else:   
    print('Number is not positive ')
    