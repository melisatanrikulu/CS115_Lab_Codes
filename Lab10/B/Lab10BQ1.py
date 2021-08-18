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
        u = 2 * i
        y = y + (np.sin(u * x) / u)

    res = pi / 2 + y / 2
    return res

pyplot.clf()
x=np.linspace(-pi,pi,500)
pyplot.plot(x, f(x,1), 'r')
pyplot.plot(x, f(x,3), 'b')
pyplot.plot(x, f(x,13), 'g')
pyplot.legend(['n=1','n=3','n=13'])
 

