# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 15:23:17 2018

@author: b
"""
hoursInDay = 24
minutesInHour = 60

inVal = int(input('Enter value to convert: '))
if inVal > 0:    
    inUnit = input('Enter input unit(days/hours/minutes): ')
    if inUnit == 'days':
        result = inVal * hoursInDay
        print('There are',result,'hours in',inVal,'days')
    elif inUnit == 'hours':
        days = inVal // hoursInDay
        hours = hours % hoursInDay
        print('There are',days,'day and',minutes,'hours in',inVal,'hours')
    elif inUnit == 'minutes':
        hour = inVal // minutesInHour
        days = hour // hoursInDay
        hour = hour - days * hoursInDay
        minutes = inVal % minutesInHour
        print('There are',days,'day and',hour,'hours and',minutes,'minutes in',inVal,'minutes')
    else:
        print('Invalid input unit!')
else:
    print('Value must be positive')