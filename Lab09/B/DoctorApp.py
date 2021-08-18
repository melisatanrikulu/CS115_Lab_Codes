# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 13:24:04 2019

@author: b
"""
from doctor import *

def selectionSort(data):
    suffixStart = 0
    while suffixStart != len(data):
        for i in range(suffixStart, len(data)):
            if data[i].getSpecialty() < data[suffixStart].getSpecialty():
                data[suffixStart], data[i] = data[i], data[suffixStart]
            elif  data[i].getSpecialty() == data[suffixStart].getSpecialty():
                if data[i].getDoctorName() < data[suffixStart].getDoctorName():
                    data[suffixStart], data[i] = data[i], data[suffixStart]
        suffixStart += 1

def searchDoctors(data, hosp, endInd):
    if(endInd == -1):
        return []
    elif data[endInd].getHospital() == hosp:
        searchRes = searchDoctors(data, hosp, endInd-1)
        searchRes.append(data[endInd])
        return searchRes
    else:
        return (searchDoctors(data, hosp, endInd-1))
    
    
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


hosp = input('Enter hospital to search: ')
matches = searchDoctors(doctors, hosp, len(doctors)-1)

if len(matches) != 0:
    print('List of Doctors at',hosp)
    for doc in matches:
        print(doc)
else:
    print('No doctors in that hospital')

selectionSort(doctors)
print('\nDoctors by specialty and name:') 
for doctor in doctors:
    print(doctor)

doctorInfo = input('Enter doctor id, name, specialty and hospital: ')
info = doctorInfo.strip().split(',')
newDoc = Doctor(info[0].strip(),info[1].strip(),info[2].strip(),info[3].strip())
if newDoc not in doctors:
    doctors.append(newDoc)
    print('New doctor added')
else:
    print('Doctor exists')
    