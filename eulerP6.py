# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 02:45:08 2017

@author: alexa

Find the difference between the sum of the squares of the first one hundred natural 
numbers and the square of the sum.

"""

sum_squares = 0
square_of_sum = 0

for x in range(1, 101):
    sum_squares += x * x
    square_of_sum += x

difference = (square_of_sum * square_of_sum) - sum_squares
print(difference)