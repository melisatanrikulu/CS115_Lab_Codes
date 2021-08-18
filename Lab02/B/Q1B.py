# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 09:03:43 2018

@author: user
"""

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
gcd = 0;

while num1 <= 0 or num2 <= 0:
    print('Numbers must be positive')
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))

for i in range(1,min(num1,num2)+1):
    if num1%i == 0 and num2%i == 0:
        gcd = i
print('The greatest common divisor of',num1,'and',num2,'is',gcd)