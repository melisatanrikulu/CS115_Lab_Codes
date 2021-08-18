# -*- coding: utf-8 -*-
"""
Created on Thu May 17 13:16:48 2018

@author: b
"""

def divisible(m,n):
    if m % n == 0:
        return True
    else:
        return False
        
count=0;
countDiv=0
m =int(input('Enter first positive integer in pair(a number <=0 will stop the program): '))
n =int(input('Enter second positive integer in pair(a number <=0 will stop the program): '))

while (m>0 and n>0):
    count+=1
    if divisible(m,n):
        countDiv+=1;
    m =int(input('Enter first positive integer in pair(a number <=0 will stop the program): '))
    n =int(input('Enter second positive integer in pair(a number <=0 will stop the program): '))

per=100*countDiv/count

print(' {0:.2f} of the pairs are divisible by each other'.format(per))