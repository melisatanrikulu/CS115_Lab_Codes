# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 22:22:01 2019

@author: Melisa Tanrikulu
"""

# Variables
mainDish = 15
starter = 10
dessert = 8
cost = 0

# Input budget
budget = int(input('Enter budget: '))

# If budget is not enough for a main dish, inform the user
if budget < mainDish:
    print('More money needed')
    
# If budget is enough for a main dish, order a main dish
else:
    # Update budget and cost and inform the user
    budget -= mainDish
    cost += mainDish
    print('Main dish added.')
    
    # If the remaining budget is not enough for a starter, inform the user
    if budget < starter:
        print('Budget not sufficient for starter...')
        
    # If the remaining budget is enough for a starter, order a starter
    else:
        # Update budget and cost and inform the user
        budget -= starter
        cost += starter
        print('Starter added.')
    
    # If the remaining budget is not enough for a dessert, inform the user 
    if budget < dessert:
        print('Budget not sufficient for dessert...')
        
    # If the remaining budget is enough for a dessert, order a dessert    
    else:
        # Update budget and cost and inform the user
        budget -= dessert
        cost += dessert        
        print('Dessert added.')

    # Display the final bill and the remaining budget
    print('Total Meal Cost: ', cost, 'Remaining Budget: ', budget)
