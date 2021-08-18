# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 13:13:08 2019

@author: b
"""
import random
def generate_password(n):
    vow = n//2
    num = n - vow
    pwd = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(vow):
        ch = str(random.choice(alphabet))
        upper = random.randint(0,1)
        if upper == 0:
            ch = ch.upper()
        pwd += ch
    for j in range(num):
        pwd += str(random.randint(0,9))
    return pwd

n = int(input('Enter password length (-1 to quit): '))
while n > 0:
    while n < 5:
        print('Password minimum length is 5')
        n = int(input('Enter password length: '))
    pwd = generate_password(n)
    print('Your password is:',pwd)
    n = int(input('Enter password length (-1 to quit): '))

    