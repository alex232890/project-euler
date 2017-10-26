# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 15:14:04 2017

@author: alexa

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million
"""
#this program uses the sieve of atkin algorithm
import math
sum_int = 5 #sum starts out with 2 and 3 added to make coding easier

s = [1,7,11,13,17,19,23,29, 31,37,41,43,47,49,53,59]
limit = int(input("#: "))
prime_list = list()
prime_list = [False] * (limit + 1)

for x in range(1, int(math.sqrt(limit)) + 1):
    for y in range(1, int(math.sqrt(limit)) + 1):
        a = (4 * (x**2)) + (y ** 2)
        if a <= limit and  (a % 12 == 1 or a % 12 == 5):
            prime_list[a] = not prime_list[a]
        a = (3 * (x**2)) + (y ** 2)
        if a <= limit and a % 12 == 7:
            prime_list[a] = not prime_list[a]
        a = (3 * (x ** 2)) - (y ** 2)
        if x > y and a <= limit and a % 12 == 11:
            prime_list[a] = not prime_list[a]
for x in range(5, int(math.sqrt(limit))):
    if prime_list[x]:
        for y in range(x**2, limit + 1, x**2):
            prime_list[y] = False
for x in range(5, limit):
    if prime_list[x]:
        sum_int += x
print(sum_int)
"""
for x in range(7, 2000001):
    if x % 2 != 0:
        y = 3
        b = True
        while(y < x // 2):
            if x % y == 0:
                y = x
                b = False
            y += 2
        s += x if b else 0
print(s)
"""