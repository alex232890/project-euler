# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 15:33:44 2017

@author: alexa
"""
"Find the sum of all the multiples of 3 or 5 below 1000."

ui = int(input("#: "))
sum = 0
if ui >= 3:
    for x in range(3, ui):
        if x % 3 == 0:
            sum += x
        elif x % 5 == 0 and x >= 5:
            sum += x
print(sum)