# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 13:40:16 2019

@author: b
"""

def minMaxList(list1, list2):
    for row in range(len(list1)):
        for col in range(len(list1[row])):
            if list1[row][col] > list2[row][col]:
                 list1[row][col], list2[row][col] = list2[row][col], list1[row][col] 
    			
            elif list1[row][col] == list2[row][col]:
                list1[row][col] = 0
                list2[row][col] = 0

mat1 = [[8,3,5],[4,6,2],[11,12,20]]
mat2 = [[7,2,6],[5,6,30],[1,15,24]]
print('Before Calling Function:')
print(mat1)
print(mat2)
minMaxList(mat1, mat2)
print('After calling function: ')
print(mat1)
print(mat2)