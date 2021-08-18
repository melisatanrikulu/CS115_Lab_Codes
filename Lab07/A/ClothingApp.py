# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 09:12:10 2019

@author: user
"""
from ClothingItem import *

def readItems(items, fileName):
    fileIn = open(fileName, 'r')
    for line in fileIn:
        data = line.split(';')
        description = data[0]
        color= data[1]
        size = data[2]
        price = float(data[3])
        quantity = int(data[4])
        item = ClothingItem(description, color, size, price, quantity)
        items.append(item)
    fileIn.close()
        
items = []
readItems(items, 'clothing.txt')

print('Clothing Items:')
for item in items:
    print('\t',item)
print('\nAll Medium Gray Pants:')
for temp in items:
    if temp.getItemSize() == 'm' and temp.getItemColor().lower() == 'gray' and 'pants'  in temp.getItemDescription():
        print(temp)

total = 0.0
for temp in items:
    total += temp.getTotalPrice()
print('Total Inventory Value: {0:.2f}\n'.format(total))

	