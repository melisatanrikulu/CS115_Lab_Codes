# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 09:29:26 2019

@author: b
"""
import numpy as np
from matplotlib import pyplot
from math import *

def  f(x,n):
    y = np.zeros(len(x))
    for i in range(1 , n+1):
        u = 2 * i - 1
        y = y + (np.sin(u * x)/u)

    res = pi / 2 + 2 * y
    return res

pyplot.clf()
x=np.arange(-pi,pi,0.01)
pyplot.plot(x, f(x,2), 'r')
pyplot.plot(x, f(x,4), 'b')
pyplot.plot(x, f(x,13), 'g')
pyplot.legend(['n=2','n=4','n=13'])
 

