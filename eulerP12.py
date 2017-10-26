# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 15:31:49 2017

@author: alexa
"""
x = 0
y = 1
tri = 0
while True:
    for z in range(x, y):
        tri += z
    divisorCount = 2
    for z in range(2, tri//2 + 1):
        if tri % z == 0:
            divisorCount += 1
    if divisorCount > 500:
        print(tri)
        break
    else:
        x += 1
        y += 1
        #print(divisorCount)