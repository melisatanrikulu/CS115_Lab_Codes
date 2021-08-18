# -*- coding: utf-8 -*-
"""
Created on Thu May 17 13:16:48 2018

@author: b
"""

def largestDivisor(n):
    for i in range (n-1,0,-1):
        if (n % i==0):
                 return i
        

num=int(input('Enter a positive integer >=1: '))
while num >= 1:
    res=largestDivisor(num)
    if (res>1):
       print(str(num), ' is not a prime number ')
    else:
        print(str(num), ' is a prime number ')
    num=int(input('Enter a positive integer >=1: '))