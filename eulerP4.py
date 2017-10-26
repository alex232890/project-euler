# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 15:23:30 2017

@author: alexa

A palindromic number reads the same both ways. The largest palindrome made from the 
product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
max_palindrome_int = 0
for x in range(100, 999):
    for y in range(100, 999):
        product_string = str(x * y)
        len_int = len(product_string)
        if len_int % 2 == 0:
            if product_string[0] == product_string[len_int - 1]:
                if product_string[1] == product_string[len_int - 2]:
                    if product_string[2] == product_string[len_int - 3]:
                        if x * y > max_palindrome_int:
                            max_palindrome_int = int(product_string)
        elif len_int % 2 == 1:
            if product_string[0] == product_string[len_int - 1]:
                if product_string[1] == product_string[len_int - 2]:
                    if x * y > max_palindrome_int:
                        max_palindrome_int = int(product_string)
print(max_palindrome_int)