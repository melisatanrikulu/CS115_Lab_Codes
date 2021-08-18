# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 12:53:43 2019

@author: user
"""
"""
calculates the GPA for each student in the dictionary,
by finding the credits for each course, and multiplying by
the points for the grade received. Write the result for each
student to the output file, gpa.txt
"""
def calculateGPA(sDict, cDict, gDict):
    outGrades = open('gpa.txt', 'w')
    for s in sDict:
        total_credits = 0
        total_points = 0
        for course in sDict[s]:
            total_credits += int(cDict[course[0]])
            grade = course[1]
            total_points += gDict[grade] * int(cDict[course[0]])
        outGrades.write(s+'\t'+str(total_points/total_credits)+'\n')
    outGrades.close()
#reads data from the file passed as a parameter and finds the student
#with the minimum gpa, and returns their id/gpa
def findMinGpa(fileName):
    sFile = open('gpa.txt', 'r')
    minGpa = 5
    minId=''
    for line in sFile:
        stu = line.split('\t')
        if float(stu[1]) < minGpa:
            minGpa = float(stu[1])
            minId = stu[0]
    sFile.close()
    return (minId,minGpa)
#prints student id and list of courses as shown in 
#sample output
def printDict(sDict):
    for s in sDict:
        print(s)
        for item in sDict[s]:
            print('\t',item[0],':',item[1])
#dictionary to store grades and points           
gDict = {'A+':4.0,'A':4.0,'A-':3.7,'B+':3.3,'B':3.0,'B-':2.7,'C+':2.3,'C':2.0,'C-':1.7,'D+':1.3,'D':1.0,'F':0.0,}
sDict = {}
cDict = {}

#read file and add students/course grades to dictionary
sFile = open('student_data.txt','r')
for student in sFile:
    sData = student.strip().split(';')
    numStudents = len(sData)//2
    sId = sData[0]
    cData = []
    for c in range(1,numStudents*2,2):
        course = (sData[c], sData[c+1])
        cData.append(course)
    sDict[sId]=cData
sFile.close()

#print students and courses
print('Students:')
printDict(sDict)

#add courses to course/credits dictionary
cFile = open('course_data.txt','r')
for course in cFile:
    cData = course.strip().split(';')
    cDict[cData[0]]= cData[1]
cFile.close()

#calculate the GPA of all students and write to file
calculateGPA(sDict,cDict,gDict)

#display the list of courses and grades for student with min GPA
minId, minGPA = findMinGpa('gpa.txt')
minCourses = sDict[minId]
print('Student with Lowest GPA:{0:s} ({1:.2f})'.format(minId, minGPA))
print('List of courses:')           
for course in minCourses:
    print(course[0],':',course[1])
        