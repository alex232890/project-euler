# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 21:34:11 2017

@author: alexa
"""
def main():
    triangle = open("eulerP18_triangle.txt", "r")
    num_rows = 0
    for line in triangle:
        num_rows += 1
    tri_arr = [0 for x in range(num_rows) for y in range(num_rows)]
    triangle.seek(0)
    for x in range(0, num_rows):
        line = triangle.readline()
        print(len(line))
        for y in range(0, len(line), 2):
            v  tri_arr[x][y] = (str(line[y]) + str(line[y + 1]))
    print(tri_arr)
#def operations():
    

def print_arr(triangle, num_rows): #prints the array of numbers
    num_spaces = ""
    for x in range(0, num_rows):
        num_spaces += "   "
    for x in range(0, len(triangle)):
        line = ""
        for y in range(0, len(triangle[0])):
            line = format_triangle(triangle[x][y], line)
        print(num_spaces + line)
        num_spaces = num_spaces.replace(" ", "", 2)
    
def format_triangle(val, line): #determines how many spaces between numbers
    if val >= 100:
        line += " " + str(val)
    elif val >= 10:
        line += "  " + str(val)
    elif val > 0:
        line += "   " + str(val)
    return line
main()