# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 08:58:03 2019

@author: user
"""
import ModuleQ1

inFileName = 'users.txt'
outFileName = 'emails.txt'
choice = ModuleQ1.displayMenu()
while choice != 3:
    if choice == 1:
        numEmails = ModuleQ1.generateEmailAddresses(inFileName, outFileName)
        print(numEmails,'email addresses created...')
    elif choice == 2:
        ModuleQ1.displayEmailAddresses(outFileName)
    choice = ModuleQ1.displayMenu()
print('Program ended...')