#! /usr/bin/env python
# 5-list-overlap
# 
# Take two lists, say for example these two:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements
# that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = [] #[ i for i in a for j in b if i in ]

for i in a:
    for j in b:
        if i == j:
            c.append(i)

print("List 1: " + str(a))
print("List 2: " + str(b))
print("Commons: " + str(c))