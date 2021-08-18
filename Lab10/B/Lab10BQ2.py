# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 10:21:05 2019

@author: b
"""
import numpy as np
from matplotlib import pyplot
from math import *

pyplot.figure(1)
pyplot.clf()

x = np.arange(1,8)
y = np.loadtxt('y.txt')
p1 = np.polyfit(x,y,1)
ny1 = np.polyval(p1,x) 

p2  = np.polyfit(x,y,2)
ny2 = np.polyval(p2,x) 

pyplot.subplot(1,2,1)
pyplot.plot(x,y)
pyplot.plot(x,ny1,'r--')
pyplot.title('Fitting to a Linear Plot')

pyplot.subplot(1,2,2)
pyplot.plot(x,y)
pyplot.plot(x,ny2, 'mx:')
pyplot.title('Fitting to a Quadratic Plot')