# -*- coding: utf-8 -*-
'''
Created on Tue Jan 22 08:58:02 2019

@author: user
'''
class ClothingItem:
	 def __init__(self, description,  color, size,  price,  quantity) :
	 	 self.__itemDescription = description
	 	 self.__itemColor = color
	 	 self.__itemSize = size
	 	 self.setItemPrice(price)
	 	 self.setItemQuantity(quantity)
	

	 def getItemDescription(self):
	 	 return self.__itemDescription
	

	 def setItemDescription(self,  description):
	 	 self.__itemDescription = description
	

	 def getItemColor(self): 
	 	 return self.__itemColor
	

	 def setItemColor( self, color):
	 	 self.__itemColor = color
	

	 def getItemSize(self):
	 	 return self.__itemSize
	

	 def setItemSize(self,size):
	 	 self.__itemSize = size
	

	 def getItemPrice(self):
	 	 return self.__itemPrice
	

	 def setItemPrice( self, price):
	 	 if price > 0:
	 	 	 self.__itemPrice = price
	

	 def getItemQuantity(self):
	 	 return self.__itemQuantity
	
	 def setItemQuantity( self, quantity):
	 	 if quantity > 0:
	 	 	 self.__itemQuantity = quantity
	
	 def getTotalPrice(self):
	 	 return self.__itemPrice * self.__itemQuantity
	
	 def __repr__(self):
	 	 return '\nClothingItem [itemDescription=' + self.__itemDescription + ', itemColor=' + self.__itemColor + ', itemSize='+str(self.__itemSize) + ', itemPrice=' + str(self.__itemPrice) + ', itemQuantity=' + str(self.__itemQuantity) + ']'
	