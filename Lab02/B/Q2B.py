# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 09:19:41 2018

@author: user
"""

num = int(input('Enter a positive integer: '))

if num < 0:
    print('Number cannot be Negative')
elif num < 10:
    print('Number must be at least Two-digits')
else:
    inputNum = num
    maxDigit = num%10
    secondMax = -1
  
    
    while num > 10:
        num = num // 10
        digit = num%10
        if digit > maxDigit:
            secondMax = maxDigit
            maxDigit = digit
        elif digit > secondMax:
            secondMax = digit
        
    if secondMax >= -1:
        print('The second largest digit in',inputNum,'is',secondMax)
        
       
