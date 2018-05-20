#! /usr/bin/env python
# 5-extra-2
#
# Write this in one line of Python

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = [i for i in a for j in b if i == j]

a.sort()
b.sort()
c.sort()

print("List 1: " + str(a))
print("List 2: " + str(b))
print("Commons: " + str(c))
