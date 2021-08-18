# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 10:03:51 2019

@author: b
"""
import numpy as np
from matplotlib import pyplot
from math import *
pyplot.figure(1)
pyplot.clf()

depth=np.loadtxt('seed.txt')
weeks=np.arange(1,16)
pyplot.subplot(2,1,1)

pyplot.title('Order 1')
pyplot.plot(weeks,depth,'bo')

p=np.polyfit(weeks,depth,1)
d1=np.polyval(p,weeks)
pyplot.plot(weeks,d1)
pyplot.xlabel('weeks')
pyplot.ylabel('d')
 
pyplot.subplot(2,1,2)
pyplot.title('Order 2')
pyplot.plot(weeks,depth,'bo')

p=np.polyfit(weeks,depth,2)
d2=np.polyval(p,weeks)
pyplot.plot(weeks,d2)
pyplot.grid(True)
pyplot.legend('Exp 1')



