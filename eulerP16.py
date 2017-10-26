# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 20:18:33 2017

@author: alexa
"""

n = 1

for x in range(1000):
    n *= 2
    
n_str = str(n)

sum_digits_of_n = 0
for c in n_str:
    sum_digits_of_n += int(c)
    
print(sum_digits_of_n)