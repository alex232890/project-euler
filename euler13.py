# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 16:24:39 2017

@author: alexa
"""

nums_file = open("euler13_nums.txt", "r")
x = 1
for line in nums_file:
    x += int(line)
x_str = str(x)
print_str = ""
x = 0
for char in x_str:
    print_str += char
    x += 1
    if x == 10:
        break
print(print_str)
