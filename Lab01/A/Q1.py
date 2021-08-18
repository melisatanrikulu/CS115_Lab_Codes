# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 14:37:21 2018

@author: b
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 14:24:32 2018

@author: b
"""
import math

#input x value
x = float(input('Enter x: '))

result = ((x * x * x) + 3 * math.fabs(x) + 9) / (x * x)
print('The result of the calculation is {0:.2f}'.format(result))
