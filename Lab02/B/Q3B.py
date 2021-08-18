# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 13:13:08 2019

@author: b
"""

def dis(n):
    for i in range (1,n+1):
      for j in range (1, i+1):
         print(j, end =" ")
      for j in range (i-1,0,-1):
         print(j, end =" ")
      print()
        
num=int(input('Enter the number of lines:'))
dis(num)