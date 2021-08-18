# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 13:24:04 2019

@author: b
"""
from doctor import *

def bubbleSort(data):
    issorted = False;
    j = 0
    while(j < len(data)-1 and not issorted):
        issorted = True;
        for k in range(len(data)-j-1):
            if data[k].getHospital() > data[k+1].getHospital():
                issorted = False
                (data[k], data[k + 1]) = (data[k+1], data[k])
            elif data[k].getHospital() == data[k+1].getHospital():
                if data[k].getSpecialty() > data[k+1].getSpecialty():
                    issorted = False
                    (data[k], data[k + 1]) = (data[k+1], data[k])
        j = j + 1

def binarySearch(data, sId, startInd, endInd):
    if(startInd > endInd):
        return -1
    else:
        mid = (startInd + endInd)//2
        if(data[mid].getDoctorId() == sId):
            return mid
        elif(data[mid].getDoctorId()  > sId):
            return binarySearch(data, sId, startInd, mid-1)
        else:
            return binarySearch(data, sId, mid+1, endInd)

def readDoctors(fileName, doctors):
    dFile = open(fileName,'r')
    for line in dFile:
        data = line.strip().split(';')
        dId = data[0]
        dName = data[1]
        dSpec = data[2]
        hosp = data[3]
        doctors.append(Doctor(dId, dName,dSpec,hosp))
    dFile.close()

doctors = []
readDoctors('doctors.txt', doctors)
doctors.sort()
idNum = input('Enter id of doctor to search: ')
res = binarySearch(doctors, idNum, 0, len(doctors)-1)

if res != -1:
    print('Doctor with id',idNum)
    print(doctors[res])
else:
    print('No such doctor')

bubbleSort(doctors)
print('Doctors by Hospital and Specialty:') 
for doctor in doctors:
    print(doctor)