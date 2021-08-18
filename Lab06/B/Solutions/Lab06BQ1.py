# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 13:40:17 2019

@author: b
"""

def findMatches(slist, word):
    arr = []

    for r in range(len(slist)):
        newStr = ''
    	
        for col in range(len(slist[r])):
            newStr += slist[r][col]
            
        if newStr.find(word) != -1:
        	arr.append(newStr)
            
    return arr

mat = [['i','t','a','l','y'],
       ['t','r','e','e','s'],
       ['b','r','i','t','e'],
       ['s','u','d','a','n']]
print('Two Dimensional List: ')
for row in mat:
    print(row)
found = findMatches(mat, 'it')
print('Matching words:',found)