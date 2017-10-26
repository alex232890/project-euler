# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 17:58:30 2017

@author: alexa

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) 
contains 10 terms. Although it has not been proved yet (Collatz Problem), it is 
thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
"""

def collatz(n):
    return n/2 if n % 2 == 0 else (3 * n) + 1

def main():
    chain_count_max = 0
    x_val_of_chain_count_max = 0
    for x in range(999999, 0, -2): #skipping evens as those will divide to 1 faster than odds
        n = x
        chain_count = 0
        while(n > 1):
            n = int(collatz(n))
            chain_count += 1
        if chain_count > chain_count_max:
            chain_count_max = chain_count
            x_val_of_chain_count_max = x
            print(x_val_of_chain_count_max)
    print(chain_count_max)  

main()