# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 12:45:00 2019

@author: b
"""

from MenuItem import *


def readMenuItems(fileName):

    inp = open(fileName, 'r')
       
    
	 #create list to store items
    items = []
		

    #read data from file into list
    for line in inp:
        info = line.strip().split(';')
       
          
        #create new MenuItem
        item = MenuItem(info[0], info[1], int(info[2]), int(info[3]), float(info[4]))
            
        #add MenuItem to list
        items.append(item)
		
    inp.close()
    return items
	

menuItems = readMenuItems('items.txt')
		
#display all MenuItems
print('Menu Items:')
for item in menuItems:
    print(item)
		
print('\nAll Menu Items with calories less than 1000 containing meat:')
for item in menuItems:
	if item.getItemCalories() < 1000 and (item.getItemDescription().find('meat') != -1):
		print(item)
			
total = 0.0
		
#display the average cost per ingredient for all menu items 
for item in menuItems:
	total += item.getAverageCostPerIngredient()

avg = total / len(menuItems)
		
print('\nAverage Cost Per Ingredient of All Menu Items: {0:.2f}\n'.format(avg))
		
	
	 


