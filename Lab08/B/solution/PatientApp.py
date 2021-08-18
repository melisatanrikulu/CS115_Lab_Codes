# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 15:26:44 2019

@author: b
"""

import datetime
from Outpatient import *

def schedulePatients(fileName, pList):
    #self, name,  ins, aDate, aTime, clinic, dName, cPercent=0.0
    inFile = open(fileName, 'r')
    for line in inFile:
        data = line.strip().split(';')
       
        name = data[0] 
        aDate = data[1]
        aTime = data[2]
        clinic = data[4]
        dName = data[3]
        
        ins = data[5] == 'True'
        if ins:
            cPercent = float(data[6])    		
            p = Outpatient( name,  ins, aDate, aTime, clinic, dName, cPercent/100 )
        else:
            p = Outpatient(name,  ins, aDate, aTime, clinic, dName )
        pList.append(p)    	
    inFile.close()
    
   
pList = []
schedulePatients("patients.txt", pList)
pList.sort()
print(pList)
