# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 13:13:11 2019

@author: b
"""

def displayMenu():
    choice = 'z'
    while choice not in 'abc':
        print("Menu: ")
        print("(a) Find email by domain ")
        print("(b) Display numeric userNames by domain")
        print("(c) EXIT ")
        choice = input("Enter choice: ")
    return choice

def getEmailByDomain(sDomain, inFileName):
    count = 0
    outFileName = sDomain+".txt"
    inFile = open(inFileName, 'r')
    outFile = open(outFileName, 'w')
    
    for email in inFile:
        atSymbol = email.find('@')
        dotSymbol = email.find('.', atSymbol)
        domain = email[atSymbol+1:dotSymbol]
        if domain == sDomain:
            userName = email[0:atSymbol]
            outFile.write(userName+'\n')
            count += 1
    outFile.close()
    return count

def displayUsersHavingNumeric(sDomain):
    inFileName = sDomain+'.txt'
    try:
        inFile = open(inFileName,'r')
        for user in inFile:
            containsNum = False
            for pos in user:
                if pos in '1234567890':
                    containsNum = True
            if containsNum:
                print(user)
        inFile.close()
    except:
        print('No such file exists')