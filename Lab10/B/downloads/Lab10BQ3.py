# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 15:11:52 2018

@author: b
"""
from matplotlib.pyplot import *
from Field import *
from Drunk import *
from Location import *

def walk(f, d, numSteps):
    """Assumes: f a Field, d a Drunk in f, and numSteps an int >= 0.
       Moves d numSteps times, and returns the distance between
       the final location and the location at the start of the 
       walk."""
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))

#random.seed(0)
clf()

f = Field()
#Create 7 ColdDrunks and add them to the field.

distances = []
drunks = f.getDrunks()
colors = ['ro', 'mo', 'bo', 'go', 'ko','co','yo']
cPos = 0


#Each drunk should take 5 walks of 1000 steps.  
#You should plot the location of each drunk, at the end of each walk.  



#iii.	For all walks of all drunks you should store the distance between 
#the origin and the final location, and display the 
#average, minimum and maximum distances.

