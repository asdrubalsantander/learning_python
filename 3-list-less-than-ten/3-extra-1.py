#! /usr/bin/env python
# 3-extra-1
#
# Instead of printing the elements one by one, make a new list that has
# all the elements less than 5 from this list in it and print out this new list.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
for i in a:
    if i < 5:
        b.append(i)

print(b)
