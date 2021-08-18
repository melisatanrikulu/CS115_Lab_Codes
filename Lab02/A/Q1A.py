# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 09:31:41 2018

@author: user
"""

above50 = 0
below20 = 0
below20count = 0

for i in range(10):
    age = int(input('Age of person '+str(i+1)+': '))
    if age > 50:
        above50 += 1
    elif age < 20:
        below20 += age
        below20count += 1

print('There are {0:d} people whose ages are above 50'.format(above50))
print('Average age of people whose ages are below 20: {0:.2f}'.format(below20/below20count))
