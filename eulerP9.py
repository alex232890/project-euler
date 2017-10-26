# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 14:58:42 2017

@author: alexa

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import math

for a in range(0, 1000): 
    for b in range(0, 1000):
        c = math.sqrt((a * a) + (b * b))
        if c - int(c) == 0.0:
            if a + b + int(c) == 1000:
                if a != 0 and b != 0 and int(c) != 0:
                    print(str(a * b * int(c)))