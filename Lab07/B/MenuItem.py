# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 12:22:05 2019

@author: b
"""

class MenuItem():
	
    def __init__(self, name, description,  ing, calories,  cost):
        self.__itemName = name
        self.__itemDescription = description
        self.__ingredients = ing
        self.setItemCalories(calories)
        self.setItemCost(cost)
	

    def getItemDescription(self):
        return self.__itemDescription
	

    def setItemDescription(self,description):
        self.__itemDescription = description
	

    def getItemName(self):
        return self.__itemName
	

    def setItemName(self, name):
        self.__itemName = name
	

    def getIngredients(self):
        return self.__ingredients
	

    def setIngredients(self, ing):
        self.__ingredients = ing
	
    
    def getItemCalories(self):
        return self.__itemCalories
	

    def setItemCalories(self, calories):
        if calories > 0:
            self.__itemCalories = calories
	

    def getItemCost(self): 
        return self.__itemCost
	

    def setItemCost(self, cost): 
        if cost > 0:
            self.__itemCost = cost
	
    def getAverageCostPerIngredient(self):
        return self.__itemCost / self.__ingredients
	
    def __repr__(self):
        return "\nMenuItem [itemDescription=" + self.__itemDescription \
        + ", itemName=" + self.__itemName \
        + ", calories=" + str(self.__itemCalories) \
        + ", ingredients=" + str(self.__ingredients) \
        + ", itemCost=" + str(self.__itemCost) + "]\n"
	
	

