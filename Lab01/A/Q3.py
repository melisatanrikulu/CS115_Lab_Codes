# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 22:22:01 2019

@author: Zeki
"""

budget = int(input('Enter budget: '))
mainDish = 15
starter = 10
dessert = 8
cost = 0

if budget < mainDish:
    print('More money needed')
else:
    print('Main Dish Added.')
    budget -= mainDish
    cost += mainDish
    if budget < starter:
        print('Budget not sufficient for starter...')
    else:
        print('Starter Added.')
        budget -= starter
        cost += starter
    if budget < dessert:
        print('Budget not sufficient for dessert...')
    else:
        print('Dessert added.')
        budget -= dessert
        cost += dessert

    print('Meal Cost: ', cost, 'Remaining Budget: ', budget)
