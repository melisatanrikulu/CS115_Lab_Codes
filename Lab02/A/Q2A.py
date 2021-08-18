# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 09:19:41 2018

@author: user
"""

num = int(input('Enter positive integer : '))

    
updateNum = num
isOrdered = True
digit = updateNum %10
while updateNum != 0 and isOrdered:
    prevDigit = digit 
    digit = updateNum %10
    
    if prevDigit > digit:
        isOrdered = False
        
    updateNum = updateNum // 10
    
if isOrdered:
    print('Digits are in descending order')
else:
    print('Digits are not in descending order')
    