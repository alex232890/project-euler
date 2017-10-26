# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 15:15:25 2017

@author: alexa

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?


"""

ui_int = int(input("#: "))
iter_int = 3
largest_prime_factor_int = 0
while ui_int > 1:
    if ui_int % iter_int == 0:
        largest_prime_factor_int = iter_int
        ui_int = ui_int // iter_int
    iter_int += 2
print(largest_prime_factor_int)