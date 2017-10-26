# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 02:50:51 2017

@author: alexa

What is the 10 001st prime number?
"""

counter = 1
num = 1

while counter < 10001:
    num += 2
    isPrime = True
    if num % 2 != 0:
        for x in range(3, num // 2):
            if num % x == 0:
                isPrime = False
                break
            x += 1
        if(isPrime):
            counter += 1
            print(counter)
print(num)