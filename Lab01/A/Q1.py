# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 14:24:32 2018

@author: Melisa Tanrikulu
"""

import math

# Input a decimal number
x = float(input('Input x: '))

# Compute the result
result = ((x * x * x) + 3 * math.fabs(x) + 9) / (x * x)

# Display the result
print('The result of the expression: {0:.2f}'.format(result))
