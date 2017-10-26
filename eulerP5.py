# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 15:36:03 2017

@author: alexa

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 
without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers 
from 1 to 20?
"""
num_int = 40 #starts at 40 since the smallest # for starting has to be divisible by 20
ans_int = 0
tracker_bool = True
iter_int = 0
while(tracker_bool):
    isDivisible_bool = True
    for x in range(1, 21):
        if num_int % x != 0:
            isDivisible_bool = False
    if isDivisible_bool:
        ans_int = num_int
        tracker_bool = False
    num_int += 2
print(ans_int)