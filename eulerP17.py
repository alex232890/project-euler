# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 20:21:42 2017

@author: alexa

gets the # of letters in the numbers from 1 to 1000 (inclusive)

0 = 1
1 = 2
2 = 3
3 = 4
4 = 5
5 = 6
6 = 7
7 = 8
8 = 9
9 = 10
10 = 11
11 = 12
12 = 13
13 = 14
14 = 15
15 = 16
16 = 17
17 = 18
18 = 19
19 = 20
20 = 30
21 = 40
22 = 50
23 = 60
24 = 70
25 = 80
26 = 90
27 = 100
28 = 1000
29 = and
"""
def less_than_21(words, sum_letters, x):
    return sum_letters + len(words[x - 1])
def less_than_hundred(words, sum_letters, x):
    index = 0
    x_str = str(x)
    if int(x_str[0]) == 2: index = 19
    elif int(x_str[0]) == 3: index = 20
    elif int(x_str[0]) == 4: index = 21
    elif int(x_str[0]) == 5: index = 22
    elif int(x_str[0]) == 6: index = 23
    elif int(x_str[0]) == 7: index = 24
    elif int(x_str[0]) == 8: index = 25
    elif int(x_str[0]) == 9: index = 26
    if int(x_str[1]) != 0:
        return sum_letters + len(words[index]) + len(words[int(x_str[1]) - 1])
    else:
        return sum_letters + len(words[index])
def less_than_thousand(words, sum_letters, x):
    x_str = str(x)
    length_last_digits = 0
    if int(x_str[1] + x_str[2]) < 21 and int(x_str[1] + x_str[2]) > 0:
        length_last_digits = less_than_21(words, 0, int(x_str[1] + x_str[2]))
    elif int(x_str[1] + x_str[2]) > 0:
        length_last_digits = less_than_hundred(words, 0, int(x_str[1] + x_str[2]))
    if x % 100 != 0:
        return sum_letters + len(words[int(x_str[0]) - 1]) + len(words[27]) + len(words[29]) + length_last_digits
    else:
        return sum_letters + len(words[int(x_str[0]) - 1]) + len(words[27])
def thousand(words, sum_letters, x):
    return sum_letters + len(words[0]) + len(words[28])
def main():
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "hundred", "thousand", "and"]
    sum_letters = 0
    for x in range(1, 1001):
        if x < 21:
            sum_letters = less_than_21(words, sum_letters, x)
        elif x < 100:
            sum_letters = less_than_hundred(words, sum_letters, x)
        elif x < 1000:
            sum_letters = less_than_thousand(words, sum_letters, x)
        elif x == 1000:
            sum_letters = thousand(words, sum_letters, x)
    print(sum_letters)
main()