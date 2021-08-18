# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 09:51:30 2019

@author: user
"""
def displayMenu():
    choice = -1
    while  choice < 1  or choice > 3:
        print('Menu: ')
        print('(1) Generate Email Addresses')
        print('(2) Display Email Addresses')
        print('(3) EXIT ')
        choice = int(input('Enter choice: '))
    return choice
    
def generateEmailAddresses(fileInput, fileOutput):
    inFile = open(fileInput,'r')

    count = 0
    for line in inFile:
        count += 1
    inFile.close()
    inFile = open(fileInput,'r')
    for i in range(count//3):
        name = inFile.readline().strip()
        surname = inFile.readline().strip()
        dept = inFile.readline().strip()

        userName = name[0]+surname
        n = searchUserExists(userName, dept, fileOutput)
        userName += str(n+1)
        emailAddress = userName+'@'+dept.lower()+'.'+'bilkent.edu.tr'

        outFile = open(fileOutput, 'a')
        outFile.write(emailAddress+'\n')
        outFile.close()
    inFile.close()
    return count //3
    
def searchUserExists(sUser, sDept, fileName):
    n = 0
    try:
        inFile = open(fileName)
        for email in inFile:
            atPos = email.find('@')
            userName =  email[0:atPos]
            dotPos = email.find('.',atPos)
            dept = email[atPos+1:dotPos]
            if sUser.lower() in userName.lower() and sDept.lower() == dept.lower():
                n += 1
        inFile.close()
    except:
        found = False
    return n
    
def displayEmailAddresses(fileName):
    inFile = open(fileName, 'r')
    for email in inFile:
        print(email)
