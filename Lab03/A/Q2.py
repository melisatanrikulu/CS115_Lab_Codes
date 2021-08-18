# -*- coding: utf-8 -*-
"""
Created on Thu May 17 13:16:48 2018

@author: b
"""

def findDigits(n):
    #find the last digit
    lastDigit = n % 10
    
    #find the first digit
    while n > 10:
        n //= 10
        
    firstDigit = n 
    
    return firstDigit,lastDigit
        

num =int(input('Enter an integer number (<=0 will stop the program): '))

while (num>=0):
    f,l=findDigits(num)
   
    if f==l:
        print(' {0:d} has the same first digit and last digit'.format(num))
    num =int(input('Enter an integer number (<=0 will stop the program): '))