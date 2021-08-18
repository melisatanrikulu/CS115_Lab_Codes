# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 15:23:17 2018

@author: Melisa Tanrikulu
"""

# Variables
hoursInDay = 24
minutesInHour = 60
minutesInDay = hoursInDay * minutesInHour

# Input an integer value
value = int(input('Enter value to convert: '))

# Validate the input by checking whether it is positive or not
if value > 0:    
    
    # Input unit
    unit = input('Enter input unit(days/hours/minutes): ')
    
    # Days are converted to hours
    if unit == 'days':
        hours = value * hoursInDay
        
        # Display the result
        print('There are', hours, 'hours in', value, 'days')
        
    # Hours are converted to days and hours
    elif unit == 'hours':
        days = value // hoursInDay
        hours = value % hoursInDay
        
        # Display the result
        print('There are', days, 'day and', hours, 'hours in', value, 'hours')
        
    # Minutes are converted to days, hours and minutes   
    elif unit == 'minutes':
        days = value // minutesInDay
        hours = (value - days * minutesInDay) // minutesInHour
        minutes = value % minutesInHour
        
        # Display the result
        print('There are', days, 'day and', hours, 'hours and', minutes, 'minutes in', value, 'minutes')
        
    # If unit input is invalid, inform the user
    else:
        print('Invalid input unit!')

# If value is invalid, inform the user
else:
    print('Value must be positive')