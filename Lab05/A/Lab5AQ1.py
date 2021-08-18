# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 10:39:22 2019

@author: user
"""
def sectionAverage(sDict):
    averages = []
    for i in sDict:
        sTotal = 0
        sCount = 0
        for stu in sDict[i]:
            sTotal += stu[1]
            sCount += 1
        averages.append(sTotal/sCount)
    return averages

def changeSection(sDict, idNum, sec):
    for section in sDict:
        for stu in sDict[section]:
            if idNum in stu:
                if section != sec:
                    sDict[section].remove(stu)
                    sDict[sec].append(stu)
                    return True
                else:
                    print('Student',idNum,'already assigned to section')
                    return False
    print('Student',idNum,'does not exist')
    return False
def maxGrade(sDict):
    maxGrade = 0
    maxId = 0
    for i in sDict:
        for stu in sDict[i]:
            if stu[1] > maxGrade:
                maxGrade = stu[1]
                maxId = stu[0]
    
    return (maxId, maxGrade) 

def printDict(sDict):
    for i in sDict:
        print('Section',i,':')
        for stu in sDict[i]:
            print('\t',stu)
            
stuDict = {}
sFile = open('CS115.txt', 'r')
for stu in sFile:
    stuData = stu.split(';')
    if int(stuData[1]) not in stuDict:
        stuDict[int(stuData[1])] = [(stuData[0], int(stuData[2]))]
    else:
        stuDict[int(stuData[1])].append((stuData[0], int(stuData[2])))

print('Section Data: ')
printDict(stuDict)

sec_avg = sectionAverage(stuDict)
print('Section Averages: ',sec_avg)

changeSection(stuDict, '21641234',2)
changeSection(stuDict, '22141734',3)
changeSection(stuDict, '21112222',3)
print('Updated Section Data: ')
printDict(stuDict)
mId,mGrade = maxGrade(stuDict)
print('Student with highest score:',mId,'(',mGrade,')')