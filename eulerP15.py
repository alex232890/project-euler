# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 20:04:35 2017

@author: alexa
"""

num = 1

"""
#calculating using the simplex # formula for pascal's triangle
#(n + 1) ^ nhat / (n!)
#in this case n = 20

for x in range(21, 41):
    num *= x
for x in range(1, 21):
    num = num // x
print(num)
"""

#calculating using the binary coefficient for the central binomial coefficient 
#(2n)! / (n!)^2 
#in this case n = 20
for x in range(1, 41):
    num *= x
divisor = 1
for x in range(1, 21):
    divisor *= x
print(num // (divisor * divisor))