# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 15:43:55 2017

@author: alexa
"""

"By considering the terms in the Fibonacci sequence whose values do not exceed four"
"million, find the sum of the even-valued terms."

ui = int(input("#: "))
fib1 = 0
fib2 = 1
sum = 0
while fib1 <= ui and fib2 <= ui:
    if fib1 % 2 == 0 and fib1 > 1 and fib1 > fib2:
        print(str(fib1) + " at fib1")
        sum += fib1
    elif fib2 % 2 == 0 and fib2 > 1 and fib2 < fib1:
        print(str(fib2) + " at fib2")
        sum += fib2
    if fib1 > fib2:
        fib2 += fib1
    else:
        fib1 += fib2
print(sum)