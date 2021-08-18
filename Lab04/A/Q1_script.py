# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 13:41:14 2019

@author: b
"""
import Q1_module

inFileName = 'input.txt'
outFileName = "output.txt"

choice = Q1_module.displayMenu()
while choice != 'c':
    if choice == 'a':
        #get email by domain			
        domain = input('Enter domain to search: ')
        numEmail = Q1_module.getEmailByDomain(domain, inFileName)
        if numEmail == 0:
            output = 'No Users Found!'
        else:
            output = str(numEmail)+' users exist in '+domain+' domain'
            print(output)
    elif choice == 'b':
        domain = input('Enter domain to search: ')
        Q1_module.displayUsersHavingNumeric(domain)
    choice = Q1_module.displayMenu()
print('Goodbye!')
