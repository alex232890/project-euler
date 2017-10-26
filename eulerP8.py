# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 14:37:08 2017

@author: alexa
"""

nums_str = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
max_product = 1

for x in range(0, len(nums_str) - 13):
    product = 1
    for y in range(x, x + 13):
        product *= int(nums_str[y])
    max_product = product if product > max_product else max_product

print(max_product)

#if a is b is true, then a == b is true also as they refer to the same object and thus comparing an object to itself with == should yield true
#print = 42 is a valid assignment as print is a reference to a function, however, if this is done, then the print function can't be called as the word now refers to a variable

"""
x = 0 y = 2 z = 4
0 acts as a False statement in a boolean expression

result = (x and y) or (y and z)
x is 0 so (x and y is false)
(y and z) returns 4
thus (x and y) or (y and z) returns the value of 4


s = 'Columbia University'
s[0:9] is "Columbia "
print(list(s)) prints out the list of each char in s
s[0:8:2] goes from 0 to 8 in the string with a step size of 2, so "Clmi'


'tuna' in 'fortunate' returns True
'forte' in 'fortunate' returns False

x = "-1,-2,-3,-4,-5".split(',')
x will be [-1, -2, -3, -4, -5]

"list of words".split() will give ['list', 'of', 'words']


x = "{} is {} years old"
x.format('Anna', 28)  {} will be filled in left to right
this will give "Anna is 28 years old"

print("Pi is {:.4f}".format(math.pi)) will print 3.1416 (4 decimal places)

bad_chars = string.whitespace + string.punctuation

10/2/2017

"""
